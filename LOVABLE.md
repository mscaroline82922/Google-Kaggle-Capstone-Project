# Project Sensi: Lovable Vibe Integration

This project is architected to transition from a CLI-based prototype to a modern full-stack application suitable for high-fidelity deployment in environments like **Lovable**.

## 🏗️ Tech Stack

- **Backend:** FastAPI (Python) - Handles multi-agent orchestration, MCP sandboxing, and self-healing logic.
- **Frontend:** React + Tailwind CSS (Vite) - Provides a high-fidelity "Crisis Command Center" UI.
- **Orchestration:** Google ADK - Manages the life-safety topology.
- **Interoperability:** MCP - Ensures secure telemetry data flow.

## 📁 Lovable Project Structure

```text
sensi_workspace/
├── api.py                      # FastAPI Backend
└── agents/                     # ADK Agents & Guard Node
sensi_frontend/                 # Modern React Dashboard
├── src/
│   ├── App.jsx                 # Dashboard State & Layout
│   └── components/             # Reusable UI (Console, Telemetry)
```

## 🚀 Deployment Instructions (Vibe Coding)

### 1. Launch the Backend
```bash
python sensi_workspace/api.py
```
Starts the life-safety REST API on `localhost:8000`.

### 2. Launch the Frontend
```bash
cd sensi_frontend
npm install
npm run dev
```
Starts the React dashboard with HMR.

## 🛡️ Resilience & Trust
The integration preserves the **Security Guard Node** at the backend level, ensuring that even in a full-stack environment, the core life-safety prediction scripts are monitored and self-healed autonomously.
