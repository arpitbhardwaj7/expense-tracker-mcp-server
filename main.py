from fastmcp import FastMCP

mcp = FastMCP(name = "Demo Server")

@mcp.tool
def add_numbers(a: float, b: float) -> float:
    "Add 2 numbers together"
    return a + b

if __name__ == "__main__":
    mcp.run()