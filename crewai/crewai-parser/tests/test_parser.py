from src.parser import extract_text_from_pdf

def test_pdf_extract():
    text = extract_text_from_pdf("data/inputs/sample-case.pdf")
    assert "linux" in text.lower()  # simple check
