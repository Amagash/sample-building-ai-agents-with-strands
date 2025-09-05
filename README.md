# Building AI Agents with Strands

This repository contains a comprehensive tutorial series for building AI agents using the Strands framework, based on the AWS Builder article series.

## Prerequisites

### Installation

1. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

2. **Activate the virtual environment:**
   - **macOS/Linux:** `source .venv/bin/activate`
   - **Windows (CMD):** `.venv\Scripts\activate.bat`
   - **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Tutorial Structure

### [Part 1: Creating Your First Agent](1_strands_basic_agent/)
Learn the fundamentals of creating AI agents with Strands.
- Basic agent creation
- System prompts and behavior
- Interactive conversations

### [Part 2: Tool Integration](2_tools/)
Enhance agents with tools for expanded capabilities.
- Built-in Strands tools
- Custom tool creation
- Tool integration patterns

### [Part 3: MCP Integration](3_mcp_integration/)
Connect agents to external services using Model Context Protocol.
- MCP server creation
- Agent-MCP integration
- Educational quiz system example

### [Part 4: Agent-to-Agent Communication](4_a2a_integration/)
Build distributed multi-agent systems.
- A2A protocol communication
- Agent orchestration
- Specialized agent collaboration

## Quick Start

1. **Clone and setup:**
   ```bash
   git clone <repository-url>
   cd strands-tutorial
   source .venv/bin/activate  # or equivalent for your OS
   ```

2. **Start with Part 1:**
   ```bash
   python 1_strands_basic_agent/simple_agent.py
   ```

3. **Progress through each part** following the README in each directory.

## Reference Articles

This tutorial is based on the AWS Builder article series:
- [Part 1: Creating Your First Agent](https://builder.aws.com/content/2xP1AQ52ofPdLawEbDI5EEUhmhH/building-ai-agents-with-strands-part-1-creating-your-first-agent/)
- [Part 2: Tool Integration](https://builder.aws.com/content/2xP8NYlAQUN0feRpeq9xqhj0i7u/building-ai-agents-with-strands-part-2-tool-integration/)
- [Part 3: MCP Integration](https://builder.aws.com/content/2xSxbxfYzWnaE7eBfvFsKQ62hcv/building-ai-agents-with-strands-part-3-mcp-integration/)

## Support

For issues with the [Strands](https://strandsagents.com/latest/?trk=b8f00cc8-e51d-4bfd-bf44-9b5ffb6acd1a&sc_channel=el) framework itself, refer to the official documentation and GitHub repositories.
