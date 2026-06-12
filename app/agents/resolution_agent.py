from app.llm import invoke


RESOLUTION_SYSTEM = """You are a senior photography mentor writing a clear, actionable guide for a photographer.
Be specific, practical, and concrete. Use numbered steps and concrete settings/values where possible.
Reference the provided knowledge base context where relevant.
End with guidance on when to seek further help (e.g. a professional repair shop or experienced photographer) if needed."""


def resolution_agent(state):

    state["execution_path"].append("resolution")

    # Clean text context — no raw Document objects
    context_chunks = state.get("retrieved_docs", [])
    context = "\n\n---\n".join(context_chunks) if context_chunks else "No retrieved context."

    sources = ", ".join(state.get("sources", [])) or "internal knowledge base"
    tool_info = state.get("tool_results", {})
    error_note = ""
    if state.get("error"):
        error_note = f"\n\nNote: Tool execution encountered an error: {state['error']}. Provide a resolution based on available context only."

    prompt = f"""Write a clear, numbered, step-by-step photography resolution or recommendation for this query.

User Query: {state['query']}

Diagnosis Summary:
{state['diagnosis']}

Equipment / Gear Tool Results:
{tool_info}{error_note}

Knowledge Base Context (Sources: {sources}):
{context}

Provide numbered steps. End with guidance on when to seek further help if needed."""

    state["resolution"] = invoke(
        prompt,
        system_prompt=RESOLUTION_SYSTEM,
        max_tokens=800
    )

    return state
