# rag_chain.py
from ollama_interface import ask_ollama_with_profile

def answer_question(query: str) -> str:
    """
    Answers user query by sending it along with company profile to Ollama.
    """
    return ask_ollama_with_profile(query)
