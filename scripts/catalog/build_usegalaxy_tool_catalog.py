from __future__ import annotations

import argparse
import json
import logging
import os
import ssl
import subprocess
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

logging.basicConfig(level=logging.INFO, format="%(message)s")
LOGGER = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch a Galaxy server tool list and write an agent-friendly JSONL snapshot "
            "(plus optional indices)."
        )
    )
    parser.add_argument(
        "--server",
        type=str,
        default="https://usegalaxy.org",
        help="Galaxy server base URL (default: https://usegalaxy.org).",
    )
    parser.add_argument(
        "--use-bioblend",
        action="store_true",
        help=(
            "Use BioBlend (bioblend.galaxy) instead of raw HTTP calls. "
            "This is optional and requires installing 'bioblend'."
        ),
    )
    parser.add_argument(
        "--galaxy-api-key",
        type=str,
        default=None,
        help="Optional Galaxy API key (fallbacks to GALAXY_API_KEY env var).",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--in-panel",
        action="store_true",
        help="Fetch only tools shown in the tool panel (smaller candidate set).",
    )
    group.add_argument(
        "--no-in-panel",
        action="store_true",
        help="Fetch all installed tools including non-panel/hidden tools (larger universe).",
    )
    parser.add_argument(
        "--out-jsonl",
        type=Path,
        default=None,
        help="Output JSONL path (one tool per line).",
    )
    parser.add_argument(
        "--out-index",
        type=Path,
        default=None,
        help="Output index JSON path: base_id -> [tool_id,...].",
    )
    parser.add_argument(
        "--out-by-section",
        type=Path,
        default=None,
        help="Output JSON path with 'by_section' mapping: section_name -> [tool_id,...].",
    )
    parser.add_argument(
        "--include-io-details",
        action="store_true",
        help=(
            "Also fetch per-tool input/output metadata via /api/tools/<tool_id> "
            "(slower; many HTTP requests)."
        ),
    )
    parser.add_argument(
        "--flush-every",
        type=int,
        default=50,
        help="When --include-io-details is set, flush output to disk every N tools (default: 50).",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help=(
            "When --include-io-details is set and the output JSONL exists, skip tool_ids already present "
            "and append the remaining tools."
        ),
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=120,
        help="HTTP timeout seconds (default: 120).",
    )
    return parser.parse_args()


def normalize_base_id(tool_id: str) -> str:
    if tool_id.startswith("toolshed.g2.bx.psu.edu/"):
        parts = tool_id.split("/")
        if len(parts) >= 2:
            return "/".join(parts[:-1])
    return tool_id


def _http_get_json(url: str, timeout: int) -> Any:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "galaxy-tool-recommendation-agent-benchmark/0.1",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read().decode("utf-8")
        return json.loads(data)
    except (ssl.SSLError, urllib.error.URLError):
        # Some older Python/OpenSSL builds can fail TLS negotiation with modern servers.
        # Fall back to curl (commonly available) to keep the script usable.
        return _curl_get_json(url, timeout=timeout)


def _curl_get_json(url: str, timeout: int) -> Any:
    cmd = [
        "curl",
        "-fsSL",
        "--max-time",
        str(timeout),
        "-H",
        "Accept: application/json",
        "-A",
        "galaxy-tool-recommendation-agent-benchmark/0.1",
        url,
    ]
    out = subprocess.check_output(cmd)
    return json.loads(out.decode("utf-8"))


def _load_env_if_available() -> None:
    try:
        from dotenv import load_dotenv  # type: ignore
    except ModuleNotFoundError:
        return
    load_dotenv(dotenv_path=Path(".env"))


def _get_galaxy_api_key(args: argparse.Namespace) -> Optional[str]:
    _load_env_if_available()
    return args.galaxy_api_key or os.environ.get("GALAXY_API_KEY")


