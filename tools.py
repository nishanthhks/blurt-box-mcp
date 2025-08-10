from mcp.server.fastmcp import FastMCP

import requests
import json  

# mcp server instance
mcp = FastMCP("BlurtBox",host="0.0.0.0", port=8000)

@mcp.tool("send message <message> to a particular username <username>")
def send(message: str, username: str) -> dict:
    """
        context: Sends a message to a specific username using the BlurtBox API.
    """
    try:
        res = requests.post(
            "https://blurtbox.vercel.app/api/send-message",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"content": message, "username": username})
        )

        # parse json to dict
        data = res.json()

        # response check -> status code
        if res.status_code != 200:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": f"Error: {data.get('message', 'An error occurred, message not sent')}"
                    }
                ]
            }

        # if positive response
        return {
            "content": [
                {
                    "type": "text",
                    "text": data.get("message", f"Message from {username}: {message}")
                }
            ]
        }

    except Exception as e:
        # network error, unable to reach API
        return {
            "content": [
                {
                    "type": "text",
                    "text": f"An error occurred, message not sent: {str(e)}"
                }
            ]
        }
