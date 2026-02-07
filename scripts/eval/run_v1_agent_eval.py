from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

from scripts.eval.evaluate_recommendations import (
    compute_metrics,
    normalize_tool_id,
    unique_in_order,
)
from scripts.benchmark.generate_llm_predictions import extract_predictions, load_jsonl
from scripts.llm.llm_providers import (
    call_anthropic,
    call_gemini,
    call_ollama,
    call_openai_compatible,
)

logging.basicConfig(level=logging.INFO, format="%(message)s")
LOGGER = logging.getLogger(__name__)


def _slug(text: str) -> str:
    text = (text or "").strip()
    text = re.sub(r"[^a-zA-Z0-9._-]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text or "unknown"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run a tool-recommendation agent on benchmark v1 and evaluate it "
            "with Hit@k / MRR@k / nDCG@k."
        )
    )
    parser.add_argument(
        "--gold",
        type=Path,
        default=Path("data/benchmark/v1_items.jsonl"),
        help="Benchmark JSONL file with {'id','query','tools',...} (default: v1).",
    )
    parser.add_argument(
        "--filter-topic",
        action="append",
        default=None,
        help=(
            "Only evaluate items whose metadata.topic matches one of these values "
            "(repeatable)."
        ),
    )
    parser.add_argument(
        "--filter-tutorial-regex",
        type=str,
        default=None,
        help="Only evaluate items whose tutorial_id matches this regex (case-insensitive).",
    )
    parser.add_argument(
        "--filter-tool-regex",
        type=str,
        default=None,
        help="Only evaluate items whose gold tools contain a tool_id matching this regex (case-insensitive).",
    )
    parser.add_argument(
        "--filter-tool-section",
        action="append",
        default=None,
        help=(
            "Only evaluate items whose gold tools fall under one of these Galaxy tool panel sections "
            "according to --tool-sections-file (repeatable)."
        ),
    )
    parser.add_argument(
        "--tool-sections-file",
        type=Path,
        default=Path("data/tool_catalog/usegalaxy_org_by_section.json"),
        help="JSON file with a 'by_section' mapping used by --filter-tool-section.",
    )
    parser.add_argument(
        "--filter-query-regex",
        type=str,
        default=None,
        help="Only evaluate items whose query text matches this regex (case-insensitive).",
    )
    parser.add_argument(
        "--filter-id-regex",
        type=str,
        default=None,
        help="Only evaluate items whose id matches this regex (case-insensitive).",
    )
    parser.add_argument(
        "--output-predictions",
        type=Path,
        default=None,
        help="Destination JSONL for {'id','predictions'} entries.",
    )
    parser.add_argument(
        "--output-metrics",
        type=Path,
        default=None,
        help="Destination JSON for aggregated metrics.",
    )
    parser.add_argument(
        "--output-markdown",
        type=Path,
        default=None,
        help=(
            "Destination Markdown report. Defaults to "
            "<results-dir>/<provider>/<model>/<run-name?>/report.md."
        ),
    )
    parser.add_argument(
        "--no-markdown",
        action="store_true",
        help="Do not generate the Markdown report.",
    )
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=Path("runs/eval"),
        help="Root folder for auto-named results (default: runs/eval).",
    )
    parser.add_argument(
        "--run-name",
        type=str,
        default=None,
        help=(
            "Optional extra subfolder under provider/model, e.g. "
            "'candidates50_temp0'. If omitted, writes directly under provider/model."
        ),
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Skip query IDs already present in the predictions file for this run.",
    )
    parser.add_argument(
        "--report-only",
        action="store_true",
        help="Do not generate predictions; only recompute metrics and (optionally) rewrite report.md from existing predictions.jsonl.",
    )
    parser.add_argument(
        "--agent",
        type=str,
        default="llm",
        choices=("llm", "llm_minimal", "standalone", "oracle", "first_tutorial_tool"),
        help=(
            "Agent strategy: "
            "'llm' calls an OpenAI-compatible chat completions endpoint; "
            "'llm_minimal' calls the LLM with only the query (no candidate list); "
            "'standalone' runs the exported Galaxy agent (pydantic-ai) with tool-calling over a local tool catalog; "
            "'oracle' returns gold tools (sanity check only); "
            "'first_tutorial_tool' returns the top retrieved tool-catalog candidates."
        ),
    )
    parser.add_argument(
        "--tool-catalog",
        type=Path,
        default=Path("data/tool_catalog/usegalaxy_org_tools.jsonl"),
        help=(
            "Tool catalog JSONL used to build candidate tools for the LLM. "
            "Expected fields per line: tool_id, name, description (at minimum)."
        ),
    )
    parser.add_argument(
        "--candidate-k",
        type=int,
        default=50,
        help="How many candidate tools to include in the LLM prompt.",
    )
    parser.add_argument(
        "--dedupe-candidates-by-base",
        action="store_true",
        default=True,
        help=(
            "De-duplicate retrieved candidates by base tool ID (ignore toolshed version segment) "
            "and keep only the best-scoring version per base. Enabled by default."
        ),
    )
    parser.add_argument(
        "--no-dedupe-candidates-by-base",
        action="store_false",
        dest="dedupe_candidates_by_base",
        help="Disable base-ID de-duplication for retrieved candidates.",
    )
    parser.add_argument(
        "--no-write-candidates",
        action="store_true",
        help="Do not include the retrieved tool shortlist in predictions.jsonl output.",
    )
    parser.add_argument(
        "--candidate-strategy",
        type=str,
        default="llm_keywords",
        choices=("token", "llm_keywords"),
        help=(
            "How to build the candidate tool shortlist. "
            "'token' uses local token matching on the raw query. "
            "'llm_keywords' asks the LLM for search keywords first, then retrieves candidates from the tool catalog."
        ),
    )
    parser.add_argument(
        "--candidate-search",
        type=str,
        default="keyword",
        choices=("keyword", "token"),
        help=(
            "How to search the tool catalog given a query/keywords. "
            "'keyword' does phrase/substring matching over tool_id/name/description and (when present) input/output "
            "details, and returns latest-only per base. "
            "'token' uses the local token inverted-index (legacy)."
        ),
    )
    parser.add_argument(
        "--keyword-model",
        type=str,
        default=None,
        help="Optional model override used for --candidate-strategy llm_keywords (defaults to --model).",
    )
    parser.add_argument(
        "--keyword-top-n",
        type=int,
        default=8,
        help="How many keywords/phrases to request from the LLM (default: 8).",
    )
    parser.add_argument(
        "--standalone-catalog",
        type=str,
        default="whoosh",
        choices=("memory", "whoosh"),
        help=(
            "Tool catalog implementation for --agent standalone. "
            "'whoosh' best matches Galaxy toolbox search; 'memory' is a lightweight fallback."
        ),
    )
    parser.add_argument(
        "--standalone-index-dir",
        type=Path,
        default=Path(".tool_search_index"),
        help="Where to store the Whoosh index for --agent standalone (default: .tool_search_index).",
    )
    parser.add_argument(
        "--standalone-max-tools",
        type=int,
        default=None,
        help="Optional cap on the number of tools loaded from --tool-catalog for --agent standalone (debug only).",
    )
    parser.add_argument(
        "--standalone-request-limit",
        type=int,
        default=1000,
        help=(
            "Max model requests per query for --agent standalone (pydantic-ai UsageLimits.request_limit). "
            "Default: 1000. Set <=0 for no limit (not recommended)."
        ),
    )
    parser.add_argument(
        "--standalone-tool-calls-limit",
        type=int,
        default=200,
        help=(
            "Max tool calls per query for --agent standalone (pydantic-ai UsageLimits.tool_calls_limit). "
            "Default: 200. Set <=0 for no limit (not recommended)."
        ),
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=10,
        help="Request up to this many predictions per query.",
    )
    parser.add_argument(
        "--k",
        type=str,
        default="1,3,5,10",
        help="Comma-separated evaluation cutoffs (default: 1,3,5,10).",
    )
    parser.add_argument(
        "--normalize-tools",
        action="store_true",
        help="Normalize toolshed IDs by removing the version (last path segment).",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-4o-mini",
        help="LLM model name to request from the API (agent=llm).",
    )
    parser.add_argument(
        "--provider",
        type=str,
        default="openai_compatible",
        choices=("openai_compatible", "anthropic", "gemini", "ollama"),
        help=(
            "LLM provider protocol. 'openai_compatible' works with OpenAI-style "
            "/v1/chat/completions endpoints (many providers support this)."
        ),
    )
    parser.add_argument(
        "--api-url",
        type=str,
        default="https://api.openai.com/v1/chat/completions",
        help=(
            "Provider endpoint. "
            "openai_compatible: full /v1/chat/completions URL; "
            "anthropic: https://api.anthropic.com/v1/messages; "
            "gemini: https://generativelanguage.googleapis.com/v1beta; "
            "ollama: http://localhost:11434/api/chat."
        ),
    )
    parser.add_argument(
        "--api-key",
        type=str,
        default=None,
        help="Optional API key (fallback depends on --provider).",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="Sampling temperature for the LLM (agent=llm).",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Seconds to wait between API calls (agent=llm).",
    )
    parser.add_argument(
        "--max-queries",
        type=int,
        default=None,
        help="Stop after scoring this many queries (default: all).",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help=(
            "Deprecated alias for --resume. Prefer --resume. "
            "If either is set, existing IDs are skipped."
        ),
    )
    return parser.parse_args()


