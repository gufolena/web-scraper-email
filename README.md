
# 📚 Web Scraper com Envio de E-mails

Este é um projeto em Python que realiza web scraping do site [Books to Scrape](https://books.toscrape.com/), coletando informações sobre livros (título, preço e imagem), e envia esses dados por e-mail com as imagens embutidas no corpo da mensagem.

---

## 🚀 Funcionalidades

- 🔎 Coleta de dados de múltiplas páginas (5 por padrão)
- 📬 Envio de e-mail automático com informações e imagens dos livros
- ⚙️ Variáveis de ambiente configuráveis via `.env`
- 🐍 Ambiente virtual gerenciado com `pipenv`

---

## 📦 Requisitos

- Python 3.10+
- Conta Gmail com [senha de app](https://support.google.com/mail/answer/185833?hl=pt-BR) ativada

---

## 📁 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/gufolena/web-scraper-email
cd web-scraper-email
```

### 2. Instale as dependências

Você pode usar **Pipenv** ou o ambiente virtual padrão do Python:

#### ✅ Opção A: Usando Pipenv (recomendado)
```
pipenv install
pipenv shell
```
#### ✅ Opção B: Usando venv + requirements.txt
```
python -m venv venv
venv\Scripts\activate          # Windows
#source venv/bin/activate      # Linux/Mac

pip install -r requirements.txt
```


## ⚙️ Configuração do `.env`

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
SCRAP_URL=https://books.toscrape.com/
EMAIL_USER=seuemail@gmail.com
EMAIL_PASS=sua_senha_de_app
EMAIL_TO=destinatario@gmail.com
```

> 💡 **Use senha de aplicativo** em contas Google (não sua senha real).

---

## ▶️ Execução

No terminal, execute:

```bash
python main.py
```

Você verá prints no terminal indicando:

- Progresso do scraping
- Número de livros coletados
- Progresso do envio de e-mail
- Sucesso ou erro no processo

---

## 🧪 Estrutura do projeto

```
web-scraper-email/
│
├── scraper/
│   └── scraper.py         # Função que coleta os livros das páginas
│
├── email_sender.py        # Envia o e-mail com os dados coletados
├── main.py                # Arquivo principal de execução
├── .env                   # Configurações sensíveis
├── Pipfile                # Gerenciador de dependências
├── Pipfile.lock
└── README.md
```

---

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [requests](https://docs.python-requests.org/)
- [smtplib + email](https://docs.python.org/3/library/email.html)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [pipenv](https://pipenv.pypa.io/)

---

## 📬 Exemplo do e-mail enviado

- Título do livro
- Preço no formato correto (ex: `£51.77`)
- Imagem embutida no corpo do e-mail

---

## ✨ Contribuição

Pull requests são bem-vindos! Sinta-se à vontade para sugerir melhorias ou abrir issues com dúvidas e feedbacks.

---

## 📝 Licença

Este projeto está sob a licença MIT.
