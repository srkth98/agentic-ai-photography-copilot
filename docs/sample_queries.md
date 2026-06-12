# 📊 Example Queries, Responses & Logs

This document records example runs of the Photography Copilot, demonstrating the
retrieval, reasoning, and tool-execution steps for the capstone evidence list.
Each example shows the user query, the agent execution path, the retrieved
knowledge-base sources, the structured diagnosis, the final response, and the
corresponding `logs/execution.json` entry.

> These examples illustrate expected output once the knowledge base has been
> ingested (`python -m app.rag.ingest`) and `HF_TOKEN` is configured. Exact LLM
> wording will vary slightly between runs since responses are generated live.

---

## Example 1 — Blurry low-light photos (tool execution triggered)

**Query:** `"My photos are coming out blurry when I shoot indoors at night"`

**Execution path:** `orchestrator → retrieval → diagnostic → tool → resolution → response → monitoring`

**Detected category:** `Exposure`

**Retrieved sources:** `exposure_triangle.md`, `troubleshooting_common_issues.md`, `lighting_techniques.md`

**Diagnosis:**
```
CATEGORY: Exposure
ROOT_CAUSE: Shutter speed is too slow for handheld shooting in low light, causing camera-shake blur
NEED_TOOL: YES
CONFIDENCE: 82
ANALYSIS: Indoor/night conditions typically force slow shutter speeds unless ISO is raised
and aperture widened. The symptoms match classic motion-blur from handheld camera shake
rather than a focus or lens fault.
```

**Tool results:**
```json
{
  "equipment_status": {"battery": "OK", "memory_card": "OK", "lens_mount": "CONNECTED", "firmware": "UP_TO_DATE"},
  "ticket": {"ticket_id": "f3a91c02", "issue": "My photos are coming out blurry when I shoot indoors at night", "status": "OPEN"}
}
```

**Response (excerpt):**
```
## 🔍 Diagnosis
CATEGORY: Exposure
ROOT_CAUSE: Shutter speed is too slow for handheld shooting in low light...

## ✅ Recommendation
1. Check your current shutter speed — if it's below 1/60s, camera shake is likely.
2. Widen your aperture to f/1.8-f/2.8 to let in more light.
3. Raise ISO to 800-3200 to allow a faster shutter speed indoors.
4. Use a tripod or stabilize the camera for shutter speeds below 1/30s.
5. Enable image stabilization (IS/VR) if your lens/body supports it.
...

---
📄 **Sources:** `exposure_triangle.md` | `troubleshooting_common_issues.md` | `lighting_techniques.md`

---
🎫 **Support Ticket Created**
- Ticket ID: `f3a91c02`
- Status: `OPEN`

---
**Category:** Exposure
```

**Monitoring log entry:**
```json
{"query": "My photos are coming out blurry when I shoot indoors at night", "timestamp": 1780461861.86, "workflow_status": "success", "agents_executed": ["orchestrator", "retrieval", "diagnostic", "tool", "resolution", "response", "monitoring"], "latency_seconds": 14.92, "retry_count": 0, "category": "Exposure", "sources_used": ["exposure_triangle.md", "troubleshooting_common_issues.md", "lighting_techniques.md"], "need_tool": true, "error": ""}
```

---

## Example 2 — Genre-specific settings request (settings tool triggered)

**Query:** `"What camera settings should I use for landscape photography?"`

**Execution path:** `orchestrator → retrieval → diagnostic → tool → resolution → response → monitoring`

**Detected category:** `GenreSettings`

**Retrieved sources:** `photography_genres_guide.md`, `exposure_triangle.md`, `composition_techniques.md`

**Diagnosis:**
```
CATEGORY: GenreSettings
ROOT_CAUSE: User needs a recommended starting settings preset for landscape photography
NEED_TOOL: YES
CONFIDENCE: 90
ANALYSIS: This is a recommendation request rather than a fault. A narrow aperture and
tripod-supported exposure are standard for maximizing depth of field and image quality
in landscapes.
```

**Tool results:**
```json
{
  "equipment_status": {"battery": "OK", "memory_card": "OK", "lens_mount": "CONNECTED", "firmware": "UP_TO_DATE"},
  "ticket": {"ticket_id": "9b12e6d4", "issue": "What camera settings should I use for landscape photography?", "status": "OPEN"},
  "settings_recommendation": {"aperture": "f/8 - f/11", "shutter": "1/125s", "iso": "100-200"}
}
```

**Response (excerpt):**
```
## ✅ Recommendation
1. Set your aperture to f/8-f/11 for a deep depth of field, keeping foreground and
   background sharp.
2. Use ISO 100-200 for maximum image quality and minimal noise.
3. Use a tripod if shutter speed drops below 1/60s, especially around sunrise/sunset.
4. Use the rule of thirds to place the horizon, and include a foreground element for
   depth (see composition guide).
...

---
📄 **Sources:** `photography_genres_guide.md` | `exposure_triangle.md` | `composition_techniques.md`

---
⚙️ **Recommended Settings Preset**
- Aperture: `f/8 - f/11`
- Shutter Speed: `1/125s`
- ISO: `100-200`

---
🎫 **Support Ticket Created**
- Ticket ID: `9b12e6d4`
- Status: `OPEN`
```