def fetch_tools(server: str, in_panel: bool, timeout: int) -> List[dict]:
    server = server.rstrip("/")
    query = urllib.parse.urlencode({"in_panel": "true" if in_panel else "false"})
    url = f"{server}/api/tools?{query}"
    payload = _http_get_json(url, timeout=timeout)
    if not isinstance(payload, list):
        raise ValueError(f"Unexpected /api/tools response type: {type(payload)}")

    def walk(obj: Any) -> Iterable[dict]:
        if isinstance(obj, dict):
            if obj.get("model_class") == "Tool":
                yield obj
            elems = obj.get("elems")
            if isinstance(elems, list):
                for e in elems:
                    yield from walk(e)
        elif isinstance(obj, list):
            for e in obj:
                yield from walk(e)

    tool_items = list(walk(payload)) if in_panel else [i for i in payload if isinstance(i, dict) and i.get("model_class") == "Tool"]

    tools: List[dict] = []
    for item in tool_items:
        tool_id = item.get("id") or item.get("tool_id")
        if not isinstance(tool_id, str) or not tool_id:
            continue
        tools.append(
            {
                "tool_id": tool_id,
                "name": item.get("name") or "",
                "version": item.get("version") or "",
                "description": item.get("description") or "",
                "base_id": normalize_base_id(tool_id),
                "panel_section_id": item.get("panel_section_id") or "",
                "panel_section_name": item.get("panel_section_name") or "",
            }
        )
    return tools


def fetch_tools_bioblend(
    server: str,
    in_panel: bool,
    api_key: Optional[str],
    timeout: int,
    include_io_details: bool,
) -> List[dict]:
    try:
        from bioblend.galaxy import GalaxyInstance  # type: ignore
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            "BioBlend is not installed. Install it in your environment: `pip install bioblend`."
        ) from exc

    gi = GalaxyInstance(url=server.rstrip("/"), key=api_key)
    # BioBlend uses requests; timeout isn't consistently plumbed through for every call,
    # but we keep the arg for API symmetry.
    try:
        tools_raw = gi.tools.get_tools(in_panel=in_panel)  # type: ignore[call-arg]
    except TypeError:
        # Older BioBlend versions don't support the `in_panel` kwarg.
        tools_raw = gi.tools.get_tools()
        if in_panel:
            panel_ids = _get_panel_tool_ids_bioblend(gi)
            if panel_ids:
                tools_raw = [
                    t
                    for t in tools_raw
                    if isinstance(t, dict) and isinstance((t.get("id") or t.get("tool_id")), str)
                    and (t.get("id") or t.get("tool_id")) in panel_ids
                ]
    tools: List[dict] = []
    for item in tools_raw:
        if not isinstance(item, dict):
            continue
        tool_id = item.get("id") or item.get("tool_id")
        if not isinstance(tool_id, str) or not tool_id:
            continue
        record = {
            "tool_id": tool_id,
            "name": item.get("name") or "",
            "version": item.get("version") or "",
            "description": item.get("description") or "",
            "base_id": normalize_base_id(tool_id),
            # Panel section metadata is not consistently exposed by BioBlend across versions.
            # We populate these later via /api/tool_panels/default when available.
            "panel_section_id": item.get("panel_section_id") or "",
            "panel_section_name": item.get("panel_section_name") or "",
        }
        tools.append(record)

    if include_io_details:
        LOGGER.info("Fetching per-tool io details for %d tools (BioBlend)...", len(tools))
        for idx, tool in enumerate(tools, start=1):
            tool_id = tool.get("tool_id")
            if not isinstance(tool_id, str) or not tool_id:
                continue
            try:
                try:
                    details = gi.tools.show_tool(tool_id, io_details=True)  # type: ignore[arg-type]
                except TypeError:
                    details = gi.tools.show_tool(tool_id)
                if isinstance(details, dict):
                    tool["inputs_raw"] = details.get("inputs")
                    tool["outputs_raw"] = details.get("outputs")
                    tool["input_params_flat"] = _flatten_inputs(details.get("inputs"))
            except Exception as exc:
                tool["io_details_error"] = str(exc)
            if idx % 250 == 0:
                LOGGER.info("...%d/%d", idx, len(tools))

    return tools


