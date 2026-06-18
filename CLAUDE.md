# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup

This project uses `uv` for dependency management (Python >=3.12 required).

```bash
uv sync                  # install dependencies
uv run jupyter notebook  # launch notebooks
```

Alternatively with pip:
```bash
pip install -r requirements.txt
jupyter notebook
```

## Environment Variables

All notebooks load credentials via `python-dotenv`. Create a `.env` file in the project root with:

```
OPENAI_API_KEY=...
GOOGLE_API_KEY=...
GROQ_API_KEY=...
```

Notebooks call `load_dotenv()` then assign `os.environ[KEY] = os.getenv(KEY)` — if a key is missing from `.env`, `os.getenv()` returns `None` and the assignment raises `TypeError: str expected, not NoneType`.

## Architecture

The repo is a progressive learning series split into two tracks:

### `ai-agents/` — LangChain concepts (notebooks 1–5)
| Notebook | Topic |
|---|---|
| `1-langchain-intro` | `create_agent` with tools, basic agent invocation |
| `2-model-integration` | `init_chat_model` with OpenAI / Gemini / Groq; streaming and batch |
| `3-tools` | `@tool` decorator, `bind_tools`, message types (System/Human/AI/Tool) |
| `4-structuredoutput` | `with_structured_output` using Pydantic, TypedDict, and dataclass schemas |
| `5-middleware` | `SummarizationMiddleware` (message/token/fraction triggers) and `HumanInTheLoopMiddleware` with approve/edit/reject |

### `langgraph/` — LangGraph Graph API
| Notebook | Topic |
|---|---|
| `1-basic-chatbot` | `StateGraph` with typed state, nodes, edges, `graph.compile()`, streaming |

### Key patterns used across notebooks
- **Model init**: `init_chat_model("provider:model-name")` is the standard — e.g. `"groq:qwen/qwen3-32b"`, `"google_genai:gemini-2.5-flash-lite"`
- **Agents**: `create_agent(model=..., tools=[...], checkpointer=..., middleware=[...])` from `langchain.agents`
- **LangGraph state**: `TypedDict` with `Annotated[list, add_messages]` for message accumulation
- **Checkpointing**: `InMemorySaver` (from `langgraph.checkpoint.memory`) used for multi-turn agent memory; config passed as `{"configurable": {"thread_id": "..."}}`
