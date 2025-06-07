# ollama_interface.py
import subprocess
from config import OLLAMA_MODEL_NAME, COMPANY_PROFILE_PATH

# Load company profile once on module load
with open(COMPANY_PROFILE_PATH, 'r', encoding='utf-8') as f:
    COMPANY_PROFILE = f.read()


def ask_ollama(prompt: str) -> str:
    """
    Calls Ollama CLI with the given prompt via stdin and returns the output string.
    """
    command = ['ollama', 'run', OLLAMA_MODEL_NAME]
    result = subprocess.run(command, input=prompt, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Ollama error: {result.stderr}")

    return result.stdout.strip()


def ask_ollama_with_profile(question: str) -> str:
    """
    Prepends company profile to the question and sends to Ollama.
    """
    full_prompt = f"{COMPANY_PROFILE}\n\nQuestion: {question}"
    return ask_ollama(full_prompt)
