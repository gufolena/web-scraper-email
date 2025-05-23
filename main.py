from scraper.scraper import scrap_books
from emailer.emailer import enviar_email

if __name__ == "__main__":
    print("🚀 Iniciando processo de scraping...")
    livros = scrap_books()
    print(f"✅ {len(livros)} livros coletados com sucesso!")

    print("📧 Enviando os dados por e-mail...")
    enviar_email(livros)
    print("🏁 Processo finalizado.")