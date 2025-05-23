import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

# Lê a URL base do .env
SCRAP_URL = os.getenv("SCRAP_URL")
PAGES_TO_SCRAPE = 5

def scrap_books(pages=PAGES_TO_SCRAPE):
    livros = []

    for page in range(1, pages + 1):
        page_url = f"{SCRAP_URL}catalogue/category/books_1/page-{page}.html"
        print(f"🌐 Acessando página {page}: {page_url}")

        response = requests.get(page_url)
        response.encoding = 'utf-8'  # força leitura correta de caracteres especiais

        if response.status_code != 200:
            print(f"❌ Erro ao acessar a página {page}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.select('article.product_pod')

        for item in items:
            titulo = item.h3.a['title']

            # Corrige possíveis problemas de codificação no preço
            preco_raw = item.select_one('.price_color').text
            preco = preco_raw.replace('Â', '').strip()

            # Trata a imagem
            imagem_relativa = item.img['src'].replace('../..', '').lstrip('/')
            imagem_url = f"{SCRAP_URL.rstrip('/')}/{imagem_relativa}"

            livros.append({
                'titulo': titulo,
                'preco': preco,
                'imagem': imagem_url
            })

    return livros
