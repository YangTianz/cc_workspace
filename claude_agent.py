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


@app.get("/")
async def get_prompt(prompt: str):
    print(f"prompt: {prompt}")

    async with ClaudeSDKClient(
        options=ClaudeCodeOptions(
            system_prompt="您是一名性能工程师",
            allowed_tools=["Bash", "Read", "WebSearch"],
            max_turns=5,
        )
    ) as client:
        await client.query(prompt)
        # 收集AI的响应
        ai_response = ""
        async for message in client.receive_response():
            if hasattr(message, "content"):
                for block in message.content:
                    if hasattr(block, "text"):
                        ai_response += block.text
                        print(block.text, end="", flush=True)

        # 返回AI的完整响应
        return {"response": ai_response}


def main() -> None:
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
