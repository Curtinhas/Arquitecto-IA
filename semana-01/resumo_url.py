import anthropic
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

# Carregar a chave
load_dotenv()
cliente = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def extrair_texto(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    resposta = requests.get(url, headers=headers)
    soup = BeautifulSoup(resposta.content, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    return soup.get_text(separator=" ", strip=True)[:3000]
  
def resumir(texto):
    resposta = cliente.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"Resume este texto em 5 pontos principais em Português:\n\n{texto}"
        }]
    )
    return resposta.content[0].text

# Programa principal
url = input("Introduz uma URL: ")
print("\n🔍 A extrair texto...")
texto = extrair_texto(url)
print("🤖 A resumir com IA...")
resumo = resumir(texto)
print("\n📋 RESUMO:\n")
print(resumo)