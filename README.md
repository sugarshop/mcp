# MCP

## Introduction
    MCP Server Step by Step to integrate utility function into Claude.app, ChatGPT and more MCP Client.

## Execution Steps

1. Initialize the project:
   ```bash
   uv init mcp
   ```

2. Enter the project directory:
   ```bash
   cd mcp
   ```

3. Then add MCP to your project dependencies:
   ```bash
   uv add "mcp[cli]"
   ```

4. Running the standalone MCP development tools:
   ```bash
   uv run mcp install server.py
   ```

## Dependencies
uv installation
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Usage
- install mcp server locally
- change config file to your local uv path:
```bash
which uv
```

## Contribution
If you want others to contribute, provide relevant information here.

## License

[Apache License](http://www.apache.org/licenses/)

Version 2.0, January 2004

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION