from src.agent import analyze_text

def test_agent_output():
    text = "Create a Linux user kn5155638 on Tst-vm1, Tst-vm2."
    result = analyze_text(text)
    assert "kn5155638" in result
