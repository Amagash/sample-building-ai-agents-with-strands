# Strands already includes MCP, no additional install required
from mcp.server import FastMCP

# Create an MCP server
mcp = FastMCP(
    name="Computer Science Quiz Service",
    host="0.0.0.0",
    port=8080
)

# Quiz database
QUIZ_CATALOG = {
    "python_basics": {
        "title": "Python Programming Fundamentals",
        "questions": [
            {
                "question": "What keyword is used to define a function in Python?",
                "options": ["func", "def", "function", "define"],
                "correct_answer": "def"
            },
            {
                "question": "Which of these creates a list in Python?",
                "options": ["(1, 2, 3)", "{1, 2, 3}", "[1, 2, 3]", "<1, 2, 3>"],
                "correct_answer": "[1, 2, 3]"
            }
        ]
    },
    "data_structures": {
        "title": "Data Structures Essentials",
        "questions": [
            {
                "question": "What is the time complexity of accessing an element in an array by index?",
                "options": ["O(n)", "O(log n)", "O(1)", "O(n²)"],
                "correct_answer": "O(1)"
            }
        ]
    }
}

@mcp.tool()
def list_quiz_topics() -> dict:
    """List all available quiz topics."""
    topics = {}
    for topic_id, quiz_data in QUIZ_CATALOG.items():
        topics[topic_id] = {
            "title": quiz_data["title"],
            "question_count": len(quiz_data["questions"])
        }
    return {"available_topics": topics}

@mcp.tool()
def get_quiz_for_topic(topic: str) -> dict:
    """Retrieve a quiz for a specific topic."""
    if topic.lower() not in QUIZ_CATALOG:
        return {
            "error": f"Topic '{topic}' not found",
            "available_topics": list(QUIZ_CATALOG.keys())
        }
    
    return QUIZ_CATALOG[topic.lower()]

# Start the MCP server
if __name__ == "__main__":
    mcp.run(transport="streamable-http")

from mcp.server import FastMCP

mcp = FastMCP(
    port="8080"
)

@mcp.tool()
def magic_word():
  """say the magic word."""
  return("Banana")

if __name__ == "__main__":
  mcp.run(transport="streamable-http")