def _get_panel_tool_ids_bioblend(gi: Any) -> set[str]:
    """
    Best-effort extraction of tool IDs shown in the Galaxy tool panel via BioBlend.
    This exists for compatibility with older BioBlend versions that can't pass
    `in_panel=true` to /api/tools.
    """
    tool_ids: set[str] = set()

    if not hasattr(gi, "tools"):
        return tool_ids

    tools_client = gi.tools
    panel_payload: Any = None
    if hasattr(tools_client, "get_tool_panel"):
        try:
            panel_payload = tools_client.get_tool_panel()  # type: ignore[call-arg]
        except Exception:
            panel_payload = None

    if panel_payload is None:
        # Fallback to raw API call if BioBlend doesn't expose panel helpers.
        try:
            url = f"{str(getattr(gi, 'url', '')).rstrip('/')}/api/tool_panels/default"
            panel_payload = _http_get_json(url, timeout=120)
        except Exception:
            panel_payload = None

    def walk(obj: Any) -> None:
        if isinstance(obj, dict):
            # Common shape from /api/tool_panels/default: section dicts have `tools: [id,...]`
            tools = obj.get("tools")
            if isinstance(tools, list):
                for t in tools:
                    if isinstance(t, str) and t:
                        tool_ids.add(t)
            for v in obj.values():
                walk(v)
        elif isinstance(obj, list):
            for v in obj:
                walk(v)
        elif isinstance(obj, str):
            # Avoid collecting obvious non-tool strings; keep it conservative.
            if obj and " " not in obj and len(obj) < 300:
                tool_ids.add(obj)

    if panel_payload is not None:
        walk(panel_payload)

    return tool_ids


def fetch_by_section(server: str, timeout: int) -> dict:
    server = server.rstrip("/")
    url = f"{server}/api/tool_panels/default"
    payload = _http_get_json(url, timeout=timeout)
    if not isinstance(payload, dict):
        raise ValueError(f"Unexpected /api/tool_panels/default response type: {type(payload)}")

    by_section: Dict[str, List[str]] = {}
    for _section_id, section in payload.items():
        if not isinstance(section, dict):
            continue
        name = section.get("name")
        tools = section.get("tools")
        if not isinstance(name, str) or not name:
            continue
        if not isinstance(tools, list):
            continue
        tool_ids: List[str] = [t for t in tools if isinstance(t, str) and t]
        if tool_ids:
            by_section[name] = tool_ids

    return {
        "server": server,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "by_section": by_section,
    }


def _annotate_tools_with_sections(tools: List[dict], by_section_payload: Optional[dict]) -> None:
    """
    Best-effort: attach panel section name to each tool record.

    This helps align local catalogs with Galaxy's toolbox search, which indexes the tool-panel section name.
    """
    if not by_section_payload or not isinstance(by_section_payload, dict):
        return
    by_section = by_section_payload.get("by_section")
    if not isinstance(by_section, dict):
        return

    tool_to_section: Dict[str, str] = {}
    for section_name, tool_ids in by_section.items():
        if not isinstance(section_name, str) or not section_name:
            continue
        if not isinstance(tool_ids, list):
            continue
        for tid in tool_ids:
            if isinstance(tid, str) and tid and tid not in tool_to_section:
                tool_to_section[tid] = section_name

    for tool in tools:
        if not isinstance(tool, dict):
            continue
        tid = tool.get("tool_id")
        if not isinstance(tid, str) or not tid:
            continue
        if not tool.get("panel_section_name"):
            tool["panel_section_name"] = tool_to_section.get(tid, "") or ""
        # Convenience aliases used by some agents/search implementations.
        tool.setdefault("section", tool.get("panel_section_name") or "")
        tool.setdefault("category", tool.get("panel_section_name") or "")


