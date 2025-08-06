from strands import Agent

# Create an agent with OpenAI (you'll need to set OPENAI_API_KEY environment variable)
# or use another provider like Anthropic, Ollama, etc.
agent = Agent(
    model="openai:gpt-4o-mini",  # or "anthropic:claude-3-haiku" or "ollama:llama3.2"
)

# Ask a question
agent("Tell me about agentic AI")