import requests
from dotenv import load_dotenv
import os
from datetime import date, timedelta
from deep_translator import GoogleTranslator  # Substituir googletrans

# API Keys
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Função para traduzir o texto
def translate_text(text, target_language="pt"):
    return GoogleTranslator(source="auto", target=target_language).translate(text)

# Função para obter notícias econômicas do Brasil
def get_brazil_news():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'category': 'business',
        'apiKey': NEWS_API_KEY,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        # Traduzindo as notícias antes de retorná-las
        translated_articles = []
        for article in articles:
            title = article.get('title', 'Título não disponível')
            description = article.get('description', 'Descrição não disponível')

            # Verifica se os campos não são None antes de traduzir
            title_pt = translate_text(title) if title else "Título não disponível"
            description_pt = translate_text(description) if description else "Descrição não disponível"

            translated_articles.append({
                'title': title_pt,
                'description': description_pt,
                'url': article.get('url', '#'),
                'publishedAt': article.get('publishedAt', 'Data não disponível')
            })
        return translated_articles
    else:
        print(f"Error fetching news: {response.status_code}")
        return []

# Função para obter a cotação do USD
def get_currency_rates():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "USD": {
                "compra": float(data["USDBRL"]["bid"]),
                "venda": float(data["USDBRL"]["ask"]),
                "data": data["USDBRL"]["create_date"],
            },
            "EUR": {
                "compra": float(data["EURBRL"]["bid"]),
                "venda": float(data["EURBRL"]["ask"]),
                "data": data["EURBRL"]["create_date"],
            },
            "BTC": {
                "compra": float(data["BTCBRL"]["bid"]),
                "venda": float(data["BTCBRL"]["ask"]),
                "data": data["BTCBRL"]["create_date"],
            },
        }
    else:
        return {"error": f"Erro ao buscar cotações: {response.status_code}"}
