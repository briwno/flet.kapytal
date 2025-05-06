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
    # # URL da API de notícias
    # url = 'https://newsapi.org/v2/top-headlines'
    # # Parâmetros para a requisição, incluindo a categoria e a chave da API
    # params = {
    #     'category': 'business',  # Categoria de notícias de negócios
    #     'apiKey': NEWS_API_KEY,  # Chave da API obtida do arquivo .env
    # }
    # # Fazendo a requisição para a API
    # response = requests.get(url, params=params)
    
    # # Verifica se a resposta foi bem-sucedida
    # if response.status_code == 200:
    #     # Obtém os artigos da resposta JSON
    #     articles = response.json().get('articles', [])
    #     # Lista para armazenar os artigos traduzidos
    #     translated_articles = []
    #     for article in articles:
    #         # Obtém o título e a descrição do artigo
    #         title = article.get('title', 'Título não disponível')
    #         description = article.get('description', 'Descrição não disponível')

    #         # Traduz os campos se eles não forem None
    #         title_pt = translate_text(title) if title else "Título não disponível"
    #         description_pt = translate_text(description) if description else "Descrição não disponível"

    #         # Adiciona o artigo traduzido à lista
    #         translated_articles.append({
    #             'title': title_pt,
    #             'description': description_pt,
    #             'url': article.get('url', '#'),
    #             'publishedAt': article.get('publishedAt', 'Data não disponível')
    #         })
    #     return translated_articles
    # else:
        # Caso ocorra um erro, retorna uma notícia genérica
        print(f"Erro ao buscar notícia")
        return [{
            'title': 'Notícia genérica',
            'description': 'Não foi possível obter notícias no momento.',
            'url': '#',
            'publishedAt': 'Data não disponível'
        }]

# Função para obter a cotação do USD
def get_currency_rates():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,ARS-BRL"
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
            "ARS": {
                "compra": float(data["ARSBRL"]["bid"]),
                "venda": float(data["ARSBRL"]["ask"]),
                "data": data["ARSBRL"]["create_date"],
            },
            
        }
    else:
        return {"error": f"Erro ao buscar cotações: {response.status_code}"}
