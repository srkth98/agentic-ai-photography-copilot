from langchain_core.tools import tool


@tool
def get_equipment_status() -> dict:
    """Check the current status of the photographer's camera equipment.
    Returns a dictionary with component names as keys and their status
    (OK / LOW / FULL / ERROR) as values, covering battery, memory card,
    lens mount connection, and camera firmware."""
    return {
        "battery": "OK",
        "memory_card": "OK",
        "lens_mount": "CONNECTED",
        "firmware": "UP_TO_DATE"
    }
