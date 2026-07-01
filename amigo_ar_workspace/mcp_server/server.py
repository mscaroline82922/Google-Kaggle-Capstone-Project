import json
import random
import sys

# Amigo AR MCP Tools: High-trust financial data sandboxing

def fetch_pending_invoices(customer_id: str = None) -> list:
    """MCP Tool: Retrieves outstanding invoices from the secure ledger."""
    mock_invoices = [
        {"id": "INV-001", "customer": "Acme Corp", "amount": 12500.00, "due_date": "2026-06-01", "status": "OVERDUE"},
        {"id": "INV-002", "customer": "Global Tech", "amount": 8400.50, "due_date": "2026-06-15", "status": "PENDING"},
        {"id": "INV-003", "customer": "Starlight Inc", "amount": 3200.00, "due_date": "2026-05-20", "status": "OVERDUE"},
    ]
    if customer_id:
        return [inv for inv in mock_invoices if inv["customer"].lower() == customer_id.lower()]
    return mock_invoices

def match_bank_records(invoice_id: str) -> dict:
    """MCP Tool: Safely interrogates bank API for matching transaction hashes."""
    # Simulation: 50% chance of finding a match
    match_found = random.choice([True, False])
    if match_found:
        return {
            "match_status": "MATCHED",
            "transaction_id": "TXN_772819BB",
            "amount_received": 12500.00,
            "match_confidence": 0.98
        }
    return {"match_status": "NO_MATCH", "last_bank_sync": "2026-06-23T18:00:00Z"}

def update_ledger_status(invoice_id: str, new_status: str) -> dict:
    """MCP Tool: Updates the internal ERP status with a cryptographic audit trail."""
    return {
        "invoice_id": invoice_id,
        "new_status": new_status,
        "audit_hash": "sha256_b331901a...f122",
        "timestamp": "2026-06-23T19:30:00Z"
    }

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        tool_name = sys.argv[1]
        args = json.loads(sys.argv[2])

        if tool_name == "fetch_pending_invoices":
            print(json.dumps(fetch_pending_invoices(args.get("customer_id"))))
        elif tool_name == "match_bank_records":
            print(json.dumps(match_bank_records(args.get("invoice_id"))))
        elif tool_name == "update_ledger_status":
            print(json.dumps(update_ledger_status(args.get("invoice_id"), args.get("new_status"))))
        else:
            print(f"Unknown AR tool: {tool_name}", file=sys.stderr)
            sys.exit(1)
