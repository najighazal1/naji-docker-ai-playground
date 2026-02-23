import os
from anthropic import Anthropic
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

def analyze_code_with_claude(code: str) -> str:
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not set")

    client = Anthropic(api_key=api_key)

    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=500,
        messages=[
            {
                "role": "user",
                "content": f"Analyze this Python code and provide engineering feedback:\n\n{code}"
            }
        ]
    )

    return message.content[0].text
