<div align="center">

# 🤖 AI Agents & LLM Engineering Cookbook

**A comprehensive, hands-on collection of notebooks and code for building production-ready AI agents, RAG pipelines, LLM gateways, and multi-provider integrations.**

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-latest-green.svg)](https://github.com/langchain-ai/langchain)
[![LangGraph](https://img.shields.io/badge/LangGraph-latest-purple.svg)](https://github.com/langchain-ai/langgraph)
[![LiteLLM](https://img.shields.io/badge/LiteLLM-Gateway-orange.svg)](https://github.com/BerriAI/litellm)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Getting Started](#-getting-started) •
[Modules](#-modules) •
[Architecture](#-architecture) •
[Contributing](#-contributing)

</div>

---

## 📖 Overview

This repository is a **learning-first, production-aware** resource for engineers building with Large Language Models. Each module is a self-contained Jupyter notebook or Python script that demonstrates a specific concept — from basic LangChain usage to advanced multi-agent orchestration with human-in-the-loop workflows.

### Who is this for?

- **ML/AI Engineers** looking to build robust LLM-powered applications
- **Backend Engineers** integrating LLMs into production systems
- **Students & Researchers** learning agent architectures hands-on
- **Teams** evaluating LLM frameworks and gateway patterns

---

## ✨ Features

| Category | What You'll Learn |
|----------|------------------|
| **AI Agents** | Tool binding, structured outputs, middleware, guardrails |
| **Deep Agents** | Multi-step planning, subagents, autonomous task execution |
| **LangGraph** | Stateful workflows, human-in-the-loop, conditional routing |
| **RAG** | Document ingestion, vector stores, semantic search, evaluation |
| **MCP** | Model Context Protocol servers & clients |
| **LLM Gateway** | Unified multi-provider access, fallbacks, caching, cost control |

---

## 📁 Project Structure

```
.
├── ai-agents/                  # Core LangChain agent patterns
│   ├── 1-langchain-intro.ipynb       # Agent creation & tool binding basics
│   ├── 2-model-integration.ipynb     # Multi-provider (OpenAI, Gemini, Groq)
│   ├── 3-tools.ipynb                 # Tool schemas & function calling
│   ├── 4-structuredoutput.ipynb      # Pydantic structured outputs
│   ├── 5-middleware.ipynb            # Conversation summarization & token mgmt
│   └── 6-guardrails.ipynb            # Input/output safety & PII detection
│
├── deep-agents/                # Advanced autonomous agents
│   └── 1-basicdeep-agent.ipynb       # Multi-step planning with subagents
│
├── langgraph/                  # Stateful agent orchestration
│   ├── 1-basic-chatbot.ipynb         # Stateful conversational agent
│   └── 2-human-in-the-loop.ipynb     # Human approval workflows
│
├── RAG/                        # Retrieval-Augmented Generation
│   ├── notebook/
│   │   ├── document-data-ingestion.ipynb
│   │   └── pdf-loader.ipynb
│   ├── pdf/                          # Sample PDF documents
│   └── text_files/                   # Sample text documents
│
├── rag-evals/                  # RAG evaluation & benchmarking
│   └── rag-eval.ipynb                # LangSmith-based evaluation
│
├── llm-gateway/                # LLM Gateway patterns
│   └── llm-gateway.ipynb             # LiteLLM unified API, routing, fallbacks
│
├── mcp/                        # Model Context Protocol
│   ├── mcp-clientserver.py           # MCP client with agent integration
│   ├── mcp-mathserver.py            # MCP math tool server
│   └── mcp-weather.py              # MCP weather tool server
│
├── src/                        # Reusable RAG pipeline library
│   ├── data_loader.py               # Multi-format document loader
│   ├── embedding.py                 # Chunking & embedding pipeline
│   ├── vectorstore.py              # FAISS vector store wrapper
│   └── search.py                   # RAG search & summarization
│
├── app.py                      # RAG application entry point
├── pyproject.toml              # Project dependencies (uv/pip)
└── requirements.txt            # Pip requirements
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- API keys for at least one LLM provider (OpenAI, Google, Groq, etc.)

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/ai-agents-cookbook.git
cd ai-agents-cookbook

# Option 1: Using uv (recommended)
uv sync

# Option 2: Using pip
pip install -r requirements.txt
```

### Environment Setup

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_key
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
LANGSMITH_API_KEY=your_langsmith_key  # Optional: for tracing
```

### Run Your First Notebook

```bash
# Launch Jupyter
jupyter notebook

# Or open in VS Code and run cells directly
code ai-agents/1-langchain-intro.ipynb
```

---

## 📚 Modules

### 1. AI Agents (`ai-agents/`)

Progressive introduction to building AI agents with LangChain:

| # | Notebook | Key Concepts |
|---|----------|--------------|
| 1 | `langchain-intro` | Agent creation, tool binding fundamentals |
| 2 | `model-integration` | OpenAI, Gemini, Groq — streaming & batch |
| 3 | `tools` | Function schemas, argument definitions |
| 4 | `structuredoutput` | Pydantic models, nested schema validation |
| 5 | `middleware` | Token management, conversation summarization |
| 6 | `guardrails` | Safety filters, PII detection, input/output validation |

### 2. Deep Agents (`deep-agents/`)

Autonomous agents that decompose complex tasks into subtasks with planning, web search, and file system access.

### 3. LangGraph (`langgraph/`)

Stateful, graph-based agent orchestration:
- **Basic Chatbot** — Message state management and persistence
- **Human-in-the-Loop** — Interrupt execution for human approval before critical actions

### 4. RAG Pipeline (`RAG/` + `src/`)

End-to-end Retrieval-Augmented Generation:
- Multi-format document loading (PDF, TXT, CSV, Excel, Word, JSON)
- Recursive text chunking with configurable overlap
- FAISS vector store with sentence-transformers embeddings
- Search + LLM summarization pipeline

### 5. RAG Evaluation (`rag-evals/`)

Measure RAG quality with LangSmith: create test datasets, run evaluations, and track performance metrics.

### 6. LLM Gateway (`llm-gateway/`)

Use LiteLLM as a unified gateway to 100+ LLM providers:
- Single API for OpenAI, Anthropic, Google, Groq, and more
- Automatic fallbacks when providers fail
- Response caching, rate limiting, cost tracking

### 7. MCP — Model Context Protocol (`mcp/`)

Build and connect MCP tool servers:
- **Math Server** — Arithmetic tools exposed via MCP
- **Weather Server** — Location-based weather tool
- **Client** — Agent that discovers and uses MCP tools dynamically

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Your Application                       │
├──────────┬──────────┬──────────┬──────────┬─────────────┤
│  Agents  │ LangGraph│   RAG    │   MCP    │  Gateway    │
├──────────┴──────────┴──────────┴──────────┴─────────────┤
│                  LangChain / LiteLLM                      │
├──────────┬──────────┬──────────┬──────────┬─────────────┤
│  OpenAI  │  Gemini  │   Groq   │  Claude  │   Local     │
└──────────┴──────────┴──────────┴──────────┴─────────────┘
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [LangChain](https://python.langchain.com/) | Agent framework & LLM abstractions |
| [LangGraph](https://langchain-ai.github.io/langgraph/) | Stateful agent orchestration |
| [LiteLLM](https://docs.litellm.ai/) | Unified LLM gateway (100+ providers) |
| [FAISS](https://github.com/facebookresearch/faiss) | Vector similarity search |
| [Sentence Transformers](https://www.sbert.net/) | Text embeddings |
| [ChromaDB](https://www.trychroma.com/) | Vector database |
| [MCP](https://modelcontextprotocol.io/) | Model Context Protocol for tool servers |
| [LangSmith](https://smith.langchain.com/) | Tracing, evaluation & observability |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-module`)
3. **Add** your notebook or code with clear markdown explanations
4. **Test** that all cells run without errors
5. **Submit** a Pull Request

### Contribution Guidelines

- Each notebook should be self-contained and runnable top-to-bottom
- Include markdown cells explaining **what** and **why**, not just code
- Add your dependencies to `pyproject.toml`
- Follow the existing naming convention: `{number}-{topic}.ipynb`

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## ⭐ Star History

If this project helps you learn or build, consider giving it a ⭐ — it helps others discover it!

---

<div align="center">

**Built with Shamserul ❤️ for the AI engineering community**

</div>