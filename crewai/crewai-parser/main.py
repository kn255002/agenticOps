# main.py
from src.parser import extract_text_from_pdf
from src.agent import analyze_text
import json
import os

pdf_path = "data/inputs/sample-case.pdf"

if __name__ == "__main__":
    raw_text = extract_text_from_pdf(pdf_path)
    print("🔍 Extracted text:\n", raw_text)

    structured_output = analyze_text(raw_text)

    with open("data/outputs/structured_output.json", "w") as f:
        f.write(structured_output)

    print("✅ Saved structured output to data/outputs/structured_output.json")
