import json
import subprocess
import sys
import re

class AROrchestrator:
    """
    Orchestrates the Amigo AR Automation Lifecycle:
    Reconciliation -> Classification -> Outreach -> Resolution.
    """

    def __init__(self):
        print("⚡ [Amigo AR Orchestrator] Initializing financial nodes...")

    def _call_mcp(self, tool_name, args):
        cmd = [sys.executable, "amigo_ar_workspace/mcp_server/server.py", tool_name, json.dumps(args)]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return json.loads(result.stdout)

    def run_reconciliation_cycle(self):
        logs = []
        logs.append("📅 Starting Automated Daily Reconciliation Cycle...")

        # 1. Fetch overdue invoices
        invoices = self._call_mcp("fetch_pending_invoices", {})
        overdue = [i for i in invoices if i["status"] == "OVERDUE"]
        logs.append(f"🔍 Found {len(overdue)} overdue items in the ledger.")

        results = []
        for inv in overdue:
            logs.append(f"--- Processing {inv['id']} ({inv['customer']}) ---")

            # 2. Match with Bank Records
            bank_match = self._call_mcp("match_bank_records", {"invoice_id": inv["id"]})

            if bank_match["match_status"] == "MATCHED":
                logs.append(f"✅ Payment Match Detected! Updating ledger for {inv['id']}...")
                update = self._call_mcp("update_ledger_status", {"invoice_id": inv["id"], "new_status": "PAID"})
                results.append({"id": inv["id"], "action": "SETTLED", "audit": update["audit_hash"]})
            else:
                logs.append(f"⚠️ No bank match found. Escalating to Collections Outreach Agent...")

                # 3. Trigger Outreach Skill
                skill_input = json.dumps(inv)
                skill_cmd = [sys.executable, "amigo_ar_workspace/skills/collections_outreach/scripts/generate_email.py", skill_input]
                skill_result = subprocess.run(skill_cmd, capture_output=True, text=True)

                try:
                    email_draft = json.loads(skill_result.stdout)
                    logs.append(f"📧 Autonomous outreach drafted for {inv['customer']}.")
                    results.append({"id": inv["id"], "action": "OUTREACH_DRAFTED", "draft": email_draft["generated_body"]})
                except:
                    logs.append(f"❌ Error in outreach skill execution.")

        return {"logs": logs, "summary": results}

if __name__ == "__main__":
    orch = AROrchestrator()
    print(json.dumps(orch.run_reconciliation_cycle(), indent=2))
