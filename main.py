from tools import mcp

if __name__ == "__main__":
    mcp.run(transport="streamable-http")


# # for streaming HTTP requests -> ideal for long-lived connections, streaming data/text
#         mcp.run(transport="streamable-http") 
# # for regular HTTP requests -> ideal for short-lived requests, single interactions, request/response cycles
#         mcp.run(transport="http") 
# # for  standard input/output -> allows for interactive use in a terminal, local integration using text streams
#         mcp.run(transport="stdio")