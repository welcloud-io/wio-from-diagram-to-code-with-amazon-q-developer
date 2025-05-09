from fastmcp import FastMCP

# Create a FastMCP instance with a simple name
mcp = FastMCP("Simple MCP Server")

@mcp.tool()
def hello(name: str = "World") -> str:
    """Say hello to someone"""
    return f"Hello, {name}!"

@mcp.tool()
def echo(message: str) -> str:
    """Echo back the provided message"""
    return message

if __name__ == "__main__":
    mcp.run()