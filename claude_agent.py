# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "claude-code-sdk",
#     "fastapi",
#     "uvicorn",
#     "openai",
# ]
# ///


from claude_code_sdk import ClaudeCodeOptions, ClaudeSDKClient
from fastapi import FastAPI

app = FastAPI()

ALLOWED_TOOLS: list[str] = ["Bash", "Read", "Write", "WebSearch", "Grep"]
DISALLOWED_TOOLS: list[str] = ["Bash(rm*)"]
SYSTEM_PROMPT = "您是一名资深 Python 开发工程师。"

@app.get("/")
async def get_prompt(prompt: str):
    print(f"User: {prompt}")

    async with ClaudeSDKClient(
        options=ClaudeCodeOptions(
            cwd="/workspace/repo",
            system_prompt=SYSTEM_PROMPT,
            continue_conversation=True,
            allowed_tools=ALLOWED_TOOLS,
            disallowed_tools=DISALLOWED_TOOLS,
            permission_mode="acceptEdits",
            extra_args={
                "--verbose": None,
                "--timeout": "300",
            },
        )
    ) as client:
        await client.query(prompt)
        # 收集AI的响应
        ai_response = ""
        async for message in client.receive_response():
            print(type(message))
            if hasattr(message, "content"):
                for block in message.content:
                    if hasattr(block, "type"):
                        if block.type == "tool_use":
                            print(f"\n[使用工具：{block.name}]\n")
                        elif hasattr(block, "text"):
                            print(block.text, end="", flush=True)
                    elif hasattr(block, "text"):
                        print(block.text, end="", flush=True)

        # 返回AI的完整响应
        return {"response": ai_response}


def main() -> None:
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
