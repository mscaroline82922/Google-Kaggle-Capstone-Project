import json
import os
import sys
import subprocess
import re

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from sensi_workspace.agents.guard_node import SecurityGuardNode

class SensiHazardOrchestrator:
    def __init__(self):
        self.guard = SecurityGuardNode()
        print("⚡ [Sensi Orchestrator] Life-Safety Topology Layer Active.")

    def _call_mcp(self, tool_name, arguments):
        cmd = [sys.executable, "sensi_workspace/mcp_server/server.py", tool_name, json.dumps(arguments)]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"MCP Tool Error: {result.stderr}")
        return json.loads(result.stdout)

    def analyze_hazard(self, location: str, hazard_type: str):
        logs = []
        logs.append(f"📥 [Intent] Monitoring {hazard_type} risks in {location}")

        # Step 1: Ingest Telemetry (MCP)
        try:
            if hazard_type == "Earthquake":
                telemetry = self._call_mcp("fetch_seismic_activity", {"location": location})
                logs.append(f"🔍 [Logistics Agent] Seismic Data: Mag {telemetry['magnitude']} at {telemetry['depth_km']}km depth.")
            else:
                telemetry = self._call_mcp("fetch_thermal_telemetry", {"location": location})
                logs.append(f"🔍 [Logistics Agent] Thermal Data: {telemetry['temperature_c']}°C | Heat Index: {telemetry['heat_index']}.")

            if telemetry["status"] == "CRITICAL":
                logs.append(f"🚨 [ALERT] CRITICAL {hazard_type.upper()} THRESHOLD REACHED.")
            else:
                logs.append(f"✅ [Status] {hazard_type} levels within manageable parameters.")

        except Exception as e:
            logs.append(f"❌ [Logistics Agent] Telemetry failure: {str(e)}")
            return {"status": "FAILED", "logs": logs}

        # Step 2: Generate Multi-Modal Broadcast (Skills)
        logs.append(f"🎬 [Comms Agent] Mapping {hazard_type} telemetry to GenMedia Engine...")
        skill_input = json.dumps({
            "location": location,
            "hazard_type": hazard_type,
            "telemetry": telemetry
        })

        # Guard Node Monitoring
        skill_output_raw = self.guard.execute_with_healing(
            "sensi_workspace/skills/broadcast_generation/scripts/generate_alert.py",
            [skill_input]
        )

        if not skill_output_raw:
            logs.append("❌ [Security Guard Node] Skill failed after healing attempt.")
            return {"status": "FAILED", "logs": logs}

        try:
            match = re.search(r'\{.*\}', skill_output_raw.replace('\n', ' '))
            skill_output = json.loads(match.group())
            logs.append(f"📢 [Comms Agent] Broadcast Package Ready: '{skill_output['alert_message']}'")
        except:
            logs.append("❌ [Comms Agent] Failed to parse safety package.")
            return {"status": "FAILED", "logs": logs}

        # Step 3: Secure Dispatch (MCP)
        if skill_output["status"] == "SUCCESS":
            logs.append(f"📡 [Sensi Orchestrator] Dispatching signed alert to {location} mesh network...")
            dispatch = self._call_mcp("dispatch_hazard_broadcast", {
                "message": skill_output["alert_message"],
                "signature": f"sha256_{skill_output['dispatch_id']}"
            })
            logs.append(f"✅ [Guard Node] Dispatch verified. Hash: {dispatch['signed_hash']}")
            return {"status": "DISPATCHED", "logs": logs, "output": skill_output, "dispatch": dispatch}
        else:
            logs.append("ℹ️ [Sensi Orchestrator] Threshold not met. System remains in active MONITORING mode.")
            return {"status": "MONITORING", "logs": logs, "output": skill_output}

if __name__ == "__main__":
    orch = SensiHazardOrchestrator()
    print(json.dumps(orch.analyze_hazard("Japan", "Earthquake"), indent=2))
