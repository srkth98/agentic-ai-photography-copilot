#  Agentic AI Photography & Camera Copilot

A multi-agent **RAG (Retrieval-Augmented Generation)** orchestration system that acts as an
expert photography assistant — answering questions about camera settings, lenses, lighting,
composition, post-processing, gear maintenance, and troubleshooting.

Built for the **AI Agentic Workflow & Orchestration Capstone**.

---

##  What It Does

A user describes a photography problem or question (e.g. *"My photos are blurry in low
light"* or *"What settings should I use for portrait photography?"*), and a 7-agent
LangGraph workflow:

1. **Classifies** the query into a photography topic (Exposure, Lens, Lighting, etc.)
2. **Retrieves** relevant knowledge-base articles from a ChromaDB vector store
3. **Diagnoses** the issue with a structured root-cause analysis
4. **Executes tools** (equipment status check, gear lookup, settings recommendation,
   support ticket creation) when needed
5. **Generates** a step-by-step resolution / recommendation
6. **Formats** a final response with source citations
7. **Logs** monitoring data (latency, category, sources, errors) for observability

---

##  Architecture

```
User (CLI / Streamlit UI)
        │
        ▼
┌─────────────────────────────────────────────────────────────────┐
│                  LangGraph Orchestration                        │
│                                                                 │
│  Orchestrator → Retrieval → Diagnostic ─┬─► Tool ─► Resolution  │
│   (classify)     (ChromaDB MMR)  (LLM)  │   (retry loop)  ▼     │
│                                         └────────────► Response │
│                                                              │  │
│                                                       Monitoring│
└────────────────────────────────────────────────────────────┘
        │                              │
        ▼                              ▼
   logs/execution.json          Final Markdown Response
```

See [`docs/architecture.md`](docs/architecture.md) for the full diagram, state schema,
and step-by-step walkthrough.

---

##  Project Structure

```
agentic-ai-photography-copilot/
│
├── .env                          ← HF_TOKEN config
├── run.py                        ← CLI entry point
├── requirements.txt
├── run.txt                       ← Setup steps
│
├── knowledge_base/               ← 10 photography markdown articles (RAG source)
├── chroma_db/                    ← Vector DB (auto-built by ingest)
├── logs/
│   └── execution.json            ← Monitoring agent execution log
├── docs/
│   ├── architecture.md           ← Architecture diagrams + walkthrough
│   └── sample_queries.md         ← Example queries & responses (evidence)
│
└── app/
    ├── llm.py                    ← LLM wrapper (Hugging Face Llama 3.1)
    │
    ├── agents/
    │   ├── orchestrator.py       ← LLM-based topic classification
    │   ├── retrieval_agent.py    ← ChromaDB MMR retrieval + source attribution
    │   ├── diagnostic_agent.py   ← Structured root-cause / recommendation analysis
    │   ├── tool_agent.py         ← Selective tool execution + retry logic
    │   ├── resolution_agent.py   ← Step-by-step resolution synthesis
    │   ├── response_agent.py     ← Final markdown formatting + citations
    │   └── monitoring_agent.py   ← Latency tracking + JSON logging
    │
    ├── rag/
    │   ├── loader.py, chunker.py, embeddings.py
    │   ├── vectordb.py, retriever.py (MMR search)
    │   └── ingest.py              ← Build the vector store
    │
    ├── tools/
    │   ├── equipment_status_tool.py  ← Camera/lens/battery/storage status
    │   ├── ticket_tool.py            ← Create support ticket
    │   ├── gear_tool.py              ← Photographer's assigned gear lookup
    │   └── settings_tool.py          ← Recommended settings preset for a genre
    │
    ├── workflows/
    │   ├── state.py               ← Shared AgentState schema
    │   └── graph.py                ← LangGraph wiring + conditional edges
    │
    ├── monitoring/
    │   ├── logger.py, metrics.py, evaluator.py
    │
    └── ui/
        └── streamlit_app.py        ← Interactive web UI
```

---

##  Technology Stack

| Technology | Role |
|---|---|
| **LangGraph** | Stateful multi-agent workflow with conditional routing & retries |
| **ChromaDB** | Local vector database for the photography knowledge base |
| **BAAI/bge-small-en-v1.5** | Local embedding model (Hugging Face) |
| **Llama 3.1 8B Instruct** | LLM reasoning (classification, diagnosis, resolution) via HF Inference API |
| **LangChain** | Document loading, text splitting, `@tool` integration |
| **Streamlit** | Interactive web UI with live metrics & pipeline visualization |

---

##  Quick Start

See [`run.txt`](run.txt) for full setup steps. In short:

```bash
python -m venv venv
source venv/bin/activate          # venv\Scripts\activate on Windows
pip install -r requirements.txt

# Add your Hugging Face token to .env
echo "HF_TOKEN=hf_xxx" >> .env

# Build the vector store from the knowledge base
python -m app.rag.ingest

# Run via CLI
python run.py

# Or run the Streamlit UI
streamlit run app/ui/streamlit_app.py
```

---

##  Knowledge Base

The `knowledge_base/` folder contains 10 markdown articles covering:

- Exposure triangle (ISO, aperture, shutter speed)
- Lens selection guide
- Lighting techniques
- Composition fundamentals
- Camera maintenance & cleaning
- Memory cards & file storage
- Post-processing workflow
- Photography genre settings (portrait, landscape, wildlife, astro, macro, sports)
- Troubleshooting common issues (blur, noise, focus, battery)
- Camera accessories guide

---

##  Observability

Every workflow run is logged to `logs/execution.json` with:

- query, timestamp, workflow status
- agents executed (execution path)
- latency in seconds
- detected category
- knowledge-base sources used
- tool retry count and any errors

See [`docs/sample_queries.md`](docs/sample_queries.md) for example queries, responses,
and log entries.

---

##  Capstone Deliverables Mapping

| Requirement | Where |
|---|---|
| Architecture diagram | `docs/architecture.md` |
| Retrieval pipeline (vector embeddings) | `app/rag/` |
| Agent + orchestration | `app/agents/`, `app/workflows/graph.py` |
| Tool execution | `app/tools/`, `app/agents/tool_agent.py` |
| Monitoring / observability | `app/monitoring/`, `logs/execution.json` |
| Example queries & responses | `docs/sample_queries.md` |
| Demo | `run.py` (CLI) and `app/ui/streamlit_app.py` (UI) |
