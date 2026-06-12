from langchain_core.tools import tool


@tool
def settings_lookup(genre: str) -> dict:
    """Look up the recommended starting camera settings preset for a given
    photography genre (portrait, landscape, sports, wildlife, astro, macro,
    night, street). Returns aperture, shutter speed, and ISO recommendations,
    or a 'no preset available' message for unknown genres."""
    presets = {
        "portrait":  {"aperture": "f/1.8 - f/2.8", "shutter": "1/200s", "iso": "100-400"},
        "landscape": {"aperture": "f/8 - f/11",     "shutter": "1/125s", "iso": "100-200"},
        "sports":    {"aperture": "f/2.8 - f/4",    "shutter": "1/1000s", "iso": "400-1600"},
        "wildlife":  {"aperture": "f/4 - f/5.6",    "shutter": "1/1000s", "iso": "400-1600"},
        "astro":     {"aperture": "f/1.4 - f/2.8",  "shutter": "15-25s",  "iso": "1600-3200"},
        "macro":     {"aperture": "f/8 - f/16",     "shutter": "1/200s",  "iso": "200-800"},
        "night":     {"aperture": "f/1.8 - f/2.8",  "shutter": "1/30 - 2s", "iso": "800-3200"},
        "street":    {"aperture": "f/5.6 - f/8",    "shutter": "1/250s", "iso": "200-800"},
    }
    return presets.get(genre.lower(), {"preset": "no preset available"})
