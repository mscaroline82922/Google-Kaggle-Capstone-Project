# Project Sensi: AI-Driven Crisis Response System

Project "Sensi" is a production-grade multi-agent system designed for high-stakes environmental monitoring and emergency response. Built for the Kaggle 5-Day AI Agents Capstone, it leverages the Google Agent Development Kit (ADK), Model Context Protocol (MCP), and Generative Media (Gemini/Veo) to transform raw telemetry into actionable, high-fidelity safety broadcasts.

## 🏗️ Architectural Blueprint

Sensi utilizes a multi-layered architecture to separate high-risk ingestion from multi-modal generation while enforcing strict security guardrails.

1.  **Sensi Orchestrator (Topology Layer)**: Built with Google ADK. It parses natural language intent and coordinates specialized agents.
2.  **Logistics Agent (Interoperability Layer)**: Interacts with the custom MCP Server to fetch satellite deltas and inventory data without direct database exposure.
3.  **Comms & Media Agent (Skill Layer)**: Uses procedural memory (Agent Skills) to map telemetry to GenMedia pipelines (Gemini 2.0 & Veo).
4.  **Security Guard Node (Self-Healing Runtime)**: Monitors execution streams, intercepts exceptions, and performs autonomous code repair.

## 🛠️ Tool Stack

| Layer | Recommended Tool | Rationale |
| :--- | :--- | :--- |
| Orchestration | **Google ADK** | Native agent schemas and lifecycle hooks. |
| Interoperability | **MCP Python SDK** | Safe tool sandboxing and data abstraction. |
| Media Foundation | **Vertex AI GenMedia** | Production-grade 1080p visualization (Veo). |
| Self-Healing | **Custom Guard Node** | Automated runtime error correction. |

## 📁 Repository Structure

```text
sensi_workspace/
├── .env                        # Secure environment configuration (Mocked)
├── agents/
│   ├── orchestrator.py        # ADK Topology & Agent definitions
│   └── guard_node.py          # Self-healing runtime logic
├── mcp_server/
│   └── server.py              # FastMCP server with validated tools
└── skills/
    └── broadcast_generation/
        ├── SKILL.md           # Procedural skill documentation
        ├── scripts/           # Execution scripts (generate_alert.py)
        └── assets/            # Generated media artifacts (Simulated)
```

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- `google-adk`, `mcp`, `pydantic`

### 2. Setup
```bash
pip install google-adk mcp pydantic python-dotenv
```

### 3. Run the MCP Server
```bash
python sensi_workspace/mcp_server/server.py
```

### 4. Run Runtime Verification (Self-Healing Demo)
```bash
python sensi_workspace/agents/guard_node.py
```

## 🔐 Security & Compliance
- **Secrets Management**: Credentials are kept in `.env` and should be mapped to Kaggle User Secrets in production.
- **Sandboxing**: Agents never have direct SQL access; all data flows through validated MCP tools.
- **Signed Alerts**: Every broadcast message is cryptographically signed to ensure authenticity.

---
*Developed for the Kaggle 5-Day AI Agents: Intensive Vibe Coding Capstone Project.*
