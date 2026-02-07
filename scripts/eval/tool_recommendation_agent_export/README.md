This folder contains an extracted copy of Galaxy's **tool recommendation agent** (LLM-based) code and prompts, packaged so it can be copied into the `galaxy-tool-recommendation-agent-benchmark` repository for evaluation.

Source:
- Repository: `galaxyproject/galaxy` (local workspace)
- Extracted from Git commit: `272b8d1c5c9dc74faf85de4129e418bebbe4a16a`

Layout:
- `original/`: A direct copy of the relevant Galaxy source files and prompts (kept as close to upstream as possible for traceability).
- `standalone/`: A minimal wrapper that is easier to run outside Galaxy (reuses the same `tool_recommendation.md` prompt and exposes an injectable tool-catalog search interface).
  - For the closest possible match to Galaxy's `trans.app.toolbox_search`, use `WhooshToolCatalog` (requires installing `whoosh`). It mirrors Galaxy's multi-field indexing, boosts, n-gram search, and BM25F help-text scoring as closely as possible.

To use this in the benchmark repo, typically you can copy the entire `tool_recommendation_agent_export/` directory.
