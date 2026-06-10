import requests
from prompts import SYSTEM_PROMPT
from services.contexto_service import obter_contexto

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:20b"

contexto = obter_contexto()

def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    request = requests.post(
        OLLAMA_URL,
          json = {
            "model": MODELO,
            "prompt":  prompt,
            "stream": False
        }
    )
    return request.json()['response']