def _compile_optional_regex(pattern: Optional[str]) -> Optional[re.Pattern[str]]:
    if not pattern:
        return None
    return re.compile(pattern, re.IGNORECASE)


def filter_gold_items(args: argparse.Namespace, gold_items: List[dict]) -> List[dict]:
    topics = set(t.strip() for t in (args.filter_topic or []) if isinstance(t, str) and t.strip())
    tutorial_re = _compile_optional_regex(args.filter_tutorial_regex)
    tool_re = _compile_optional_regex(args.filter_tool_regex)
    query_re = _compile_optional_regex(args.filter_query_regex)
    id_re = _compile_optional_regex(args.filter_id_regex)
    sections = set(
        s.strip()
        for s in (args.filter_tool_section or [])
        if isinstance(s, str) and s.strip()
    )
    section_tool_bases: Optional[set[str]] = None
    if sections:
        if not args.tool_sections_file.exists():
            raise FileNotFoundError(
                f"--filter-tool-section requires --tool-sections-file, but it does not exist: {args.tool_sections_file}"
            )
        payload = json.loads(args.tool_sections_file.read_text(encoding="utf-8"))
        by_section = payload.get("by_section") if isinstance(payload, dict) else None
        if not isinstance(by_section, dict):
            raise ValueError(
                f"Expected a JSON object with 'by_section' in {args.tool_sections_file}"
            )
        bases: set[str] = set()
        for sec in sections:
            tools = by_section.get(sec)
            if not isinstance(tools, list):
                continue
            for t in tools:
                if isinstance(t, str) and t:
                    bases.add(normalize_tool_id(t))
        section_tool_bases = bases

    if not (topics or tutorial_re or tool_re or query_re or id_re or sections):
        return gold_items

    filtered: List[dict] = []
    for item in gold_items:
        qid = item.get("id")
        if id_re and (not isinstance(qid, str) or not id_re.search(qid)):
            continue

        if topics:
            topic = ((item.get("metadata") or {}).get("topic")) or ""
            if topic not in topics:
                continue

        if tutorial_re:
            tutorial_id = item.get("tutorial_id") or ""
            if not isinstance(tutorial_id, str) or not tutorial_re.search(tutorial_id):
                continue

        if query_re:
            query = item.get("query") or ""
            if not isinstance(query, str) or not query_re.search(query):
                continue

        if tool_re:
            tools = item.get("tools") or []
            if not isinstance(tools, list) or not any(isinstance(t, str) and tool_re.search(t) for t in tools):
                continue
        if section_tool_bases is not None:
            tools = item.get("tools") or []
            if not isinstance(tools, list):
                continue
            tool_bases = [normalize_tool_id(t) for t in tools if isinstance(t, str)]
            if not any(tb in section_tool_bases for tb in tool_bases):
                continue

        filtered.append(item)
    return filtered


def resolve_output_paths(args: argparse.Namespace) -> Tuple[Path, Path]:
    """
    If the user provided explicit paths, use them.
    Otherwise, use: <results-dir>/<provider>/<model>/<run-name?>/{predictions.jsonl,metrics.json}
    """
    if args.output_predictions is not None and args.output_metrics is not None:
        return args.output_predictions, args.output_metrics

    provider = _slug(getattr(args, "provider", "unknown"))
    model = _slug(getattr(args, "model", "unknown"))
    base = args.results_dir / provider / model
    if args.run_name:
        base = base / _slug(args.run_name)
    predictions = args.output_predictions or (base / "predictions.jsonl")
    metrics = args.output_metrics or (base / "metrics.json")
    return predictions, metrics


