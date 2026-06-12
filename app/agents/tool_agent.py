from app.tools.equipment_status_tool import get_equipment_status
from app.tools.ticket_tool import create_ticket
from app.tools.gear_tool import gear_lookup
from app.tools.settings_tool import settings_lookup


def tool_agent(state):

    state["execution_path"].append("tool")
    results = {}
    category = state.get("category", "General").lower()

    try:
        # Always check equipment status when tools are needed
        results["equipment_status"] = get_equipment_status.invoke({})

        # Always create a support ticket for traceability
        results["ticket"] = create_ticket.invoke({"issue": state["query"]})

        # Category-specific tool calls
        if "genresettings" in category or "composition" in category or "lighting" in category:
            # Extract first known genre from query
            known_genres = ["portrait", "landscape", "sports", "wildlife", "astro", "macro", "night", "street"]
            query_lower = state["query"].lower()
            matched = next((g for g in known_genres if g in query_lower), "general")
            results["settings_recommendation"] = settings_lookup.invoke({"genre": matched})

        if "lens" in category or "accessories" in category:
            # Extract gear identifier — fallback to "current_user"
            results["gear_info"] = gear_lookup.invoke({"user": "current_user"})

        state["tool_results"] = results
        state["error"] = ""

    except Exception as e:
        state["error"] = f"Tool execution failed: {str(e)}"
        state["retry_count"] = state.get("retry_count", 0) + 1

    return state
