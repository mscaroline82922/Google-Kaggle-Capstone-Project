import json
import sys

def generate_outreach_email(invoice_data_json: str):
    """
    Simulates a Gemini-powered skill to generate personalized, empathetic
    collection outreach for Amigo customers.
    """
    try:
        data = json.loads(invoice_data_json)
        customer = data.get("customer")
        amount = data.get("amount")
        invoice_id = data.get("id")

        # In a real setup, this would be a prompt to Gemini 2.0
        email_body = f"""
Subject: Assistance with your Amigo Invoice {invoice_id}

Hi {customer} Team,

We hope your week is going well!

We're reaching out regarding invoice {invoice_id} for ${amount:,.2f} which is currently showing as overdue.
At Amigo, we aim to make financial operations seamless. If there's any discrepancy or if you need assistance
setting up a payment plan, please let us know.

Best regards,
The Amigo Finance Team
        """

        output = {
            "status": "DRAFT_READY",
            "customer": customer,
            "generated_body": email_body,
            "tone_analysis": "Empathetic/Professional",
            "compliance_check": "PASSED"
        }
        return json.dumps(output)
    except Exception as e:
        print(f"Error generating outreach: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(generate_outreach_email(sys.argv[1]))