def resolve_markdown_path(args: argparse.Namespace) -> Path:
    if args.output_markdown is not None:
        return args.output_markdown
    provider = _slug(getattr(args, "provider", "unknown"))
    model = _slug(getattr(args, "model", "unknown"))
    base = args.results_dir / provider / model
    if args.run_name:
        base = base / _slug(args.run_name)
    return base / "report.md"


def _normalize_list(values: Iterable[str], do_normalize: bool) -> List[str]:
    if not do_normalize:
        return unique_in_order(values)
    return unique_in_order(normalize_tool_id(v) for v in values)


def _ensure_llm_key(args: argparse.Namespace) -> str:
    try:
        from dotenv import load_dotenv  # type: ignore
    except ModuleNotFoundError:
        load_dotenv = None
    if load_dotenv is not None:
        load_dotenv(dotenv_path=Path(".env"))
    if args.provider == "anthropic":
        api_key = args.api_key or os.environ.get("ANTHROPIC_API_KEY")
    elif args.provider == "gemini":
        api_key = args.api_key or os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    elif args.provider == "ollama":
        api_key = ""
    else:
        api_key = args.api_key or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        if args.provider == "anthropic":
            LOGGER.error("No API key provided. Set ANTHROPIC_API_KEY or pass --api-key.")
        elif args.provider == "gemini":
            LOGGER.error("No API key provided. Set GEMINI_API_KEY/GOOGLE_API_KEY or pass --api-key.")
        else:
            LOGGER.error("No API key provided. Set OPENAI_API_KEY or pass --api-key.")
        sys.exit(1)
    return api_key


def _load_existing_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {item["id"] for item in load_jsonl(path) if isinstance(item.get("id"), str)}


def _write_prediction(path: Path, qid: str, predictions: List[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as out_handle:
        out_handle.write(
            json.dumps({"id": qid, "predictions": predictions}, ensure_ascii=False)
            + "\n"
        )


def _write_prediction_record(path: Path, record: Dict[str, Any]) -> None:
    qid = record.get("id")
    if not isinstance(qid, str) or not qid:
        raise ValueError("Prediction record missing string 'id'")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as out_handle:
        out_handle.write(json.dumps(record, ensure_ascii=False) + "\n")


_STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "before",
    "by",
    "can",
    "data",
    "dataset",
    "do",
    "for",
    "from",
    "have",
    "how",
    "i",
    "in",
    "into",
    "is",
    "it",
    "need",
    "of",
    "on",
    "or",
    "run",
    "should",
    "that",
    "the",
    "this",
    "to",
    "tool",
    "use",
    "using",
    "what",
    "which",
    "with",
}


def _tokenize(text: str) -> List[str]:
    text = text.lower()
    parts = re.split(r"[^a-z0-9]+", text)
    tokens: List[str] = []
    for part in parts:
        if len(part) < 2:
            continue
        if part in _STOPWORDS:
            continue
        tokens.append(part)
    return tokens


def _tool_text(tool: dict) -> str:
    tool_id = str(tool.get("tool_id") or "")
    name = str(tool.get("name") or "")
    desc = str(tool.get("description") or "")
    io_parts: List[str] = []
    help_text = str(tool.get("tool_help_text") or "")
    if not help_text:
        # Backward compatibility for older merged catalogs.
        help_text = str(tool.get("help_text") or "")

    def add_from_mapping(m: dict) -> None:
        for k in ("name", "label", "type", "help", "argument", "extensions", "format"):
            v = m.get(k)
            if isinstance(v, str) and v.strip():
                io_parts.append(v.strip())
            elif isinstance(v, list):
                # Keep simple scalar lists (e.g., extensions).
                for item in v:
                    if isinstance(item, str) and item.strip():
                        io_parts.append(item.strip())

    def add_from_list(xs: list) -> None:
        for x in xs:
            if isinstance(x, str) and x.strip():
                io_parts.append(x.strip())
            elif isinstance(x, dict):
                add_from_mapping(x)

    # Include IO details when available (built by the tool-catalog script).
    # Prefer the flattened input params when present; fall back to raw fields.
    ipf = tool.get("input_params_flat")
    if isinstance(ipf, list):
        add_from_list(ipf)

    inputs_raw = tool.get("inputs_raw")
    if isinstance(inputs_raw, list):
        add_from_list(inputs_raw)

    outputs_raw = tool.get("outputs_raw")
    if isinstance(outputs_raw, list):
        add_from_list(outputs_raw)

    io_text = " ".join(io_parts).strip()
    return " ".join([tool_id, name, desc, help_text, io_text]).strip()


def load_tool_catalog(path: Path) -> List[dict]:
    if not path.exists():
        raise FileNotFoundError(
            f"Tool catalog not found: {path}. "
            "Build a usegalaxy.org tool snapshot and point --tool-catalog to it."
        )
    tools: List[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            item = json.loads(line)
            if not isinstance(item, dict):
                continue
            if not item.get("tool_id"):
                continue
            tools.append(item)
    return tools


def _collapse_predictions(pred_items_raw: List[dict]) -> Dict[str, dict]:
    """
    Collapse possibly-duplicated predictions.jsonl records by id.

    We prefer the most recent record that has a non-empty `predictions` list.
    This makes evaluation/reporting robust when a run is resumed and accidentally
    appends duplicate ids (e.g., after partial failures).
    """

    best_by_id: Dict[str, dict] = {}
    for item in pred_items_raw:
        if not isinstance(item, dict):
            continue
        qid = item.get("id")
        if not isinstance(qid, str) or not qid:
            continue
        preds = item.get("predictions") or []
        has_preds = isinstance(preds, list) and any(isinstance(p, str) and p for p in preds)

        prev = best_by_id.get(qid)
        if prev is None:
            best_by_id[qid] = item
            continue

        prev_preds = prev.get("predictions") or []
        prev_has_preds = isinstance(prev_preds, list) and any(
            isinstance(p, str) and p for p in prev_preds
        )

        # Prefer non-empty predictions; otherwise keep the latest.
        if has_preds:
            best_by_id[qid] = item
        elif not prev_has_preds:
            best_by_id[qid] = item

    return best_by_id


def _version_key(version: str) -> tuple:
    # Similar to the helper in scripts/benchmark/generate_manual_queries.py
    parts = re.split(r"[._+-]", (version or "").strip())
    key: List[tuple] = []
    for part in parts:
        if part.isdigit():
            key.append((0, int(part)))
        else:
            key.append((1, part))
    return tuple(key)


def build_latest_tools(tools: List[dict]) -> List[dict]:
    """
    Collapse multiple versions to a single 'latest' tool per base_id (toolshed version segment).
    Output tools keep their original fields, but are unique by normalize_tool_id(tool_id).
    """
    best_by_base: Dict[str, dict] = {}
    for tool in tools:
        tool_id = str(tool.get("tool_id") or "")
        if not tool_id:
            continue
        base = normalize_tool_id(tool_id)
        # Prefer explicit version field; otherwise derive from toolshed path.
        version = str(tool.get("version") or "")
        if not version and tool_id.startswith("toolshed.g2.bx.psu.edu/"):
            version = tool_id.split("/")[-1]

        current = best_by_base.get(base)
        if current is None:
            best_by_base[base] = tool
            best_by_base[base]["_version_key"] = _version_key(version)
            continue

        cur_v = current.get("_version_key")
        new_v = _version_key(version)
        if not isinstance(cur_v, tuple) or new_v > cur_v:
            tool["_version_key"] = new_v
            best_by_base[base] = tool

    # Drop helper field for output cleanliness.
    out = list(best_by_base.values())
    for t in out:
        t.pop("_version_key", None)
    return out


def build_inverted_index(tools: List[dict]) -> tuple[Dict[str, List[int]], Dict[str, float]]:
    """
    Build a simple token->tool_index inverted index with IDF weights.
    """
    postings: Dict[str, List[int]] = {}
    df: Dict[str, int] = {}
    for idx, tool in enumerate(tools):
        seen_tokens = set(_tokenize(_tool_text(tool)))
        for tok in seen_tokens:
            postings.setdefault(tok, []).append(idx)
            df[tok] = df.get(tok, 0) + 1

    n = max(1, len(tools))
    idf: Dict[str, float] = {}
    for tok, freq in df.items():
        # Smooth IDF; simple and dependency-free
        idf[tok] = 1.0 + (0.0 if freq <= 0 else (math_log((n + 1) / (freq + 1))))
    return postings, idf


def math_log(x: float) -> float:
    # local helper to avoid importing math at top for a single call-site
    import math

    return math.log(x)


def select_candidates(
    query: str,
    tools: List[dict],
    postings: Dict[str, List[int]],
    idf: Dict[str, float],
    candidate_k: int,
    dedupe_by_base: bool = True,
) -> List[dict]:
    tokens = _tokenize(query)
    scores: Dict[int, float] = {}
    for tok in tokens:
        tool_idxs = postings.get(tok)
        if not tool_idxs:
            continue
        weight = idf.get(tok, 1.0)
        for idx in tool_idxs:
            scores[idx] = scores.get(idx, 0.0) + weight

    if not scores:
        # Deterministic fallback: first N tools from the snapshot.
        return tools[:candidate_k]

    ranked = sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))
    out: List[dict] = []
    seen_base: set[str] = set()
    for idx, _score in ranked[:candidate_k]:
        tool = tools[idx]
        if dedupe_by_base:
            base = normalize_tool_id(str(tool.get("tool_id") or ""))
            if base in seen_base:
                continue
            seen_base.add(base)
        out.append(tool)
        if len(out) >= candidate_k:
            break
    return out


