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
    Message,
    ResultMessage,
    SystemMessage,
    TextBlock,
    ToolResultBlock,
    ToolUseBlock,
    UserMessage,
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


def display_message(msg: Message) -> str:
    if isinstance(msg, UserMessage):
        for block in msg.content:
            if isinstance(block, TextBlock):
                print(f"User: {block.text}")
    elif isinstance(msg, AssistantMessage):
        for block in msg.content:
            if isinstance(block, ToolUseBlock):
                print(f"\n[使用工具：{block.name}]\n\t{block.input}\n")
            elif isinstance(block, TextBlock):
                print(block.text, end="", flush=True)
            elif isinstance(block, ToolResultBlock):
                if block.content:
                    print(f"\n[工具结果：{block.content}]\n")
    elif isinstance(msg, SystemMessage):
        # Ignore system messages
        pass
    elif isinstance(msg, ResultMessage):
        print("\n=== 会话结果信息 ===")
        print(f"会话 ID: {msg.session_id}")
        print(f"对话轮数: {msg.num_turns}")
        print(f"总耗时: {msg.duration_ms}ms")
        print(f"API 耗时: {msg.duration_api_ms}ms")
        print(f"错误状态: {'是' if msg.is_error else '否'}")
        if msg.total_cost_usd is not None:
            print(f"费用: ${msg.total_cost_usd:.6f}")
        else:
            print("费用: 未提供")
        if msg.usage:
            print(f"使用量统计: {msg.usage}")
        else:
            print("使用量统计: 未提供")
        print("Result ended")
        return msg.result or ""
    return ""


@app.post("/chat")
async def chat(request: ChatRequest):
    """AI 对话接口"""
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="prompt 不能为空")

    async with ClaudeSDKClient(
        options=ClaudeCodeOptions(
            cwd="/workspace",
            system_prompt=SYSTEM_PROMPT,
            continue_conversation=True,
            permission_mode="acceptEdits",
        )
    ) as client:
        await client.query(request.prompt)
        # 收集AI的响应
        ai_response = ""
        async for message in client.receive_response():
            ai_response = display_message(message)

        return ChatResponse(response=ai_response)


def main() -> None:
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
