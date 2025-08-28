# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "claude-code-sdk",
#     "fastapi",
#     "uvicorn",
#     "openai",
# ]
# ///

import os
from fastapi import FastAPI
from openai import OpenAI

app = FastAPI()

client = OpenAI(
    base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.openai.com/v1"),
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

@app.get("/")
def get_prompt(prompt: str):
    print(f"prompt: {prompt}")
    
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user", "content": prompt}
            ],
            stream=True
        )
        
        print("AI response: ", end="", flush=True)
        ai_output = ""
        
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                print(content, end="", flush=True)
                ai_output += content
        
        print()  # 换行
        
        return {"prompt": prompt, "ai_response": ai_output}
        
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return {"prompt": prompt, "error": str(e)}

def main() -> None:
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