def select_candidates_by_keywords(
    *,
    keywords: List[str],
    tools_latest: List[dict],
    candidate_k: int,
) -> List[dict]:
    """
    Keyword/phrase matching over tool text built from:
    - tool_id, name, description
    - plus input/output details when present (e.g., input_params_flat / inputs_raw / outputs_raw)

    Assumes tools_latest is already latest-only.
    """
    candidate_k = max(0, int(candidate_k))
    if candidate_k == 0:
        return []

    kw_norm = [k.strip().lower() for k in keywords if isinstance(k, str) and k.strip()]
    if not kw_norm:
        # Fallback: deterministic slice
        return tools_latest[:candidate_k]

    scored: List[tuple[float, int]] = []
    for idx, tool in enumerate(tools_latest):
        text = _tool_text(tool).lower()
        score = 0.0
        for kw in kw_norm:
            if kw in text:
                # Weight longer phrases slightly higher.
                score += 1.0 + min(1.0, len(kw) / 10.0)
        if score > 0:
            scored.append((score, idx))

    if not scored:
        return tools_latest[:candidate_k]

    scored.sort(key=lambda x: (-x[0], x[1]))
    return [tools_latest[idx] for _s, idx in scored[:candidate_k]]


def _call_provider_text(
    *,
    provider: str,
    api_url: str,
    api_key: str,
    model: str,
    messages: List[Dict[str, str]],
    temperature: float,
    response_format: Optional[Dict[str, Any]] = None,
) -> str:
    if provider == "anthropic":
        return call_anthropic(
            api_url=api_url,
            api_key=api_key,
            model=model,
            messages=messages,
            temperature=temperature,
        ).content
    if provider == "gemini":
        return call_gemini(
            api_base=api_url,
            api_key=api_key,
            model=model,
            messages=messages,
            temperature=temperature,
        ).content
    if provider == "ollama":
        return call_ollama(
            api_url=api_url,
            model=model,
            messages=messages,
            temperature=temperature,
        ).content
    return call_openai_compatible(
        api_url=api_url,
        api_key=api_key,
        model=model,
        messages=messages,
        temperature=temperature,
        response_format=response_format,
    ).content


def _extract_json_object(text: str) -> dict:
    try:
        obj = json.loads(text)
        if isinstance(obj, dict):
            return obj
    except json.JSONDecodeError:
        pass
    match = re.search(r"\{.*\}", text, re.S)
    if match:
        obj = json.loads(match.group(0))
        if isinstance(obj, dict):
            return obj
    raise ValueError("Could not parse JSON object from LLM output")


