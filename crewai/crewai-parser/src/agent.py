# src/agent.py
from openai import OpenAI
from src.utils import load_env

def analyze_text(text: str) -> dict:
    api_key = load_env()
    client = OpenAI(api_key=api_key)

    prompt = f"""Extract this information:
    - Task Type (create/delete user)
    - Username(s)
    - Target Hostnames

    From this input:\n{text}
    Respond in JSON format.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content
