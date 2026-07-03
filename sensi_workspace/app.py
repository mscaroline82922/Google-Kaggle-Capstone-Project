import gradio as gr
import json
import os
import sys

# Ensure imports work
sys.path.append(os.path.abspath(os.getcwd()))

from sensi_workspace.agents.orchestrator import SensiHazardOrchestrator

orchestrator = SensiHazardOrchestrator()

def run_hazard_monitor(location, hazard_type):
    result = orchestrator.analyze_hazard(location, hazard_type)

    log_display = "\n".join(result["logs"])

    if result["status"] == "DISPATCHED":
        output = result["output"]
        dispatch = result["dispatch"]
        status_md = f"### 🚨 {hazard_type.upper()} ALERT DISPATCHED\n**Target:** {location}\n**Signature:** `{dispatch['signed_hash']}`"
        msg_md = f"#### 📢 Broadcast Message\n> {output['alert_message']}"
        media_md = f"#### 🎬 GenMedia Visual (Veo)\n- **Prompt:** {output['media_config']['prompt']}\n- **Resolution:** 1080p"
        return log_display, status_md, msg_md, media_md
    elif result["status"] == "MONITORING":
        status_md = f"### 🟢 System Status: MONITORING\nNo critical {hazard_type} thresholds exceeded in {location}."
        return log_display, status_md, "", ""
    else:
        return log_display, "### ❌ System Failure", "", ""

custom_css = """
.gradio-container { background-color: #0d1117; color: #c9d1d9; }
.hazard-header { text-align: center; color: #ff7b72; }
.log-box { font-family: 'Courier New', monospace; background-color: #161b22; border: 1px solid #30363d; }
"""

with gr.Blocks(css=custom_css, theme=gr.themes.Default(primary_hue="red", neutral_hue="slate")) as demo:
    gr.Markdown("# 🛰️ Project Sensi: Global Hazard Monitor", elem_classes=["hazard-header"])
    gr.Markdown("### Autonomous Life-Safety Prediction & Response System")

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("#### 📥 Mission Parameters")
            loc_input = gr.Textbox(label="Target Location", value="Japan")
            hazard_input = gr.Dropdown(choices=["Earthquake", "Heatwave"], value="Earthquake", label="Hazard Type")
            submit_btn = gr.Button("⚡ Trigger Prediction Loop", variant="primary")

            gr.Markdown("#### 🛡️ Resilience Layers")
            gr.Markdown("- **Guard Node:** ACTIVE\n- **MCP Sandboxing:** ACTIVE\n- **Self-Healing:** ENABLED")

        with gr.Column(scale=2):
            gr.Markdown("#### 📟 Live Runtime Logs")
            log_out = gr.Textbox(label="", interactive=False, lines=15, elem_classes=["log-box"])

    with gr.Row():
        with gr.Column():
            status_out = gr.Markdown()
        with gr.Column():
            msg_out = gr.Markdown()

    with gr.Row():
        media_out = gr.Markdown()

    submit_btn.click(
        fn=run_hazard_monitor,
        inputs=[loc_input, hazard_input],
        outputs=[log_out, status_out, msg_out, media_out]
    )

if __name__ == "__main__":
    demo.launch()
