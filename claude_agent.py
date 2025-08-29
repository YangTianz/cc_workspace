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
from claude_code_sdk.types import (
    AssistantMessage,
    ResultMessage,
    TextBlock,
    ToolUseBlock,
)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

SYSTEM_PROMPT = "您是一名资深 Python 开发工程师。"


class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    response: str
    status: str = "success"


@app.get("/health")
async def health_check():
    """健康检查接口"""
    return {"status": "ok", "message": "AI 对话服务运行正常"}


@app.post("/chat")
async def chat(request: ChatRequest):
    """AI 对话接口"""
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="prompt 不能为空")

    print(f"User: {request.prompt}")

    async with ClaudeSDKClient(
        options=ClaudeCodeOptions(
            cwd="/workspace",
            system_prompt=SYSTEM_PROMPT,
            continue_conversation=True,
            permission_mode="acceptEdits",
            extra_args={
                "--timeout": "300",
            },
        )
    ) as client:
        await client.query(request.prompt)
        # 收集AI的响应
        ai_response = ""
        async for message in client.receive_response():
            print(f"Message type: {type(message)}")
            # 处理 AssistantMessage
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, ToolUseBlock):
                        print(f"\n[使用工具：{block.name}]\n")
                    elif isinstance(block, TextBlock):
                        print(block.text, end="", flush=True)
                        ai_response += block.text
            # 处理结果消息
            elif isinstance(message, ResultMessage) and message.result:
                print(f"Result: {message.result}")
                ai_response += message.result

        # 返回AI的完整响应
        return ChatResponse(response=ai_response)


def main() -> None:
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
