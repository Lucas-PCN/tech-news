from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title.lower(), "$options": "i"}}
    news = search_news(query)
    list = [(new["title"], new["url"]) for new in news]
    return list


# Requisito 7
def search_by_date(date):
    try:
        new_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        query = {"timestamp": {"$eq": new_date}}
        news = search_news(query)

        return [(new["title"], new["url"]) for new in news]

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
