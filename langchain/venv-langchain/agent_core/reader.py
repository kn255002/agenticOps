# agent_core/reader.py
from pdfminer.high_level import extract_text

def read_text_file(path):
    with open(path, 'r') as file:
        return file.read()

def read_pdf(path):
    return extract_text(path)
