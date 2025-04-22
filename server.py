# server.py
from mcp.server.fastmcp import FastMCP
from typing import Union

# Create an MCP server
mcp = FastMCP("Caculator")

# Add an addition tool
@mcp.tool()
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers"""
    return a + b

@mcp.tool()
def sub(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Subtract two numbers"""
    return a - b

@mcp.tool()
def mul(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def div(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Divide two numbers"""
    return a / b

@mcp.tool()
def pow(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Raise a number to the power of another number"""
    return a ** b

@mcp.tool()
def sqrt(a: Union[int, float]) -> Union[int, float]:
    """Square root of a number"""
    return a ** 0.5

@mcp.tool()
def sin(a: Union[int, float]) -> Union[int, float]:
    """Sine of a number"""
    return math.sin(a)

@mcp.tool()
def cos(a: Union[int, float]) -> Union[int, float]: 
    """Cosine of a number"""
    return math.cos(a)

@mcp.tool()
def tan(a: Union[int, float]) -> Union[int, float]:
    """Tangent of a number"""
    return math.tan(a)

@mcp.tool()
def log(a: Union[int, float]) -> Union[int, float]:
    """Logarithm of a number"""
    return math.log(a)

@mcp.tool()
def exp(a: Union[int, float]) -> Union[int, float]:
    """Exponential of a number"""
    return math.exp(a)

@mcp.tool()
def log10(a: Union[int, float]) -> Union[int, float]:
    """Logarithm base 10 of a number"""
    return math.log10(a)

@mcp.tool()
def log2(a: Union[int, float]) -> Union[int, float]:
    """Logarithm base 2 of a number"""
    return math.log2(a)

@mcp.tool()
def log1p(a: Union[int, float]) -> Union[int, float]:
    """Logarithm of 1 plus a number"""
    return math.log1p(a)

@mcp.tool()
def logb(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Logarithm of a number to a base"""
    return math.log(a, b)

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"