def _ensure_panel_tools_present(
    tools: List[dict],
    by_section_payload: Optional[dict],
    *,
    server: str,
    timeout: int,
    include_io_details: bool,
) -> None:
    """
    Ensure that every tool listed in /api/tool_panels/default is present in the JSONL snapshot.

    Some Galaxy servers may omit panel tools (notably interactive tools) from /api/tools?in_panel=true,
    while still showing them in the tool panel. For agent benchmarking, we want the catalog "universe"
    to match what the default panel view can actually surface.
    """
    if not by_section_payload or not isinstance(by_section_payload, dict):
        return
    by_section = by_section_payload.get("by_section")
    if not isinstance(by_section, dict):
        return

    panel_tool_ids: set[str] = set()
    tool_to_section: Dict[str, str] = {}
    for section_name, tool_ids in by_section.items():
        if not isinstance(section_name, str) or not section_name:
            continue
        if not isinstance(tool_ids, list):
            continue
        for tid in tool_ids:
            if not isinstance(tid, str) or not tid:
                continue
            panel_tool_ids.add(tid)
            tool_to_section.setdefault(tid, section_name)

    existing = {t.get("tool_id") for t in tools if isinstance(t, dict) and isinstance(t.get("tool_id"), str)}
    missing = sorted(tid for tid in panel_tool_ids if tid not in existing)
    if not missing:
        return

    LOGGER.warning("Panel contains %d tool(s) missing from /api/tools listing; adding them.", len(missing))
    for tid in missing:
        record: dict = {
            "tool_id": tid,
            "name": "",
            "version": "",
            "description": "",
            "base_id": normalize_base_id(tid),
            "panel_section_id": "",
            "panel_section_name": tool_to_section.get(tid, "") or "",
        }
        # Keep aliases consistent with other entries.
        record["section"] = record["panel_section_name"]
        record["category"] = record["panel_section_name"]
        if include_io_details:
            try:
                record.update(fetch_tool_io_details(server, tid, timeout=timeout))
            except Exception as exc:
                record["io_details_error"] = str(exc)
        tools.append(record)


def _flatten_inputs(inputs: Any) -> List[dict]:
    """
    Best-effort flattening of Galaxy tool input specs.
    This is intentionally conservative: it stores a compact, schema-agnostic summary.
    """
    out: List[dict] = []
    if not isinstance(inputs, list):
        return out
    for inp in inputs:
        if not isinstance(inp, dict):
            continue
        summary: dict = {}
        for key in ("name", "label", "type", "optional", "help"):
            if key in inp:
                summary[key] = inp.get(key)
        if summary:
            out.append(summary)
    return out


def fetch_tool_io_details(server: str, tool_id: str, timeout: int) -> dict:
    server = server.rstrip("/")
    url = f"{server}/api/tools/{urllib.parse.quote(tool_id, safe='')}"
    # Some Galaxy servers accept io_details=true; harmless if ignored.
    url = f"{url}?{urllib.parse.urlencode({'io_details': 'true'})}"
    payload = _http_get_json(url, timeout=timeout)
    if not isinstance(payload, dict):
        return {}
    inputs = payload.get("inputs")
    outputs = payload.get("outputs")
    return {
        # Some servers return descriptive metadata here; include it if present so the catalog
        # remains informative even for panel tools missing from /api/tools.
        "name": payload.get("name") or "",
        "version": payload.get("version") or "",
        "description": payload.get("description") or "",
        "inputs_raw": inputs,
        "outputs_raw": outputs,
        "input_params_flat": _flatten_inputs(inputs),
    }


