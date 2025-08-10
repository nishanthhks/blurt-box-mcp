# BlurtBox MCP Server

A custom MCP (Model Context Protocol) server built with FastMCP to send messages to specified usernames. Includes a Dockerized setup for easy deployment. Designed for seamless integration with BlurtBox messaging API.

# Public Usage

```json
"servers": {
  "confluence": {
    "url": "https://blurt-box-mcp.onrender.com/mcp/",
    "type": "http"
  }
}
```

# Project Setup

```bash
# Initialize project
uv init ./

# Create virtual env (if needed)
uv venv

# Activate venv (Win)
.venv\Scripts\activate
# (Mac/Linux)
source .venv/Scripts/activate

# Add dependencies
uv add mcp mcp[cli] requests

# Run and debug MCP server locally
uv run mcp dev main.py
```

# Transport setup:

- **STDIO** (local, editor/CLI integration):
  Run server with
  `uv run --directory ./ main.py`
  Example client config snippet:

  ```json
  "blurtbox message send": {
    "command": "path/to/uv.exe",
    "args": ["run", "--directory", "your/project/path", "main.py"]
  }
  ```

- **Streamable HTTP** (remote/cloud hosting):
  Run server with
  `mcp.run(transport="streamable-http", port=8000)`
  Client config example:

  ```json
  "servers": {
    "confluence": {
      "url": "http://0.0.0.0:8000/mcp/",
      "type": "http"
    }
  }
  ```

  Replace URL with your public domain in production.

# Find paths in (Mac/Linux)

- Check python path: `which python`
- Check uv path: `which uv`
- Current directory: `pwd`


# Note

- STDIO = stdin/stdout communication, no network, local only
- HTTP = full HTTP protocol, for remote or cloud access
- Choose transport based on your use case
- This project uses Onrender vis Docker for deployment
