import ipywidgets as widgets
from IPython.display import display, HTML
import time

def run_sensi_map_enabled_cli():
    """
    Enhanced Sensi Terminal with Dynamic Map Visualization.
    """
    # 1. Terminal & Map CSS
    terminal_css = """
    <style>
        .sensi-term-v2 {
            background-color: #050505 !important;
            color: #00FF00 !important;
            font-family: 'Courier New', Courier, monospace !important;
            padding: 20px !important;
            border-radius: 10px !important;
            border: 2px solid #3b82f6 !important;
            height: 450px !important;
            overflow-y: auto !important;
            font-size: 15px !important;
            font-weight: bold !important;
        }
        .sensi-map-overlay {
            border: 2px solid #FF4500;
            border-radius: 5px;
            margin-top: 10px;
            width: 100%;
            max-width: 500px;
        }
        .alert-banner {
            background-color: #FF4500;
            color: white;
            padding: 5px;
            text-align: center;
            font-weight: bold;
            margin-top: 5px;
        }
    </style>
    """
    display(HTML(terminal_css))

    output = widgets.Output()
    output.add_class("sensi-term-v2")

    input_field = widgets.Text(
        placeholder='Type "triage" to see the map alert...',
        description='<b style="color: #3b82f6;">CMD:</b>',
        layout=widgets.Layout(width='100%', margin='10px 0 0 0')
    )

    def print_line(text, color="#00FF00"):
        with output:
            display(HTML(f"<div style='color: {color}; margin-bottom: 3px;'>{text}</div>"))

    def show_map_alert(sector):
        with output:
            # Simulated dynamic map coordinates
            lat, lon = "24.86", "67.00"
            map_url = f"https://api.mapbox.com/styles/v1/mapbox/dark-v10/static/pin-s-l+ff0000({lon},{lat})/{lon},{lat},13,0/600x300?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTAwMTYycXBndWRtcXFwZ3MifQ=="

            display(HTML(f"""
                <div class="alert-banner">🚨 CRITICAL ALERT: {sector} ZONE COMPROMISED</div>
                <img src="{map_url}" class="sensi-map-overlay" alt="Crisis Map">
                <div style="color: #FF4500; font-size: 12px;">Satellite Lock: {lat}N, {lon}E | Status: FLOODING_DETECTED</div>
            """))

    def handle_command(sender):
        cmd = input_field.value.strip().lower()
        input_field.value = ''
        with output:
            display(HTML(f"<div style='color: #3b82f6; border-top: 1px solid #333; padding-top: 5px;'><b>> {cmd}</b></div>"))
            if cmd == "triage":
                print_line("[SYSTEM] Orchestrating Crisis Response...", "#FFD700")
                time.sleep(0.5)
                print_line("[LOGISTICS] Fetching MCP Geodata...", "#00FF00")
                time.sleep(0.8)

                # Dynamic Map Alert Display
                show_map_alert("SECTOR 7")

                time.sleep(0.5)
                print_line("[COMMS] Visualizing evacuation paths on local network...", "#00BFFF")
                time.sleep(0.5)
                print_line("[GUARD] Security Check: OK", "#32CD32")
                print_line("STATUS: DEPLOYED", "#32CD32")

            elif cmd == "status":
                print_line("AGENT_NODES: 3 ACTIVE", "#00FF00")
                print_line("MAP_ENGINE: READY", "#00FF00")
            elif cmd == "clear":
                output.clear_output()
            elif cmd == "help":
                print_line("Commands: triage, status, clear, help", "#00BFFF")
            else:
                print_line(f"Unknown: {cmd}", "#FF4500")

    input_field.on_submit(handle_command)
    display(HTML("<h2 style='color: #3b82f6;'>🛰️ Sensi Map-Enabled Command Center</h2>"), output, input_field)
    print_line("Project Sensi Terminal v1.1.0 (Map Engine: ON)", "#00FF00")

if __name__ == "__main__":
    run_sensi_map_enabled_cli()
