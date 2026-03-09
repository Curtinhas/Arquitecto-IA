import anthropic
from dotenv import load_dotenv
import os

# Carregar a chave de API do ficheiro .env
load_dotenv()
chave = os.getenv("ANTHROPIC_API_KEY")

# Configurar o cliente Anthropic
cliente = anthropic.Anthropic(api_key=chave)

# Fazer a primeira pergunta à IA
resposta = cliente.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Explica o que é inteligência artificial em 3 linhas simples"}
    ]
)

print(resposta.content[0].text)