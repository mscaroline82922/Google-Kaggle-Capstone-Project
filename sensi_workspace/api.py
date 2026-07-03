from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sensi_workspace.agents.orchestrator import orchestrator

app = FastAPI(title="Sensi Life-Safety API", version="1.0.0")

class HazardRequest(BaseModel):
    location: str
    hazard_type: str

@app.get("/status")
async def get_system_status():
    return {
        "system": "Project Sensi",
        "status": "Operational",
        "agents": ["Orchestrator", "Logistics", "Comms", "Security Guard"],
        "mcp_connection": "Secure"
    }

@app.post("/analyze")
async def analyze_hazard(request: HazardRequest):
    try:
        result = orchestrator.trigger_hazard_analysis(request.location, request.hazard_type)
        if not result["success"]:
            raise HTTPException(status_code=500, detail=result.get("error", "Unknown Orchestration Error"))
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
