import json
import sys
import hashlib

def process_hazard_and_generate_broadcast(input_json: str):
    """
    Processes seismic/thermal data and generates a life-safety broadcast package.
    """
    try:
        data = json.loads(input_json)
        location = data.get("location", "Unknown")
        hazard_type = data.get("hazard_type", "General")
        telemetry = data.get("telemetry", {})

        status = telemetry.get("status", "NORMAL")

        # High-Fidelity Prompt Engineering for Veo (Simulated)
        if hazard_type == "Earthquake":
            veo_prompt = f"1080p aerial cinematic view of {location}, stable evacuation routes highlighted in glowing green, structural risk zones in red pulse, hyper-realistic."
            alert_msg = f"URGENT: Magnitude {telemetry.get('magnitude')} earthquake detected in {location}. Evacuate to open areas immediately."
        elif hazard_type == "Heatwave":
            veo_prompt = f"Thermal heatmap visualization of {location} city streets, cooling centers highlighted, safety advisory overlays, 4K resolution."
            alert_msg = f"HEAT ADVISORY: Temperatures in {location} reaching {telemetry.get('temperature_c')}°C. Seek shade and cooling centers."
        else:
            veo_prompt = "Generic safety visual."
            alert_msg = "Stay alert for environmental updates."

        output = {
            "status": "SUCCESS" if status != "NORMAL" else "MONITORING",
            "alert_message": alert_msg,
            "media_config": {
                "engine": "Veo",
                "prompt": veo_prompt,
                "resolution": "1080p"
            },
            "dispatch_id": hashlib.sha256(alert_msg.encode()).hexdigest()[:16]
        }

        return json.dumps(output)
    except Exception as e:
        print(f"Error in hazard skill: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(process_hazard_and_generate_broadcast(sys.argv[1]))
