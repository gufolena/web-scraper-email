import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import requests
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = os.getenv("EMAIL_TO")


def baixar_imagem(url):
    """Faz o download da imagem a partir da URL."""
    try:
        print(f"🔄 Baixando imagem: {url}")
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"⚠️ Erro ao baixar imagem: {url}")
            return None
    except Exception as e:
        print(f"❌ Erro ao baixar imagem: {e}")
        return None


def enviar_email(livros):
    print("📤 Iniciando montagem do e-mail...")

    msg = MIMEMultipart('related')
    msg['Subject'] = "📚 Lista de livros com imagens embutidas"
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_TO

    html = """
    <html>
    <body>
    <h2>Livros coletados:</h2>
    <ul>
    """

    partes_imagem = []

    for idx, livro in enumerate(livros):
        content_id = f"livro{idx}"
        html += f"""
        <li>
            <strong>{livro['titulo']}</strong><br>
            Preço: {livro['preco']}<br>
            <img src="cid:{content_id}" width="100"/><br><br>
        </li>
        """

        img_bytes = baixar_imagem(livro['imagem'])
        if img_bytes:
            image_part = MIMEImage(img_bytes)
            image_part.add_header('Content-ID', f'<{content_id}>')
            partes_imagem.append(image_part)

    html += "</ul></body></html>"

    # Anexa o corpo HTML
    corpo_email = MIMEText(html, 'html')
    msg.attach(corpo_email)

    # Anexa todas as imagens
    for img in partes_imagem:
        msg.attach(img)

    print("📦 Conectando ao servidor SMTP...")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_USER, EMAIL_PASS)
            print("🔐 Login realizado com sucesso.")
            server.sendmail(EMAIL_USER, EMAIL_TO, msg.as_string())
            print("✅ E-mail enviado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")
