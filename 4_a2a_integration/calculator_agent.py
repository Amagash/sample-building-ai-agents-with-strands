from strands import Agent
from strands.multiagent.a2a import A2AServer
from strands_tools.calculator import calculator



# Create a Strands agent
strands_agent = Agent(
    name="Calculator Agent",
    description="A calculator agent that can perform basic arithmetic operations.",
    tools=[calculator],
    callback_handler=None
)

# Create A2A server (streaming enabled by default)
a2a_server = A2AServer(agent=strands_agent, port=8002)

# Start the server
a2a_server.serve(host="0.0.0.0", port=8002)