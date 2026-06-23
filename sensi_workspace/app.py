import gradio as gr
import json
import os
import sys

# Ensure imports work from project root
sys.path.append(os.path.abspath(os.getcwd()))

from sensi_workspace.agents.orchestrator import SensiOrchestrator

orchestrator = SensiOrchestrator()

def run_triage(intent, sector):
    result = orchestrator.process_intent(intent, sector)

    log_output = "\n".join(result["logs"])

    if result["status"] == "SUCCESS":
        media = result["media"]
        dispatch = result["dispatch"]

        status_md = f"### ✅ Dispatch Successful\n**Signed Hash:** `{dispatch['signed_hash']}`"

        media_md = "#### 🎬 Generated Media Assets\n"
        for m in media:
            icon = "📹" if m["type"] == "video" else "🖼️"
            media_md += f"- {icon} [{m['type'].capitalize()}]({m['url']}) - {m.get('resolution', 'N/A')}\n"

        broadcast_md = f"#### 📢 Broadcast Payload\n> {dispatch['payload_delivered']}"

        return log_output, status_md, media_md, broadcast_md
    else:
        return log_output, "### ❌ Dispatch Failed", "", ""

# Custom CSS for a "Crisis Command Center" vibe
custom_css = """
.gradio-container { background-color: #0b0f19; color: #e0e6ed; }
.main-header { text-align: center; color: #3b82f6; }
.log-box { font-family: 'Courier New', Courier, monospace; background-color: #111827; border: 1px solid #1f2937; }
"""

with gr.Blocks(css=custom_css, theme=gr.themes.Soft(primary_hue="blue", neutral_hue="slate")) as demo:
    gr.Markdown("# 🛰️ Project Sensi: Crisis Command Center", elem_classes=["main-header"])
    gr.Markdown("### Autonomous Multi-Agent Triage & Response System")

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("#### 📥 Command Input")
            intent_input = gr.Textbox(
                label="Natural Language Intent",
                placeholder="e.g., Coordinate emergency advisory for Sector 7",
                value="Coordinate emergency advisory for Sector 7"
            )
            sector_input = gr.Dropdown(
                choices=["Sector 7", "Sector 3", "Sector 12"],
                label="Target Jurisdiction",
                value="Sector 7"
            )
            submit_btn = gr.Button("🚀 Trigger Autonomous Pipeline", variant="primary")

            gr.Markdown("#### 🛡️ Security Status")
            gr.Markdown("- **MCP Sandboxing:** ACTIVE\n- **Guard Node Monitoring:** ACTIVE\n- **Cryptographic Signing:** ENABLED")

        with gr.Column(scale=2):
            gr.Markdown("#### 📟 System Runtime Logs")
            log_display = gr.Textbox(label="", interactive=False, lines=12, elem_classes=["log-box"])

    with gr.Row():
        with gr.Column():
            status_out = gr.Markdown()
        with gr.Column():
            broadcast_out = gr.Markdown()

    with gr.Row():
        media_out = gr.Markdown()

    submit_btn.click(
        fn=run_triage,
        inputs=[intent_input, sector_input],
        outputs=[log_display, status_out, media_out, broadcast_out]
    )

if __name__ == "__main__":
    demo.launch()
