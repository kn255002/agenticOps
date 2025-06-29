# agent_core/parser.py
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Initialize OpenAI client using API key from environment
#https://platform.openai.com/api-keys
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



def parse_task(text):
    prompt = f"""
You are a DevOps assistant. Extract the following from the text:
- username to create
- list of target machines

Text:
{text}

Return JSON in the format:
{{"username": "kn5155638", "machines": ["Tst-vm1", "Tst-vm2"]}}
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return eval(response.choices[0].message.content.strip())