def llm_extract_keywords(
    *,
    query: str,
    provider: str,
    api_url: str,
    api_key: str,
    model: str,
    temperature: float,
    top_n: int,
) -> List[str]:
    top_n = max(1, int(top_n))
    system = (
        "You are a search assistant for Galaxy tools. "
        "Extract short search keywords/phrases that would help retrieve the correct Galaxy tool."
    )
    user = (
        "User query:\n"
        f"{query}\n\n"
        f"Return a single JSON object only: {{\"keywords\": [\"...\", ...]}} with up to {top_n} items.\n"
        "- Use concise terms (1-4 words each).\n"
        "- Prefer task/algorithm/tool-family terms (e.g. 'long read mapping', 'busco', 'random forest').\n"
        "- Do not include tutorial names, dataset URLs, or parameter settings.\n"
    )
    messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
    content = _call_provider_text(
        provider=provider,
        api_url=api_url,
        api_key=api_key,
        model=model,
        messages=messages,
        temperature=temperature,
        response_format={"type": "json_object"} if provider == "openai_compatible" else None,
    )
    obj = _extract_json_object(content)
    kws = obj.get("keywords") or obj.get("terms") or []
    if not isinstance(kws, list):
        return []
    out: List[str] = []
    seen: set[str] = set()
    for kw in kws:
        if not isinstance(kw, str):
            continue
        kw = kw.strip()
        if not kw:
            continue
        if kw.lower() in seen:
            continue
        seen.add(kw.lower())
        out.append(kw)
        if len(out) >= top_n:
            break
    return out


def build_llm_messages(query: str, candidates: List[dict], top_k: int) -> List[dict[str, str]]:
    system_content = (
        "You are a Galaxy tool recommendation agent. "
        "Given a user query and a list of candidate Galaxy tools, return the best-matching tool IDs."
    )

    lines: List[str] = []
    for tool in candidates:
        tool_id = str(tool.get("tool_id") or "").strip()
        name = str(tool.get("name") or "").strip()
        desc = str(tool.get("description") or "").strip()
        if not tool_id:
            continue
        snippet = f"{tool_id} | {name}"
        if desc:
            snippet = f"{snippet} | {desc}"
        lines.append(snippet)

    user_content = (
        "User query:\n"
        f"{query}\n\n"
        "Candidate tools (tool_id | name | description):\n"
        + ("\n".join(lines) if lines else "N/A")
        + "\n\n"
        "Instructions:\n"
        f"- Pick up to {top_k} tool_id values from the candidate tools that best solve the query.\n"
        "- Output a single JSON object and nothing else: {\"predictions\": [\"tool_id\", ...]}.\n"
        "- Order predictions from most to least relevant.\n"
        "- If none match, return an empty list.\n"
    )

    return [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content},
    ]


def build_llm_minimal_messages(query: str, top_k: int) -> List[dict[str, str]]:
    system_content = (
        "You are a Galaxy tool recommendation assistant. "
        "Given a user query, return the best-matching Galaxy tool IDs."
    )

    user_content = (
        "User query:\n"
        f"{query}\n\n"
        "Instructions:\n"
        f"- Return up to {top_k} Galaxy tool IDs.\n"
        "- Prefer full tool IDs when possible (e.g. toolshed.g2.bx.psu.edu/repos/<owner>/<repo>/<tool>/<version>). "
        "If you are unsure about the version, you may omit the version segment.\n"
        "- Output a single JSON object and nothing else: {\"predictions\": [\"tool_id\", ...]}.\n"
        "- Order predictions from most to least relevant.\n"
        "- If you cannot identify a tool, return an empty list.\n"
    )

    return [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content},
    ]


_TOOL_ID_PATTERN = re.compile(
    r"(toolshed\.g2\.bx\.psu\.edu/repos/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/[A-Za-z0-9+_.-]+|upload1|__[^\\s\"']+|interactive_tool_[A-Za-z0-9_.-]+|CONVERTER_[A-Za-z0-9_.-]+|[A-Za-z0-9_.-]{2,}1)"
)


def safe_extract_predictions(
    content: str,
    *,
    top_k: int,
    candidates: Optional[List[str]] = None,
) -> Tuple[List[str], Optional[str]]:
    """
    Return (predictions, error_message). Never raises.
    """
    try:
        return extract_predictions(content, top_k), None
    except Exception as exc:  # noqa: BLE001
        cand_set = set(candidates or [])
        found: List[str] = []
        for match in _TOOL_ID_PATTERN.finditer(content):
            tid = match.group(0)
            if cand_set and tid not in cand_set:
                continue
            found.append(tid)
            if len(found) >= top_k:
                break
        return unique_in_order(found)[:top_k], f"{type(exc).__name__}: {exc}"


