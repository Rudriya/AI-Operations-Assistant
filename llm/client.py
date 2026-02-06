import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = genai.GenerativeModel("gemini-3-flash-preview")

def call_llm(
    system_prompt: str,
    user_prompt: str,
    temperature: float = 0
) -> str:
    """
    Central Gemini LLM interface for all agents.
    """
    prompt = f"""
{system_prompt}

{user_prompt}
"""

    response = MODEL.generate_content(
        prompt,
        generation_config={
            "temperature": temperature
        }
    )

    return response.text.strip()

if __name__ == "__main__":
    print(
        call_llm(
            "You are a helpful assistant.",
            "Say hello in one word."
        )
    )