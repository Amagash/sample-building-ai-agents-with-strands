from strands import Agent
from strands.multiagent.a2a import A2AServer
from strands_tools.current_time import current_time

# Create a Strands agent
strands_agent = Agent(
    name="Current time Agent",
    description="An agent that gives the current time",
    tools=[current_time],
    callback_handler=None
)

# Create A2A server (streaming enabled by default)
a2a_server = A2AServer(agent=strands_agent, port=8001)

# Start the server
a2a_server.serve(host="0.0.0.0", port=8001)