def generate_predictions(args: argparse.Namespace) -> None:
    output_predictions, _output_metrics = resolve_output_paths(args)
    gold_items = filter_gold_items(args, load_jsonl(args.gold))
    if not gold_items:
        raise ValueError(f"No items found in {args.gold}")

    if args.agent == "llm_minimal" and not args.no_write_candidates:
        LOGGER.warning("--agent llm_minimal ignores candidate retrieval; forcing --no-write-candidates.")
        args.no_write_candidates = True

    # Tool catalog fallback: if the default panel snapshot isn't present but an all-tools
    # snapshot exists, use it automatically.
    if not args.tool_catalog.exists():
        fallback = Path("data/tool_catalog/usegalaxy_org_all_tools.jsonl")
        if fallback.exists():
            LOGGER.warning(
                "Tool catalog %s not found; falling back to %s",
                args.tool_catalog,
                fallback,
            )
            args.tool_catalog = fallback

    tools: List[dict] = []
    tools_latest: List[dict] = []
    postings: Dict[str, List[int]] = {}
    idf: Dict[str, float] = {}
    need_catalog = args.agent in ("llm", "first_tutorial_tool") or (
        args.agent == "oracle" and (not args.no_write_candidates)
    )
    if need_catalog:
        try:
            tools = load_tool_catalog(args.tool_catalog)
            tools_latest = build_latest_tools(tools)
            if args.candidate_search == "token":
                postings, idf = build_inverted_index(tools)
        except FileNotFoundError:
            if args.agent == "oracle":
                LOGGER.warning(
                    "Tool catalog not available; continuing without writing candidates (set --no-write-candidates to silence)."
                )
                args.no_write_candidates = True
            else:
                raise
    do_resume = bool(args.resume or args.skip_existing)
    existing_ids = _load_existing_ids(output_predictions) if do_resume else set()

    api_key: Optional[str] = None
    if args.agent in ("llm", "llm_minimal") or (
        args.agent == "first_tutorial_tool" and args.candidate_strategy == "llm_keywords"
    ):
        api_key = _ensure_llm_key(args)
    elif args.agent == "standalone":
        if args.provider != "openai_compatible":
            raise ValueError("--agent standalone currently supports only --provider openai_compatible")
        api_key = _ensure_llm_key(args)

    standalone_agent = None
    if args.agent == "standalone":
        try:
            from pydantic_ai.models.openai import OpenAIChatModel  # type: ignore
            from pydantic_ai.providers.openai import OpenAIProvider  # type: ignore
            from pydantic_ai.usage import UsageLimits  # type: ignore

            from scripts.eval.tool_recommendation_agent_export.standalone.galaxy_tool_rec_agent import (  # type: ignore
                JsonlToolCatalog,
                ToolRecommendationAgentStandalone,
                WhooshToolCatalog,
            )
        except ModuleNotFoundError as exc:
            raise ModuleNotFoundError(
                "Missing standalone agent dependencies. Install them with:\n"
                "  .venv/bin/pip install -r scripts/eval/tool_recommendation_agent_export/standalone/requirements.txt"
            ) from exc

        base_url = args.api_url
        if base_url.endswith("/chat/completions"):
            base_url = base_url[: -len("/chat/completions")]
        provider = OpenAIProvider(base_url=base_url, api_key=api_key or None)
        model_obj = OpenAIChatModel(args.model, provider=provider)

        jsonl_catalog = JsonlToolCatalog.from_path(args.tool_catalog, max_tools=args.standalone_max_tools)
        if args.standalone_catalog == "whoosh":
            catalog = WhooshToolCatalog(
                jsonl_catalog.all_tools(),
                index_dir=args.standalone_index_dir,
                index_help=True,
            )
        else:
            catalog = jsonl_catalog

        req_limit = None if int(args.standalone_request_limit) <= 0 else int(args.standalone_request_limit)
        tool_limit = None if int(args.standalone_tool_calls_limit) <= 0 else int(args.standalone_tool_calls_limit)
        usage_limits = UsageLimits(request_limit=req_limit, tool_calls_limit=tool_limit)
        standalone_agent = ToolRecommendationAgentStandalone(
            model=model_obj, tool_catalog=catalog, usage_limits=usage_limits
        )

    processed = 0
    for entry in gold_items:
        qid = entry.get("id")
        if not isinstance(qid, str) or not qid:
            continue
        if do_resume and qid in existing_ids:
            continue
        if args.max_queries and processed >= args.max_queries:
            break

        query = str(entry.get("query") or "").strip()
        gold_tools = unique_in_order([t for t in (entry.get("tools") or []) if isinstance(t, str)])
        if args.agent == "oracle":
            predictions = [t for t in entry.get("tools") or [] if isinstance(t, str)]
            record = {"id": qid, "predictions": predictions}
            if not args.no_write_candidates:
                if args.candidate_search == "keyword":
                    candidates = select_candidates_by_keywords(
                        keywords=[query],
                        tools_latest=tools_latest,
                        candidate_k=max(0, args.candidate_k),
                    )
                else:
                    candidates = select_candidates(
                        query=query,
                        tools=tools,
                        postings=postings,
                        idf=idf,
                        candidate_k=max(0, args.candidate_k),
                        dedupe_by_base=args.dedupe_candidates_by_base,
                    )
                record["retrieved_tools"] = [str(t.get("tool_id")) for t in candidates if t.get("tool_id")]
                record["candidate_strategy"] = "token"
                record["candidate_search"] = args.candidate_search
                record["candidate_query"] = query
        elif args.agent == "first_tutorial_tool":
            candidate_query = query
            kws: List[str] = []
            if args.candidate_strategy == "llm_keywords":
                kws = llm_extract_keywords(
                    query=query,
                    provider=args.provider,
                    api_url=args.api_url,
                    api_key=api_key or "",
                    model=args.keyword_model or args.model,
                    temperature=0.0,
                    top_n=args.keyword_top_n,
                )
                if kws:
                    candidate_query = " ".join(kws)
            if args.candidate_search == "keyword":
                candidates = select_candidates_by_keywords(
                    keywords=kws or [candidate_query],
                    tools_latest=tools_latest,
                    candidate_k=max(0, args.candidate_k),
                )
            else:
                candidates = select_candidates(
                    query=candidate_query,
                    tools=tools,
                    postings=postings,
                    idf=idf,
                    candidate_k=max(0, args.candidate_k),
                    dedupe_by_base=args.dedupe_candidates_by_base,
                )
            predictions = [str(t.get("tool_id")) for t in candidates if t.get("tool_id")][: args.top_k]
            record = {"id": qid, "predictions": predictions}
            if not args.no_write_candidates:
                record["retrieved_tools"] = [str(t.get("tool_id")) for t in candidates if t.get("tool_id")]
                record["candidate_strategy"] = args.candidate_strategy
                record["candidate_search"] = args.candidate_search
                record["candidate_query"] = candidate_query
                if kws:
                    record["keywords"] = kws
        elif args.agent == "llm_minimal":
            messages = build_llm_minimal_messages(query=query, top_k=args.top_k)
            content = _call_provider_text(
                provider=args.provider,
                api_url=args.api_url,
                api_key=api_key or "",
                model=args.model,
                messages=messages,
                temperature=args.temperature,
                response_format={"type": "json_object"} if args.provider == "openai_compatible" else None,
            )
            predictions, parse_err = safe_extract_predictions(content, top_k=args.top_k, candidates=None)
            record = {"id": qid, "predictions": predictions}
            if parse_err:
                record["llm_parse_error"] = parse_err
                record["llm_raw_truncated"] = content[:2000]
        elif args.agent == "standalone":
            if standalone_agent is None:
                raise RuntimeError("Standalone agent was not initialized.")
            try:
                result = standalone_agent.recommend_sync(query)
            except Exception as exc:  # noqa: BLE001
                predictions = []
                record = {
                    "id": qid,
                    "predictions": predictions,
                    "standalone_error": f"{type(exc).__name__}: {exc}",
                }
                record["gold"] = gold_tools
                record["query"] = query
                _write_prediction_record(output_predictions, record)
                existing_ids.add(qid)
                processed += 1
                LOGGER.info("Wrote predictions for %s (%d) [standalone_error]", qid, processed)
                continue

            predictions = []
            record = {"id": qid}
            usage_obj = getattr(standalone_agent, "last_usage", lambda: None)()
            if usage_obj is not None:
                record["standalone_usage"] = {
                    "requests": getattr(usage_obj, "requests", None),
                    "tool_calls": getattr(usage_obj, "tool_calls", None),
                    "input_tokens": getattr(usage_obj, "input_tokens", None),
                    "output_tokens": getattr(usage_obj, "output_tokens", None),
                    "total_tokens": getattr(usage_obj, "total_tokens", None),
                }
            trace_obj = getattr(standalone_agent, "last_trace", lambda: None)()
            if trace_obj is not None:
                record["standalone_trace"] = trace_obj
            if hasattr(result, "primary_tools"):
                primary = getattr(result, "primary_tools", []) or []
                alt = getattr(result, "alternative_tools", []) or []
                for tool in list(primary) + list(alt):
                    if not isinstance(tool, dict):
                        continue
                    tid = tool.get("id") or tool.get("tool_id")
                    if isinstance(tid, str) and tid.strip():
                        predictions.append(tid.strip())
                record["standalone_confidence"] = getattr(result, "confidence", None)
                record["standalone_search_keywords"] = getattr(result, "search_keywords", None)
                record["standalone_reasoning"] = getattr(result, "reasoning", None)
            else:
                record["standalone_raw"] = str(result)
            record["predictions"] = unique_in_order(predictions)[: args.top_k]
        else:
            candidate_query = query
            kws = []
            if args.candidate_strategy == "llm_keywords":
                kws = llm_extract_keywords(
                    query=query,
                    provider=args.provider,
                    api_url=args.api_url,
                    api_key=api_key or "",
                    model=args.keyword_model or args.model,
                    temperature=0.0,
                    top_n=args.keyword_top_n,
                )
                if kws:
                    candidate_query = " ".join(kws)
            if args.candidate_search == "keyword":
                candidates = select_candidates_by_keywords(
                    keywords=kws or [candidate_query],
                    tools_latest=tools_latest,
                    candidate_k=max(0, args.candidate_k),
                )
            else:
                candidates = select_candidates(
                    query=candidate_query,
                    tools=tools,
                    postings=postings,
                    idf=idf,
                    candidate_k=max(0, args.candidate_k),
                    dedupe_by_base=args.dedupe_candidates_by_base,
                )
            messages = build_llm_messages(query=query, candidates=candidates, top_k=args.top_k)
            content = _call_provider_text(
                provider=args.provider,
                api_url=args.api_url,
                api_key=api_key or "",
                model=args.model,
                messages=messages,
                temperature=args.temperature,
                response_format={"type": "json_object"} if args.provider == "openai_compatible" else None,
            )
            candidate_ids = [str(t.get("tool_id")) for t in candidates if t.get("tool_id")]
            predictions, parse_err = safe_extract_predictions(
                content, top_k=args.top_k, candidates=candidate_ids
            )
            record = {"id": qid, "predictions": predictions}
            if not args.no_write_candidates:
                record["retrieved_tools"] = candidate_ids
                record["candidate_strategy"] = args.candidate_strategy
                record["candidate_search"] = args.candidate_search
                record["candidate_query"] = candidate_query
                if kws:
                    record["keywords"] = kws
            if parse_err:
                record["llm_parse_error"] = parse_err
                record["llm_raw_truncated"] = content[:2000]

        predictions = unique_in_order(predictions)[: args.top_k]
        record["predictions"] = predictions
        record["gold"] = gold_tools
        record["query"] = query
        _write_prediction_record(output_predictions, record)
        existing_ids.add(qid)
        processed += 1
        LOGGER.info("Wrote predictions for %s (%d)", qid, processed)
        time.sleep(max(0.0, args.delay if args.agent in ("llm", "llm_minimal") else 0.0))


