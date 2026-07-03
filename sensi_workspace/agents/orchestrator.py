import json
import os
import sys
import subprocess
import re
from typing import Dict, List, Any

# Ensure project root is in path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if project_root not in sys.path:
    sys.path.append(project_root)

from sensi_workspace.agents.guard_node import SecurityGuardNode

class SensiOrchestrator:
    """
    Production-grade Orchestrator for Lovable Full-Stack Integration.
    Coordinates between MCP Telemetry and Generative Media Skills.
    """

    def __init__(self):
        self.guard = SecurityGuardNode()
        self.mcp_server_path = "sensi_workspace/mcp_server/server.py"

    def _call_mcp(self, tool_name: str, args: Dict[str, Any]) -> Dict[str, Any]:
        cmd = [sys.executable, self.mcp_server_path, tool_name, json.dumps(args)]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"MCP Error: {result.stderr}")
        return json.loads(result.stdout)

    def trigger_hazard_analysis(self, location: str, hazard_type: str) -> Dict[str, Any]:
        logs = []
        logs.append(f"INBOUND: {hazard_type} monitoring requested for {location}")

        # 1. Telemetry Ingestion (MCP)
        try:
            if hazard_type.lower() == "earthquake":
                telemetry = self._call_mcp("fetch_seismic_activity", {"location": location})
            else:
                telemetry = self._call_mcp("fetch_thermal_telemetry", {"location": location})

            logs.append(f"LOGISTICS: Telemetry ingested for {location} (Status: {telemetry['status']})")
        except Exception as e:
            return {"success": False, "error": str(e), "logs": logs}

        # 2. Safety Packaging (Skills via Guard Node)
        skill_input = json.dumps({"location": location, "hazard_type": hazard_type, "telemetry": telemetry})
        skill_path = "sensi_workspace/skills/broadcast_generation/scripts/generate_alert.py"

        skill_output_raw = self.guard.execute_with_healing(skill_path, [skill_input])

        try:
            match = re.search(r'\{.*\}', skill_output_raw.replace('\n', ' '))
            skill_output = json.loads(match.group())
            logs.append(f"COMMS: Multi-modal broadcast generated for {location}")
        except:
            return {"success": False, "error": "Skill Output Parsing Failed", "logs": logs}

        # 3. Final Dispatch
        if skill_output["status"] == "SUCCESS":
            dispatch = self._call_mcp("dispatch_hazard_broadcast", {
                "message": skill_output["alert_message"],
                "signature": f"sha256_{skill_output['dispatch_id']}"
            })
            logs.append(f"ORCHESTRATOR: Signed Alert Dispatched (Hash: {dispatch['signed_hash']})")
            return {
                "success": True,
                "status": "DISPATCHED",
                "logs": logs,
                "telemetry": telemetry,
                "alert": skill_output,
                "dispatch": dispatch
            }

        return {
            "success": True,
            "status": "MONITORING",
            "logs": logs,
            "telemetry": telemetry
        }

# Global Instance
orchestrator = SensiOrchestrator()