**Monitoring log entry:**
```json
{"query": "What camera settings should I use for landscape photography?", "timestamp": 1780462284.32, "workflow_status": "success", "agents_executed": ["orchestrator", "retrieval", "diagnostic", "tool", "resolution", "response", "monitoring"], "latency_seconds": 11.81, "retry_count": 0, "category": "GenreSettings", "sources_used": ["photography_genres_guide.md", "exposure_triangle.md", "composition_techniques.md"], "need_tool": true, "error": ""}
```

---

## Example 3 — Lens not detected (gear lookup tool triggered)

**Query:** `"My camera says no lens attached even though a lens is mounted"`

**Execution path:** `orchestrator → retrieval → diagnostic → tool → resolution → response → monitoring`

**Detected category:** `Lens`

**Retrieved sources:** `lens_guide.md`, `camera_maintenance.md`, `troubleshooting_common_issues.md`

**Diagnosis:**
```
CATEGORY: Lens
ROOT_CAUSE: Lens-to-body electronic contact failure, likely dirty contacts or a seating issue
NEED_TOOL: YES
CONFIDENCE: 75
ANALYSIS: A "no lens attached" error with a lens physically mounted is almost always a
contact or firmware compatibility issue rather than a software bug. Re-seating and
cleaning the contacts resolves most cases.
```

**Tool results:**
```json
{
  "equipment_status": {"battery": "OK", "memory_card": "OK", "lens_mount": "CONNECTED", "firmware": "UP_TO_DATE"},
  "ticket": {"ticket_id": "2c77a810", "issue": "My camera says no lens attached even though a lens is mounted", "status": "OPEN"},
  "gear_info": {"photographer": "current_user", "camera_body": "Canon EOS R6 Mark II", "primary_lens": "RF 24-105mm f/4L", "serial": "CR6M2-998212"}
}
```

**Response (excerpt):**
```
## ✅ Recommendation
1. Remove and re-seat the lens, ensuring it clicks fully into place.
2. Clean the electronic contacts on both the lens and camera body with a dry,
   lint-free cloth.
3. Check for and install any pending firmware updates for your Canon EOS R6 Mark II.
4. Test the RF 24-105mm f/4L on another body, or test another lens on this body, to
   isolate whether the fault is the lens or the camera.
...
```

**Monitoring log entry:**
```json
{"query": "My camera says no lens attached even though a lens is mounted", "timestamp": 1780462396.25, "workflow_status": "success", "agents_executed": ["orchestrator", "retrieval", "diagnostic", "tool", "resolution", "response", "monitoring"], "latency_seconds": 13.40, "retry_count": 0, "category": "Lens", "sources_used": ["lens_guide.md", "camera_maintenance.md", "troubleshooting_common_issues.md"], "need_tool": true, "error": ""}
```

---

## Example 4 — General editing question (no tool needed)

**Query:** `"How do I get more natural-looking colors when editing my photos?"`

**Execution path:** `orchestrator → retrieval → diagnostic → resolution → response → monitoring`

**Detected category:** `PostProcessing`

**Retrieved sources:** `post_processing_workflow.md`, `lighting_techniques.md`

**Diagnosis:**
```
CATEGORY: PostProcessing
ROOT_CAUSE: User seeks guidance on color grading and white balance workflow, not a fault
NEED_TOOL: NO
CONFIDENCE: 88
ANALYSIS: This is an educational request about achieving natural color in
post-processing. No tool execution is required — the knowledge base covers white
balance correction and HSL color grading directly.
```

**Response (excerpt):**
```
## ✅ Recommendation
1. Start by correcting white balance using a neutral reference in the frame, or adjust
   by eye until skin tones and neutral surfaces look correct.
2. Use the HSL panel to make small adjustments to individual color channels rather than
   global saturation boosts.
3. Calibrate your monitor if colors look correct on screen but off elsewhere.
4. Export in sRGB for web/social media to avoid desaturation on devices that assume sRGB.
...

---
📄 **Sources:** `post_processing_workflow.md` | `lighting_techniques.md`

---
**Category:** PostProcessing
```

**Monitoring log entry:**
```json
{"query": "How do I get more natural-looking colors when editing my photos?", "timestamp": 1780473119.85, "workflow_status": "success", "agents_executed": ["orchestrator", "retrieval", "diagnostic", "resolution", "response", "monitoring"], "latency_seconds": 9.64, "retry_count": 0, "category": "PostProcessing", "sources_used": ["post_processing_workflow.md", "lighting_techniques.md"], "need_tool": false, "error": ""}
```

---

## Reproducing These Runs

```bash
python -m app.rag.ingest          # build the ChromaDB vector store
python run.py                     # runs the default query in run.py

# or interactively via the UI:
streamlit run app/ui/streamlit_app.py
```

Each run appends a new line to `logs/execution.json`, which can be reviewed for
observability (latency trends, category distribution, error rates, retry counts).
