from strands import Agent
from strands.multiagent.a2a import A2AServer
from pydantic import BaseModel
import uvicorn
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from workshop_utils import A2AClientToolProvider

# Define request model for the inquire endpoint
class InquireRequest(BaseModel):
    question: str

# Create A2AClientToolProvider pointing to the 3 agents
provider = A2AClientToolProvider(known_agent_urls=[
    "http://127.0.0.1:8001",  # Time Agent
    "http://127.0.0.1:8002",  # Calculator Agent
    "http://127.0.0.1:8003"   # Web Agent
])

# Initialize A2A tools using the workshop utils (fixes event loop issues)
a2a_tools = list(provider.tools) if provider else []
print(f"A2A tools available: {[tool.tool_name for tool in a2a_tools]}")

# Create orchestrator agent with A2A client tools and intelligent routing
agent = Agent(
    name="Orchestrator Agent",
    tools=a2a_tools,
    model="us.anthropic.claude-3-5-haiku-20241022-v1:0",
    description="An orchestrator that delegates questions to specialized agents using A2A communication",
    system_prompt="""You are an orchestrator that MUST always delegate ALL questions to specialized agents using A2A communication.

MANDATORY WORKFLOW for EVERY question:
1. FIRST: Use a2a_list_discovered_agents to see available agents
2. THEN: Use a2a_send_message to consult the appropriate agent for the request
3. FINALLY: Return the response from the specialized agent

NEVER answer from your own knowledge without consulting agents first. Always delegate to specialists."""
)

# Create A2A server on port 8009
a2a_server = A2AServer(agent=agent, port=8009)

# Get the FastAPI app from the A2A server
app = a2a_server.to_fastapi_app()

# Add the /inquire endpoint
@app.post("/inquire")
async def inquire(request: InquireRequest):
    """Handle POST requests to /inquire endpoint - let the agent decide routing intelligently"""
    try:
        print(f"Processing question: {request.question}")
        
        # Let the agent handle the question using its A2A tools
        # The agent will automatically use its tools to discover and route to appropriate agents
        response = agent(request.question)
        
        return {"response": response, "status": "success"}
        
    except Exception as e:
        print(f"Error processing request: {e}")
        return {"response": f"Error: {str(e)}", "status": "error"}

# Start the server
if __name__ == "__main__":
    print("Starting Orchestrator Agent on port 8009...")
    print("Available endpoints:")
    print("  POST /inquire - Send questions to be intelligently routed to specialized agents")
    uvicorn.run(app, host="0.0.0.0", port=8009)