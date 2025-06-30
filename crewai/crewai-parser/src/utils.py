# src/utils.py
from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")
