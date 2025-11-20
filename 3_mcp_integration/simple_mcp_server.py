from mcp.server import FastMCP

mcp = FastMCP(
  port=8080
)

@mcp.tool()
def magic_word():
  """say the magic word."""
  return("Banana")
  
if __name__ == "__main__":
  mcp.run(transport="streamable-http")