def evaluate(args: argparse.Namespace) -> Dict[str, Any]:
    output_predictions, _output_metrics = resolve_output_paths(args)
    ks = [int(k.strip()) for k in args.k.split(",") if k.strip()]

    gold_items_raw = filter_gold_items(args, load_jsonl(args.gold))
    pred_items_raw = load_jsonl(output_predictions)
    pred_by_id = _collapse_predictions(pred_items_raw)

    gold_items: Dict[str, List[str]] = {}
    for item in gold_items_raw:
        qid = item.get("id")
        if not isinstance(qid, str) or not qid:
            continue
        tools = [t for t in (item.get("tools") or []) if isinstance(t, str)]
        gold_items[qid] = _normalize_list(tools, args.normalize_tools)

    pred_items: Dict[str, List[str]] = {}
    for qid, item in pred_by_id.items():
        preds = [p for p in (item.get("predictions") or []) if isinstance(p, str)]
        pred_items[qid] = _normalize_list(preds, args.normalize_tools)

    return compute_metrics(gold_items, pred_items, ks)


def write_markdown_report(
    path: Path,
    *,
    args: argparse.Namespace,
    results: Dict[str, Any],
    gold_items: List[dict],
    pred_items_raw: List[dict],
    argv: Optional[List[str]] = None,
) -> None:
    pred_by_id = _collapse_predictions(pred_items_raw)

    def _redact_argv(raw_argv: List[str]) -> List[str]:
        redacted: List[str] = []
        i = 0
        while i < len(raw_argv):
            a = raw_argv[i]
            if a == "--api-key":
                redacted.append(a)
                if i + 1 < len(raw_argv):
                    redacted.append("***")
                    i += 2
                    continue
            if a.startswith("--api-key="):
                redacted.append("--api-key=***")
                i += 1
                continue
            # Best-effort scrub any accidentally pasted OpenAI keys.
            if isinstance(a, str) and ("sk-" in a or "sk-proj-" in a):
                redacted.append(re.sub(r"sk-[A-Za-z0-9_-]+", "sk-***", a))
                i += 1
                continue
            redacted.append(a)
            i += 1
        return redacted

    lines: List[str] = []
    lines.append("# Evaluation report")
    lines.append("")

    lines.append("## Run configuration")
    lines.append("")
    if argv:
        safe_argv = _redact_argv(argv)
        lines.append("Command:")
        lines.append("")
        lines.append("```bash")
        lines.append(" ".join(safe_argv))
        lines.append("```")
        lines.append("")
    lines.append(f"- provider: `{getattr(args, 'provider', None)}`")
    lines.append(f"- model: `{getattr(args, 'model', None)}`")
    lines.append(f"- agent: `{getattr(args, 'agent', None)}`")
    lines.append(f"- gold: `{getattr(args, 'gold', None)}`")
    lines.append(f"- tool_catalog: `{getattr(args, 'tool_catalog', None)}`")
    lines.append(f"- api_url: `{getattr(args, 'api_url', None)}`")
    lines.append(f"- top_k: `{getattr(args, 'top_k', None)}`")
    lines.append(f"- k: `{getattr(args, 'k', None)}`")
    lines.append(f"- normalize_tools: `{bool(getattr(args, 'normalize_tools', False))}`")
    lines.append("")
    lines.append("Outputs:")
    lines.append(f"- predictions: `{getattr(args, 'output_predictions', None)}`")
    lines.append(f"- metrics: `{getattr(args, 'output_metrics', None)}`")
    lines.append(f"- report: `{path}`")
    lines.append("")

    lines.append("## Agent context")
    lines.append("")
    lines.append("This evaluation treats tool recommendation as a ranked retrieval task.")
    lines.append(f"Agent: `{args.agent}`")
    lines.append("")
    lines.append("For each benchmark item, the agent is given:")
    lines.append("- The **user query text** (natural language).")
    if args.agent == "llm":
        lines.append("- A **candidate tool shortlist** retrieved from the local tool catalog (`--tool-catalog`).")
        lines.append(
            "  - Each candidate is provided as `tool_id | name | description` plus (when present) input/output details."
        )
    elif args.agent == "standalone":
        lines.append("- Access to a **local tool catalog** via tool-calling (search/details/categories).")
    elif args.agent == "llm_minimal":
        lines.append("- No tool catalog or candidate list is provided.")
    lines.append("")
    lines.append("The agent is **not** given `tutorial_id`, `topic`, dataset metadata, or the gold tools.")
    lines.append("")
    if args.agent in ("llm", "first_tutorial_tool") or (args.agent == "oracle" and (not args.no_write_candidates)):
        lines.append("Candidate retrieval:")
        lines.append(f"- `candidate_strategy`: `{args.candidate_strategy}`")
        lines.append(f"- `candidate_search`: `{args.candidate_search}`")
        lines.append(f"- `candidate_k`: `{args.candidate_k}`")
        if args.candidate_strategy == "llm_keywords":
            lines.append(
                "- For each query, the LLM first returns search keywords, then candidates are retrieved using those keywords."
            )
        else:
            lines.append("- Candidates are retrieved using local token matching on the query text.")
        if args.candidate_search == "keyword":
            lines.append(
                "- Tool catalog search uses keyword/phrase matching over `tool_id`, `name`, and `description`, and keeps only the latest version per base tool ID."
            )
        else:
            lines.append("- Tool catalog search uses a local token inverted-index (may return multiple versions).")
    lines.append("")

    lines.append("## Metrics (how they are computed)")
    lines.append("")
    lines.append(
        "We compute standard top-k retrieval metrics with binary relevance (a tool is relevant if it appears in the gold list)."
    )
    lines.append("Predictions are de-duplicated in order before scoring.")
    lines.append("")
    lines.append("- **Hit@k**: 1 if any gold tool is in the top-k predictions, else 0.")
    lines.append(
        "- **MRR@k**: reciprocal rank of the first gold tool within the top-k (e.g., rank 2 → 1/2)."
    )
    lines.append(
        "- **nDCG@k**: discounted cumulative gain normalized by the ideal ranking (binary relevance)."
    )
    lines.append("")
    lines.append("Example (k=3):")
    lines.append("- Gold: `{A, B}`")
    lines.append("- Predictions: `[C, B, A, ...]`")
    lines.append("- Hit@3 = 1 (a gold tool appears in top 3)")
    lines.append("- MRR@3 = 1/2 (first relevant is at rank 2)")
    lines.append(
        "- nDCG@3 ≈ 0.693 (relevant at ranks 2 and 3, normalized by the ideal ranks 1 and 2)"
    )
    lines.append("")
    if getattr(args, "normalize_tools", False):
        lines.append(
            "Tool normalization: `--normalize-tools` drops the toolshed version segment when comparing tool IDs."
        )
        lines.append("")
    lines.append("## Metrics")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(results, ensure_ascii=False, indent=2))
    lines.append("```")
    lines.append("")
    lines.append("## Cases")
    lines.append("")

    for entry in gold_items:
        qid = entry.get("id")
        if not isinstance(qid, str) or not qid:
            continue
        query = str(entry.get("query") or "").strip()
        gold_tools = [t for t in (entry.get("tools") or []) if isinstance(t, str)]
        pred = pred_by_id.get(qid) or {}
        preds = [p for p in (pred.get("predictions") or []) if isinstance(p, str)]
        retrieved_tools = [
            c
            for c in (pred.get("retrieved_tools") or pred.get("candidates") or [])
            if isinstance(c, str)
        ]
        keywords = [k for k in (pred.get("keywords") or []) if isinstance(k, str)]

        lines.append(f"### {qid}")
        lines.append("")
        lines.append(query if query else "_(missing query)_")
        lines.append("")

        lines.append("**Ground truth**")
        if gold_tools:
            for t in gold_tools:
                lines.append(f"- `{t}`")
        else:
            lines.append("- _(none)_")
        lines.append("")

        lines.append("**Predictions**")
        if preds:
            for i, p in enumerate(preds, start=1):
                lines.append(f"- {i}. `{p}`")
        else:
            lines.append("- _(none)_")
        lines.append("")

        if keywords:
            lines.append("**Keywords**")
            for k in keywords:
                lines.append(f"- `{k}`")
            lines.append("")

        if retrieved_tools:
            lines.append(f"**Retrieved tool shortlist** (n={len(retrieved_tools)})")
            show = retrieved_tools[: min(30, len(retrieved_tools))]
            for c in show:
                lines.append(f"- `{c}`")
            if len(retrieved_tools) > len(show):
                lines.append(f"- _(… {len(retrieved_tools) - len(show)} more)_")
            lines.append("")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    output_predictions, output_metrics = resolve_output_paths(args)
    args.output_predictions = output_predictions
    args.output_metrics = output_metrics
    if not args.report_only:
        generate_predictions(args)
    results = evaluate(args)

    output_metrics.parent.mkdir(parents=True, exist_ok=True)
    output_metrics.write_text(
        json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    if not args.no_markdown:
        gold_items = filter_gold_items(args, load_jsonl(args.gold))
        pred_items_raw = load_jsonl(output_predictions)
        output_md = resolve_markdown_path(args)
        write_markdown_report(
            output_md,
            args=args,
            results=results,
            gold_items=gold_items,
            pred_items_raw=pred_items_raw,
            argv=sys.argv[:],
        )
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