def write_jsonl(path: Path, tools: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for tool in tools:
            handle.write(json.dumps(tool, ensure_ascii=False) + "\n")


def build_index(tools: Iterable[dict]) -> Dict[str, List[str]]:
    out: Dict[str, List[str]] = defaultdict(list)
    for tool in tools:
        tool_id = tool.get("tool_id")
        base_id = tool.get("base_id")
        if not isinstance(tool_id, str) or not tool_id:
            continue
        if not isinstance(base_id, str) or not base_id:
            base_id = normalize_base_id(tool_id)
        out[base_id].append(tool_id)
    # deterministic ordering
    return {k: sorted(v) for k, v in sorted(out.items(), key=lambda kv: kv[0])}

def _load_existing_tool_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    tool_ids: set[str] = set()
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(obj, dict) and isinstance(obj.get("tool_id"), str):
                tool_ids.add(obj["tool_id"])
    return tool_ids


def main() -> None:
    args = parse_args()
    in_panel = True if args.in_panel or not args.no_in_panel else False
    out_jsonl = args.out_jsonl
    out_index = args.out_index
    out_by_section = args.out_by_section
    if out_jsonl is None:
        out_jsonl = (
            Path("data/tool_catalog/usegalaxy_org_tools.jsonl")
            if in_panel
            else Path("data/tool_catalog/usegalaxy_org_all_tools.jsonl")
        )
    if out_index is None:
        out_index = (
            Path("data/tool_catalog/usegalaxy_org_index.json")
            if in_panel
            else Path("data/tool_catalog/usegalaxy_org_all_index.json")
        )
    if out_by_section is None:
        out_by_section = (
            Path("data/tool_catalog/usegalaxy_org_by_section.json")
            if in_panel
            else Path("data/tool_catalog/usegalaxy_org_all_by_section.json")
        )
    api_key = _get_galaxy_api_key(args)
    tools: List[dict]
    if args.use_bioblend:
        tools = fetch_tools_bioblend(
            args.server,
            in_panel=in_panel,
            api_key=api_key,
            timeout=args.timeout,
            include_io_details=args.include_io_details,
        )
    else:
        tools = fetch_tools(args.server, in_panel=in_panel, timeout=args.timeout)

    # Fetch panel section mapping early so we can attach section metadata to JSONL output.
    by_section_payload: Optional[dict] = None
    try:
        by_section_payload = fetch_by_section(args.server, timeout=args.timeout)
    except Exception as exc:
        LOGGER.warning("Failed to fetch by-section mapping: %s", exc)

    # Some panel tools may be absent from /api/tools output; ensure panel view completeness.
    _ensure_panel_tools_present(
        tools,
        by_section_payload,
        server=args.server,
        timeout=args.timeout,
        include_io_details=bool(args.include_io_details),
    )

    _annotate_tools_with_sections(tools, by_section_payload)

    if args.include_io_details:
        existing = _load_existing_tool_ids(out_jsonl) if args.resume else set()
        if existing:
            LOGGER.info("Resuming: %d tool(s) already present in %s", len(existing), out_jsonl)

        flush_every = max(1, int(args.flush_every))
        mode = "a" if (args.resume and out_jsonl.exists()) else "w"
        out_jsonl.parent.mkdir(parents=True, exist_ok=True)
        written = 0
        processed = 0

        with out_jsonl.open(mode, encoding="utf-8") as out_handle:
            if not args.use_bioblend:
                LOGGER.info("Fetching per-tool io details for %d tools...", len(tools))
                for tool in tools:
                    tool_id = tool.get("tool_id")
                    if not isinstance(tool_id, str) or not tool_id:
                        continue
                    processed += 1
                    if tool_id in existing:
                        continue
                    try:
                        tool.update(fetch_tool_io_details(args.server, tool_id, timeout=args.timeout))
                    except Exception as exc:
                        tool["io_details_error"] = str(exc)
                    out_handle.write(json.dumps(tool, ensure_ascii=False) + "\n")
                    written += 1
                    if written % flush_every == 0:
                        out_handle.flush()
                        LOGGER.info("Flushed %d tools to %s", written, out_jsonl)
                    if written % 250 == 0:
                        LOGGER.info("...%d processed, %d written", processed, written)
            else:
                # BioBlend path already populated IO details if requested.
                for tool in tools:
                    tool_id = tool.get("tool_id")
                    if not isinstance(tool_id, str) or not tool_id:
                        continue
                    processed += 1
                    if tool_id in existing:
                        continue
                    out_handle.write(json.dumps(tool, ensure_ascii=False) + "\n")
                    written += 1
                    if written % flush_every == 0:
                        out_handle.flush()
                        LOGGER.info("Flushed %d tools to %s", written, out_jsonl)
            out_handle.flush()
    else:
        write_jsonl(out_jsonl, tools)
    index = build_index(tools)
    out_index.parent.mkdir(parents=True, exist_ok=True)
    out_index.write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    if by_section_payload is not None:
        out_by_section.parent.mkdir(parents=True, exist_ok=True)
        out_by_section.write_text(
            json.dumps(by_section_payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
