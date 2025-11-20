from strands import Agent
from strands.multiagent.a2a import A2AServer
from strands_tools import http_request

# Create a Strands agent
strands_agent = Agent(
    name="Web Agent",
    description="An agent that can make http requests to look for information",
    tools=[http_request],
    callback_handler=None
)

# Create A2A server (streaming enabled by default)
a2a_server = A2AServer(agent=strands_agent, port=8003)

# Start the server
a2a_server.serve(host="0.0.0.0", port=8003)