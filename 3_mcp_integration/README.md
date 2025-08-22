# Building AI Agents with Strands - Part 3: MCP Integration

This directory contains examples from the AWS Builder article: [Building AI Agents with Strands - Part 3: MCP Integration](https://builder.aws.com/content/2xSxbxfYzWnaE7eBfvFsKQ62hcv/building-ai-agents-with-strands-part-3-mcp-integration/?trk=b8f00cc8-e51d-4bfd-bf44-9b5ffb6acd1a&sc_channel=el)

## Overview

This section demonstrates how to integrate Model Context Protocol (MCP) servers with Strands agents. MCP enables agents to access external services and data sources through standardized protocols, greatly expanding their capabilities.

## Files

### `mcp_server.py`
A Computer Science Quiz MCP server that provides:
- **Quiz Topics**: Python basics, data structures, and more
- **Quiz Retrieval**: Get questions and answers for specific topics
- **Topic Listing**: Discover available quiz categories
- **HTTP Server**: Serves MCP protocol over HTTP

### `agent_with_mcp.py`
A Computer Science Subject Expert agent that:
- **Connects to Quiz MCP Server**: Uses external quiz service
- **Interactive Learning**: Conducts quiz sessions with students
- **Answer Checking**: Grades student responses automatically
- **Educational Feedback**: Provides explanations and encouragement

## Getting Started

1. **Start the MCP Server**
   ```bash
   python 3_mcp_integration/mcp_server.py
   ```
   The server will start on `http://localhost:8080/mcp`

2. **Run the Agent with MCP**
   In a separate terminal:
   ```bash
   python 3_mcp_integration/agent_with_mcp.py
   ```

## Key Concepts

- **Model Context Protocol (MCP)**: Standardized protocol for connecting AI models to external services
- **MCP Servers**: Services that expose tools and resources via MCP
- **MCP Clients**: Components that connect to and use MCP servers
- **Tool Discovery**: Automatic discovery of available MCP tools
- **Protocol Communication**: JSON-RPC based communication between clients and servers

## Example Interactions

With the MCP quiz server, you can ask:
- "What quiz topics are available?"
- "Give me a Python quiz"
- "I want to test my knowledge of data structures"

The agent will use the MCP quiz service to provide interactive learning experiences with real questions and automated grading.

## MCP Architecture

```
┌─────────────────┐    MCP Protocol    ┌─────────────────┐
│   CS Subject    │◄──────────────────►│   Quiz MCP      │
│   Expert Agent  │    (JSON-RPC)      │   Server        │
│   + MCP Client  │                    │                 │
└─────────────────┘                    └─────────────────┘
```

## Benefits of MCP Integration

1. **Standardization**: Common protocol for tool integration
2. **Modularity**: Separate services can be developed independently
3. **Scalability**: Multiple agents can share the same MCP servers
4. **Flexibility**: Easy to add new capabilities without modifying agents
5. **Interoperability**: MCP servers can be used across different AI frameworks

## Creating Custom MCP Servers

To create your own MCP server:

1. **Define Tools**: Create functions that perform specific tasks
2. **Implement Protocol**: Handle MCP JSON-RPC messages
3. **Expose HTTP Endpoint**: Serve the MCP protocol over HTTP
4. **Register Tools**: Make tools discoverable by MCP clients

## Next Steps

After mastering MCP integration, explore:
- **Part 4**: Agent-to-Agent communication (see `4_a2a_integration/`)
- **Advanced MCP**: File system access, database connections, API integrations

## Reference

This code is based on the AWS Builder article series on building AI agents with Strands. For detailed explanations and additional context, refer to the original article linked above.