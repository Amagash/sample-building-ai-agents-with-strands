from strands import Agent

# Create an agent with OpenAI (you'll need to set OPENAI_API_KEY environment variable)
# or use another provider like Anthropic, Ollama, etc.
agent = Agent()

# Ask a question
response = agent("Tell me about agentic AI")