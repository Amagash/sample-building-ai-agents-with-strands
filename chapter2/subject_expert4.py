import os
import json
from typing import Optional
from strands import Agent, tool
from strands_tools import calculator

# Define a custom tool to manage CS terminology
@tool
def cs_glossary(
    action: str, term: Optional[str] = None, definition: Optional[str] = None
) -> str:
    """
    Manage a glossary of computer science terms.

    Args:
        action: The action to perform: 'lookup', 'add', 'update', or 'list'.
        term: The term to look up, add, or update (not needed for 'list').
        definition: The definition to add or update (not needed for 'lookup' and 'list').
    """
    glossary_file = "cs_glossary.json"

    def load_glossary():
        if not os.path.exists(glossary_file):
            with open(glossary_file, "w") as f:
                json.dump({}, f)
        with open(glossary_file, "r") as f:
            return json.load(f)

    def save_glossary(glossary):
        with open(glossary_file, "w") as f:
            json.dump(glossary, f)

    glossary = load_glossary()

    if action == "lookup":
        if not term:
            return "Error: Term is required for lookup"
        return glossary.get(term, f"Term '{term}' not found in the glossary")

    elif action == "add":
        if not term or not definition:
            return "Error: Both term and definition are required"
        if term in glossary:
            return f"Error: '{term}' already exists. Use 'update' instead."
        glossary[term] = definition
        save_glossary(glossary)
        return f"Added '{term}' to the glossary"

    elif action == "update":
        if not term or not definition:
            return "Error: Both term and definition are required"
        if term not in glossary:
            return f"Error: Term '{term}' not found. Use 'add' instead."
        glossary[term] = definition
        save_glossary(glossary)
        return f"Updated definition for '{term}'"

    elif action == "list":
        if not glossary:
            return "The glossary is empty"
        return "\n".join(f"- {t}" for t in sorted(glossary))

    return f"Error: Unknown action '{action}'. Use 'lookup', 'add', 'update', or 'list'."

# Create an enhanced subject expert agent with multiple tools
subject_expert = Agent(
    system_prompt="""You are a Computer Science Subject Expert specializing
    in explaining technical concepts clearly and concisely. Your expertise
    covers programming languages, data structures, algorithms, computer
    architecture, and software engineering principles.
    
    You can manage a glossary of computer science terms with the cs_glossary tool.
    You can perform calculations with the calculator tool.
    You can read and write files with the file_read and file_write tools.
    
    When explaining concepts:
    1. Start with a clear, concise definition
    2. Check the glossary for any related terms
    3. Add important terms to the glossary if they're not already there
    4. Provide relevant examples to illustrate the concept
    5. Use calculations when appropriate to demonstrate complexity or performance
    
    Your goal is to help learners build a solid understanding of computer
    science fundamentals.
    """,
    tools=[calculator, cs_glossary]
)

def interactive_session():
    print("Computer Science Subject Expert (type 'exit' to quit)")
    print("---------------------------------------------------")
    print("Suggested commands to try:")
    print("- 'Add recursion to the glossary'")
    print("- 'What terms are in the glossary?'")
    print("- 'Explain the time complexity of binary search'")
    
    while True:
        user_input = input("\nYour question: ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break
        
        print("\nThinking...\n")
        response = subject_expert(user_input)
        print(response)

if __name__ == "__main__":
    interactive_session()