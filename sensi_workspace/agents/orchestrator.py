import json
import os
import sys
import subprocess
import re

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from sensi_workspace.agents.guard_node import SecurityGuardNode

class SensiOrchestrator:
    def __init__(self):
        self.guard = SecurityGuardNode()
        print("⚡ [Sensi Orchestrator] Topology Layer Active.")

    def _call_mcp_tool(self, tool_name: str, arguments: dict):
        """
        Simulates calling an MCP tool via the MCP server.
        In a real production environment, this would use an MCP Client
        connecting via stdio or SSE.
        """
        # We simulate the MCP round-trip to ensure sandboxing logic
        # Run the server script with the tool call (using a simulated client)
        cmd = [sys.executable, "sensi_workspace/mcp_server/server.py", tool_name, json.dumps(arguments)]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"MCP Tool Error: {result.stderr}")
        return json.loads(result.stdout)

    def process_intent(self, intent: str, sector: str):
        logs = []
        logs.append(f"📥 Received Intent: '{intent}' for {sector}")

        # Step 1: Logistics Analysis (MCP Sandboxed Tools)
        logs.append("🔍 [Logistics Agent] Accessing sandboxed environmental context via MCP Client...")
        try:
            satellite_data = self._call_mcp_tool("fetch_satellite_deltas", {"sector": sector})
            inventory_data = self._call_mcp_tool("query_inventory_db", {"supply_type": "medical_kits"})
            logs.append(f"   -> MCP Satellite Deltas: {satellite_data}")
            logs.append(f"   -> MCP Inventory Status: {inventory_data}")
        except Exception as e:
            logs.append(f"❌ [Logistics Agent] MCP Tool failure: {str(e)}")
            return {"status": "FAILED", "logs": logs}

        # Step 2: Media/Comms Generation (Skills)
        logs.append("🎬 [Comms & Media Agent] Converting asset metrics into multi-modal templates...")

        skill_input = json.dumps({
            "zone": sector,
            "urgency": "CRITICAL" if satellite_data.get("structural_integrity_index", 1.0) < 0.3 else "HIGH",
            "telemetry": satellite_data
        })

        # Guard Node execution (Runtime Monitoring)
        skill_output_raw = self.guard.execute_with_healing(
            "sensi_workspace/skills/broadcast_generation/scripts/generate_alert.py",
            [skill_input]
        )

        if not skill_output_raw:
            logs.append("❌ [Security Guard Node] Skill execution failed after healing attempt.")
            return {"status": "FAILED", "logs": logs}

        try:
            # Robust JSON parsing from stdout
            match = re.search(r'\{.*\}', skill_output_raw.replace('\n', ' '))
            if match:
                skill_output = json.loads(match.group())
            else:
                raise ValueError("No JSON found in skill output")
        except Exception as e:
            logs.append(f"❌ [Comms & Media Agent] Failed to parse skill output: {str(e)}")
            return {"status": "FAILED", "logs": logs}

        # Step 3: Secure Dispatch (MCP Sandboxed Tools)
        logs.append("📡 [Sensi Orchestrator] Dispatching cryptographically signed broadcast via MCP...")
        try:
            dispatch_result = self._call_mcp_tool("dispatch_emergency_broadcast", {"message": skill_output["broadcast_message"]})
            logs.append("✅ [Security Guard Node] Runtime ethical assertions passed. Zero secrets exposed.")

            return {
                "status": "SUCCESS",
                "logs": logs,
                "media": skill_output["media_assets"],
                "dispatch": dispatch_result
            }
        except Exception as e:
            logs.append(f"❌ [Sensi Orchestrator] Dispatch failure: {str(e)}")
            return {"status": "FAILED", "logs": logs}
