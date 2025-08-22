# Building AI Agents with Strands - Part 4: Agent-to-Agent Communication

This directory demonstrates advanced agent orchestration using Agent-to-Agent (A2A) communication in the Strands framework. Learn how to build distributed agent systems where specialized agents collaborate to solve complex tasks.

## Overview

This section shows how to create a multi-agent system where an orchestrator agent delegates tasks to specialized agents. Each agent focuses on a specific domain, and they communicate using the A2A protocol to provide comprehensive solutions.

## Files

### `orchestrator_agent.py`
The main orchestrator that:
- **Receives user queries** via HTTP endpoint (`/inquire`)
- **Discovers available agents** using A2A tools
- **Routes questions intelligently** to appropriate specialized agents
- **Returns responses** from the specialized agents

### `time_agent.py`
A specialized agent that handles:
- **Current time queries**: "What time is it?"
- **Date information**: "What's today's date?"
- **Time-related calculations**: Time zones, scheduling

### `calculator_agent.py`
A mathematical specialist that provides:
- **Basic arithmetic**: Addition, subtraction, multiplication, division
- **Complex calculations**: Advanced mathematical operations
- **Numerical analysis**: Statistical calculations

### `web_agent.py`
An internet-enabled agent for:
- **Web searches**: General internet queries
- **Wikipedia lookups**: Encyclopedia information
- **URL content retrieval**: Fetching web page content

### `utils.py`
Workshop utilities that provide:
- **A2A Client Tools**: Patched A2A communication tools
- **Message Format Handling**: Correct JSON-RPC message structure
- **Event Loop Compatibility**: Fixes for FastAPI/uvicorn integration

## Getting Started

1. **Start the Specialized Agents**
   In separate terminals:
   ```bash
   python 4_a2a_integration/time_agent.py      # Port 8001
   python 4_a2a_integration/calculator_agent.py # Port 8002
   python 4_a2a_integration/web_agent.py       # Port 8003
   ```

2. **Start the Orchestrator**
   ```bash
   python 4_a2a_integration/orchestrator_agent.py # Port 8009
   ```

3. **Test the System**
   Using curl:
   ```bash
   curl -X POST http://127.0.0.1:8009/inquire \
     -H "Content-Type: application/json" \
     -d '{"question": "What time is it?"}'
   ```
   
   Or use the provided `test.http` file with your HTTP client (VS Code REST Client, IntelliJ HTTP Client, etc.)

## Key Concepts

- **Agent-to-Agent (A2A) Protocol**: JSON-RPC based communication between agents
- **Orchestration**: Central coordination of multiple specialized agents
- **Intelligent Routing**: Automatic delegation based on question analysis
- **Distributed Architecture**: Each agent runs as an independent service
- **Specialization**: Agents focused on specific domains for better performance

## System Architecture

```
┌─────────────────┐    HTTP POST     ┌─────────────────┐
│     Client      │─────────────────►│  Orchestrator   │
│                 │                  │   Agent :8009   │
└─────────────────┘                  └─────────┬───────┘
                                               │ A2A
                              ┌────────────────┼────────────────┐
                              │                │                │
                              ▼                ▼                ▼
                    ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
                    │   Time Agent    │ │ Calculator Agent│ │   Web Agent     │
                    │     :8001       │ │     :8002       │ │     :8003       │
                    └─────────────────┘ └─────────────────┘ └─────────────────┘
```

## Example Interactions

**Time Queries:**
- "What time is it?"
- "What's today's date?"

**Mathematical Operations:**
- "Calculate 15 * 23 + 7"
- "What's the square root of 144?"

**Web Searches:**
- "Look up information about Python programming"
- "Search Wikipedia for the history of AI"

## A2A Communication Flow

1. **Client Request**: User sends question to orchestrator
2. **Agent Discovery**: Orchestrator discovers available agents
3. **Question Analysis**: Orchestrator analyzes the question type
4. **Agent Selection**: Routes to most appropriate specialized agent
5. **A2A Communication**: Sends question using A2A protocol
6. **Response Processing**: Receives and returns specialist's response

## Benefits of A2A Architecture

1. **Modularity**: Each agent can be developed and deployed independently
2. **Scalability**: Easy to add new specialized agents
3. **Fault Tolerance**: System continues working if some agents are unavailable
4. **Specialization**: Each agent optimized for specific tasks
5. **Load Distribution**: Work distributed across multiple agents

## Troubleshooting

**Common Issues:**
- **Port conflicts**: Ensure each agent uses a unique port
- **Agent discovery**: Check that specialized agents are running before starting orchestrator
- **Message format**: The `utils.py` file handles A2A message format compatibility

## Advanced Features

- **Dynamic Agent Discovery**: Orchestrator automatically finds available agents
- **Intelligent Routing**: No hardcoded routing logic - agents decide based on context
- **Error Handling**: Graceful handling of agent unavailability
- **HTTP Integration**: RESTful API for easy client integration

## Next Steps

- **Scale the System**: Add more specialized agents (database, file system, etc.)
- **Implement Load Balancing**: Distribute work across multiple instances
- **Add Authentication**: Secure agent communication
- **Monitor Performance**: Add logging and metrics

## Reference

This implementation demonstrates advanced multi-agent patterns using the Strands framework, building upon the concepts from the previous parts of this tutorial series.