# Building AI Agents with Strands - Part 2: Tool Integration

This directory contains examples from the AWS Builder article: [Building AI Agents with Strands - Part 2: Tool Integration](https://builder.aws.com/content/2xP8NYlAQUN0feRpeq9xqhj0i7u/building-ai-agents-with-strands-part-2-tool-integration/?trk=b8f00cc8-e51d-4bfd-bf44-9b5ffb6acd1a&sc_channel=el)

## Overview

This section demonstrates how to enhance AI agents with tools, enabling them to perform specific actions beyond text generation. You'll learn how to integrate both built-in Strands tools and create custom tools for your agents.

## Files

### `built_in_tools.py`
Demonstrates the use of built-in Strands tools:
- **Current Time Tool**: Get the current date and time
- **Web Search Tool**: Search the internet for information
- **Calculator Tool**: Perform mathematical calculations
- Shows how to add multiple tools to a single agent

### `custom_tools.py`
Shows how to create and integrate custom tools:
- **Custom Tool Creation**: Using the `@tool` decorator
- **Function Parameters**: Defining tool inputs with type hints
- **Tool Documentation**: Adding descriptions for better agent understanding
- **Integration**: Adding custom tools to agents

## Getting Started

1. **Run Built-in Tools Example**
   ```bash
   python 2_tools/built_in_tools.py
   ```

2. **Try Custom Tools Example**
   ```bash
   python 2_tools/custom_tools.py
   ```

## Key Concepts

- **Tool Integration**: Adding functionality to agents beyond text generation
- **Built-in Tools**: Using pre-built tools from the `strands-tools` package
- **Custom Tools**: Creating your own tools with the `@tool` decorator
- **Tool Parameters**: Defining inputs and outputs for tools
- **Agent Enhancement**: How tools expand agent capabilities

## Example Interactions

With built-in tools, you can ask:
- "What time is it?"
- "Calculate 15 * 23"
- "Search for information about Python programming"

With custom tools, you can create specialized functionality:
- Domain-specific calculations
- API integrations
- File operations
- Database queries

## Tool Best Practices

1. **Clear Descriptions**: Write descriptive tool documentation
2. **Type Hints**: Use proper Python type hints for parameters
3. **Error Handling**: Handle edge cases gracefully
4. **Focused Functionality**: Keep tools focused on specific tasks

## Next Steps

After mastering tool integration, explore:
- **Part 3**: MCP (Model Context Protocol) integration (see `3_mcp_integration/`)
- **Part 4**: Agent-to-Agent communication (see `4_a2a_integration/`)

## Reference

This code is based on the AWS Builder article series on building AI agents with Strands. For detailed explanations and additional context, refer to the original article linked above.