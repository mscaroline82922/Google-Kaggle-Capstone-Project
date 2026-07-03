# Skill: Multi-Modal Hazard Broadcast Generation
**Procedural Memory Identifier:** `sensi.skills.v1.broadcast_generation`

## 1. Overview
This skill implements the standardized procedural workflow for transforming raw environmental telemetry (Seismic/Thermal) into high-fidelity, actionable life-safety media. It bridges the gap between structured data and human-centric crisis communication using generative AI model chains.

## 2. Procedural Workflow
The following steps are executed by the Comms Agent when this skill is invoked:

1.  **Payload Ingestion:** Receive JSON-structured telemetry from the Logistics Agent (via MCP Server).
2.  **Telemetry Analysis:**
    *   Evaluate Seismic Magnitude/Depth against safety thresholds (e.g., Mag > 6.0).
    *   Evaluate Thermal Heat Index against regional safety bands (e.g., Temp > 42°C).
3.  **Media Asset Specification:**
    *   **Prompt Engineering:** Dynamically generate high-fidelity prompts for **Gemini 3 Pro Image** and **Veo**.
    *   **Visual Context:** Inject location-specific landmarks to ensure evacuation visuals are recognizable by local populations.
4.  **Generative Chain Invocation:**
    *   Call **Gemini 3 Pro** for static infographic generation (Safety Checklists).
    *   Call **Veo** for 1080p video production (Dynamic Evacuation Routes).
5.  **Alert Signing & Dispatch:**
    *   Generate a unique `dispatch_id` based on alert content hash.
    *   Package assets for hand-off back to the Sensi Orchestrator.

## 3. Input Specification
```json
{
  "location": "Tokyo, Japan",
  "hazard_type": "Earthquake",
  "telemetry": {
    "magnitude": 7.2,
    "depth_km": 15.0,
    "status": "CRITICAL"
  }
}
```

## 4. Output Specification
```json
{
  "status": "SUCCESS",
  "alert_message": "URGENT: Evacuation orders in effect...",
  "media_config": {
    "engine": "Veo",
    "prompt": "1080p aerial cinematic view of...",
    "resolution": "1080p"
  },
  "dispatch_id": "sha256_..."
}
```

## 5. References & Assets
- `/references/safety_protocols.pdf`: Standard operating procedures for hazard alerts.
- `/scripts/generate_alert.py`: Main execution logic for the skill.
- `/assets/logo_watermark.png`: Security branding for official broadcasts.
