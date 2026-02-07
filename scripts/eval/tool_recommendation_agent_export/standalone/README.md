This is a minimal, standalone extraction of Galaxy's tool recommendation agent. It is designed to be easy to call from a benchmark harness by injecting a tool catalog.

Contents:
- `galaxy_tool_rec_agent/agent.py`: Standalone agent (based on `pydantic-ai`). Exposes three tools to the LLM:
  - `search_galaxy_tools`
  - `get_galaxy_tool_details`
  - `get_galaxy_tool_categories`
  The system prompt is kept identical to Galaxy's `tool_recommendation.md`.
  - `JsonlToolCatalog`: Loads the benchmark JSONL catalog (fields are normalized to `id/name/description/help`).
  - `WhooshToolCatalog`: Uses Whoosh to mirror Galaxy's `trans.app.toolbox_search` as closely as possible (field schema, boosts, n-grams, BM25F help-text scoring). This is the closest option to `original/`, but requires installing `whoosh`.
- `galaxy_tool_rec_agent/prompts/tool_recommendation.md`: System prompt copied from Galaxy.

Install dependencies (example):
```bash
pip install -r requirements.txt
```

Minimal usage (example):
```python
import asyncio
from pydantic_ai.models.openai import OpenAIChatModel

from galaxy_tool_rec_agent import JsonlToolCatalog, ToolRecommendationAgentStandalone

catalog = JsonlToolCatalog.from_path(
    "/path/to/usegalaxy_org_all_tools_with_helptext.jsonl"
)
model = OpenAIChatModel("gpt-4o-mini")  # configure provider env vars (e.g. OPENAI_API_KEY)
agent = ToolRecommendationAgentStandalone(model=model, tool_catalog=catalog)

result = asyncio.run(agent.recommend("I want to align paired-end FASTQ to hg38"))
print(result)
```

More exact search (recommended to match Galaxy search semantics):
```python
import asyncio
from pydantic_ai.models.openai import OpenAIChatModel

from galaxy_tool_rec_agent import JsonlToolCatalog, WhooshToolCatalog, ToolRecommendationAgentStandalone

jsonl = "/path/to/usegalaxy_org_all_tools_with_helptext.jsonl"
tools = JsonlToolCatalog.from_path(jsonl).all_tools()
catalog = WhooshToolCatalog(tools, index_dir=".tool_search_index", index_help=True)

model = OpenAIChatModel("gpt-4o-mini")
agent = ToolRecommendationAgentStandalone(model=model, tool_catalog=catalog)
print(asyncio.run(agent.recommend("align reads to hg38")))
```
