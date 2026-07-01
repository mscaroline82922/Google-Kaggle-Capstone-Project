import gradio as gr
import json
import os
import sys

# Add project root to path
sys.path.append(os.path.abspath(os.getcwd()))

from amigo_ar_workspace.agents.orchestrator import AROrchestrator

orchestrator = AROrchestrator()

def run_ar_pipeline():
    result = orchestrator.run_reconciliation_cycle()

    logs = "\n".join(result["logs"])

    summary_md = "### 📊 AR Cycle Summary\n"
    actions = result["summary"]

    settled = [a for a in actions if a["action"] == "SETTLED"]
    outreach = [a for a in actions if a["action"] == "OUTREACH_DRAFTED"]

    summary_md += f"- **Invoices Settled:** {len(settled)}\n"
    summary_md += f"- **Outreach Drafts Generated:** {len(outreach)}\n"

    detailed_md = "#### 📄 Detailed Actions\n"
    for item in actions:
        status_icon = "✅" if item["action"] == "SETTLED" else "📧"
        detailed_md += f"- {status_icon} **{item['id']}**: {item['action']}\n"
        if "draft" in item:
            detailed_md += f"  > *Drafting email to customer...*\n"

    return logs, summary_md, detailed_md

custom_css = """
.gradio-container { background-color: #f8fafc; color: #1e293b; }
.ar-header { text-align: center; color: #4f46e5; }
.log-box { font-family: monospace; background-color: #f1f5f9; border: 1px solid #cbd5e1; }
"""

with gr.Blocks(css=custom_css, theme=gr.themes.Default(primary_hue="indigo")) as demo:
    gr.Markdown("# 🤝 Amigo Autonomous AR Command Center", elem_classes=["ar-header"])
    gr.Markdown("### Automating the Accounts Receivable Lifecycle with High-Trust Agents")

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("#### 🛠️ Operation Control")
            run_btn = gr.Button("▶️ Run Daily Reconciliation Cycle", variant="primary")
            gr.Markdown("""
            **Automated Checks:**
            - [x] Secure Ledger Sync
            - [x] Bank Record Matching
            - [x] Sentiment-Aware Outreach
            - [x] Cryptographic Audit Trail
            """)

        with gr.Column(scale=2):
            gr.Markdown("#### 📟 Audit Logs")
            log_display = gr.Textbox(label="", interactive=False, lines=15, elem_classes=["log-box"])

    with gr.Row():
        with gr.Column():
            summary_out = gr.Markdown()
        with gr.Column():
            detailed_out = gr.Markdown()

    run_btn.click(
        fn=run_ar_pipeline,
        inputs=[],
        outputs=[log_display, summary_out, detailed_out]
    )

if __name__ == "__main__":
    demo.launch()
