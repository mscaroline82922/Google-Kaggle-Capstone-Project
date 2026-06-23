from google import adk
from pydantic import BaseModel, Field
from typing import List, Optional
import json

# --- Models ---

class LogisticsRequest(BaseModel):
    coordinates: str = Field(..., description="GPS coordinates or Sector name")

class BroadcastRequest(BaseModel):
    zone: str
    urgency: str
    message: str

# --- Agents ---

# Logistics Agent: Specialist for environmental ingestion
logistics_agent = adk.Agent(
    name="Logistics Agent",
    instructions="""You are a specialist in environmental data and supply chain logistics.
    Use the MCP server to fetch satellite deltas and query inventory databases.
    Provide concise summaries of structural integrity and resource availability.""",
    # Tools will be added during orchestration if needed, or defined globally
)

# Comms/Media Agent: Specialist for procedural skill memory and media generation
comms_agent = adk.Agent(
    name="Comms/Media Agent",
    instructions="""You are a specialist in emergency communications and media generation.
    You map telemetry data to visual and textual broadcast packages.
    Use the broadcast_generation skill to create 1080p evacuation visuals.""",
)

# Sensi Orchestrator: Topology Layer
sensi_orchestrator = adk.Agent(
    name="Sensi Orchestrator",
    instructions="""You are the central coordinator for Project Sensi.
    1. Accept natural language intent.
    2. Delegate environmental analysis to the Logistics Agent.
    3. Delegate broadcast generation to the Comms/Media Agent.
    4. Ensure self-healing checks are performed by the Security Guard Node (runtime).""",
    agents=[logistics_agent, comms_agent]
)

if __name__ == "__main__":
    # This would typically be run via the ADK CLI or a main script
    print("Sensi Orchestrator initialized.")
