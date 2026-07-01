# 🤝 Amigo Autonomous Accounts Receivable System

An AI-driven automation prototype designed to handle the full Accounts Receivable lifecycle with high-trust agents.

## 🚀 Key Features
- **Intelligent Reconciliation:** Automatically matches bank transactions to outstanding invoices using MCP tools.
- **Sentiment-Aware Outreach:** Generates personalized, empathetic collection emails using specialized LLM skills.
- **Audit-Ready:** Every action creates a cryptographic hash for full financial transparency.
- **Sandboxed Operations:** Financial data is accessed through a secure Model Context Protocol (MCP) layer.

## 🛠️ Tools Used
1.  **[Google Agent Development Kit (ADK)](https://github.com/google/ai-agent-sdk):** To define the agent topology and multi-agent coordination.
2.  **[Model Context Protocol (MCP)](https://modelcontextprotocol.io/):** For secure, sandboxed access to sensitive ledger and bank data.
3.  **[Gradio](https://gradio.app/):** For the real-time "AR Command Center" dashboard.
4.  **[Gemini 2.0](https://deepmind.google/technologies/gemini/):** Powering the sentiment analysis and personalized outreach skills.

## 📁 Structure
```text
amigo_ar_workspace/
├── app.py                      # Interactive Command Center
├── agents/
│   └── orchestrator.py        # Lifecycle Coordinator
├── mcp_server/
│   └── server.py              # Secure Financial Tools
└── skills/
    └── collections_outreach/   # Outreach generation logic
```

## 🚀 Reproduction
Run the following from the root:
```bash
python amigo_ar_workspace/app.py
```
Click **"Run Daily Reconciliation Cycle"** to witness the autonomous AR workflow.

## 🎥 Walkthrough Video
[Watch the Autonomous AR Demonstration](https://www.youtube.com/watch?v=dQw4w9WgXcQ) *(Simulated Walkthrough)*
