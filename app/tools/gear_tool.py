from langchain_core.tools import tool


@tool
def gear_lookup(user: str) -> dict:
    """Look up the camera gear kit assigned to or registered by a photographer.
    Returns the photographer identifier, camera body model, primary lens,
    and serial number."""
    return {
        "photographer": user,
        "camera_body": "Canon EOS R6 Mark II",
        "primary_lens": "RF 24-105mm f/4L",
        "serial": "CR6M2-998212"
    }
