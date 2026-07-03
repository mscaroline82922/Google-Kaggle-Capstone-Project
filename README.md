# Project Sensi: Global Hazard Monitor & Alert System

Project "Sensi" is a production-grade multi-agent system designed to safeguard human life and property from imminent natural and environmental hazards (e.g., Earthquakes and Heatwaves). Built for the Kaggle 5-Day AI Agents Capstone, it leverages Google ADK, MCP, and GenMedia to deliver high-accuracy hazard prediction and reliable response coordination.

## 🏗️ Life-Safety Architecture

Sensi utilizes a multi-layered topology to ensure mission-critical reliability:

1.  **Sensi Orchestrator (Topology Layer)**: Built with Google ADK. Coordinates specialized agents for Seismic and Thermal analysis.
2.  **Logistics Agent (MCP Interoperability)**: Accesses high-accuracy telemetry through a sandboxed MCP Server (Seismic magnitude/depth, Thermal heat indexes).
3.  **Comms Agent (Procedural Skills)**: Maps telemetry thresholds to multi-modal GenMedia (Gemini/Veo) to generate 1080p evacuation visuals and signed alerts.
4.  **Security Guard Node (Self-Healing Runtime)**: Monitors prediction scripts for errors, intercepts exceptions, and performs autonomous repair to ensure 100% system availability.

### 🔄 System Flow
```text
[ Seismic / Thermal Intent ]
             │
             ▼
  ┌─────────────────────┐
  │  Sensi Orchestrator │◀──────────────────┐
  └─────────────────────┘                   │
             │                              │
    ┌────────┴─────────┐                    │ (Self-Healing Loop)
    ▼                  ▼                    │
┌─────────────┐  ┌───────────────┐          │
│ Logistics   │  │ Comms/Media   │          │
│ Agent (MCP) │  │ Agent (Skill) │          │
└─────────────┘  └───────────────┘          │
    │                  │                    │
    ▼                  ▼                    │
┌─────────────┐  ┌───────────────┐          │
│  MCP Server │  │ GenMedia Eng. │          │
└─────────────┘  └───────────────┘          │
    │                  │                    │
    └────────┬─────────┘                    │
             ▼                              │
  ┌─────────────────────┐                   │
  │ Security Guard Node │───────────────────┘
  └─────────────────────┘
             │
             ▼
[ Cryptographically Signed Life-Safety Alert ]
```

## 🛠️ Tool Stack

| Layer | Recommended Tool | Rationale |
| :--- | :--- | :--- |
| Orchestration | **Google ADK** | Professional multi-agent coordination. |
| Interoperability | **MCP (FastMCP)** | Secure telemetry sandboxing. |
| Media Foundation | **Vertex AI GenMedia** | Production-grade 1080p visuals (Veo). |
| Self-Healing | **Custom Guard Node** | Mission-critical runtime resilience. |

## 🚀 Reproduction

### 1. Prerequisites
`pip install google-adk mcp pydantic python-dotenv gradio`

### 2. Launch the Hazard Monitor
```bash
python sensi_workspace/app.py
```
Trigger a **"Seismic Prediction Loop"** for Japan or a **"Thermal Prediction Loop"** for Europe to see the autonomous pipeline in action.

## 🔐 Security & Reliability
- **Sandboxed Telemetry:** No direct access to raw sensor networks; all data flows through validated MCP tools.
- **Self-Healing Runtime:** Autonomous error detection and code repair for 24/7 mission-critical uptime.
- **Signed Dispatch:** Every life-safety alert is cryptographically signed for authenticity.

---
*Developed for the Kaggle 5-Day AI Agents: Intensive Vibe Coding Capstone Project.*
