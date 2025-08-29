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
    ToolResultBlock,
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
        )
    ) as client:
        await client.query(request.prompt)
        # 收集AI的响应
        ai_response = ""
        async for message in client.receive_response():
            # 处理 AssistantMessage
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, ToolUseBlock):
                        print(f"\n[使用工具：{block.name}]\n\t{block.input}\n")
                    elif isinstance(block, TextBlock):
                        print(block.text, end="", flush=True)
                    elif isinstance(block, ToolResultBlock):
                        if block.content:
                            print(f"\n[工具结果：{block.content}]\n")

            elif isinstance(message, ResultMessage):
                print("\n=== 会话结果信息 ===")
                print(f"会话 ID: {message.session_id}")
                print(f"对话轮数: {message.num_turns}")
                print(f"总耗时: {message.duration_ms}ms")
                print(f"API 耗时: {message.duration_api_ms}ms")
                print(f"错误状态: {'是' if message.is_error else '否'}")
                if message.total_cost_usd is not None:
                    print(f"费用: ${message.total_cost_usd:.6f}")
                else:
                    print("费用: 未提供")
                if message.usage:
                    print(f"使用量统计: {message.usage}")
                else:
                    print("使用量统计: 未提供")
                if message.result:
                    ai_response += message.result

        # 返回AI的完整响应
        return ChatResponse(response=ai_response)


def main() -> None:
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
