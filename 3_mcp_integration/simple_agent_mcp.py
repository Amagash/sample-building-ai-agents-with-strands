from strands import Agent
from strands.tools.mcp import MCPClient
from mcp.client.streamable_http import streamablehttp_client

def main():
  mcp_server = MCPClient(lambda: streamablehttp_client('http://127.0.0.1:8080/mcp'))

  print(mcp_server)
  with mcp_server:
    mcp_tools = mcp_server.list_tools_sync()
    agent = Agent(tools=mcp_tools)

    #print available tools
    print(f"Available tools: {[tool.tool_name for tool in mcp_tools]}")

    while True:
      user_input = input("Enter a prompt: ")
      response = agent(user_input)
      print(response)


if __name__ == '__main__':
  main()

