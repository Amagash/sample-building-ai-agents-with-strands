# Building AI Agents with Strands - Part 1: Creating Your First Agent

This directory contains examples from the AWS Builder article: [Building AI Agents with Strands - Part 1: Creating Your First Agent](https://builder.aws.com/content/2xP1AQ52ofPdLawEbDI5EEUhmhH/building-ai-agents-with-strands-part-1-creating-your-first-agent/?trk=b8f00cc8-e51d-4bfd-bf44-9b5ffb6acd1a&sc_channel=ellis)

## Overview

This section demonstrates the fundamentals of creating AI agents using the Strands framework. You'll learn how to build simple agents that can process user input and provide intelligent responses.

## Files

### `simple_agent.py`
A basic Strands agent implementation that demonstrates:
- Creating an agent with a specific model (Claude Haiku)
- Setting up system prompts for agent behavior
- Running the agent with user input

### `interactive_agent.py`
An enhanced version that shows:
- Interactive conversation loops
- User input handling
- Graceful exit mechanisms

## Getting Started

1. **Run the Simple Agent**
   ```bash
   python 1_strands_basic_agent/simple_agent.py
   ```

2. **Try the Interactive Agent**
   ```bash
   python 1_strands_basic_agent/interactive_agent.py
   ```

## Key Concepts

- **Agent Creation**: Using the `Agent` class to create AI agents
- **Model Configuration**: Specifying which LLM to use (Claude Haiku in this case)
- **System Prompts**: Defining agent behavior and personality
- **User Interaction**: Processing and responding to user input

## Next Steps

After mastering basic agents, explore:
- **Part 2**: Adding tools to agents (see `2_tools/`)
- **Part 3**: MCP integration (see `3_mcp_integration/`)
- **Part 4**: Agent-to-Agent communication (see `4_a2a_integration/`)

## Reference

This code is based on the AWS Builder article series on building AI agents with Strands. For detailed explanations and additional context, refer to the original article linked above.