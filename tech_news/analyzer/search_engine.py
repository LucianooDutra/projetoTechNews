from tech_news.database import search_news
import datetime


# Requisito 7
def search_by_title(title):
    get_news = search_news({"title": {"$regex": title, "$options": "i"}})
    # "$options": "i" = torna case sensitive

    list_news_formated = []
    for new in get_news:
        list_news_formated.append((new["title"], new["url"]))

    return list_news_formated


# Requisito 8
def search_by_date(date):
    try:
        new_date = datetime.date.fromisoformat(date).strftime("%d/%m/%Y")

    except ValueError:
        raise ValueError("Data inválida")

    get_news = search_news({"timestamp": new_date})

    list_news_formated = []
    for new in get_news:
        list_news_formated.append((new["title"], new["url"]))
    return list_news_formated


# Requisito 9
def search_by_category(category):
    get_news = search_news({"category": {"$regex": category, "$options": "i"}})
    # "$options": "i" = torna case sensitive

    list_news_formated = []
    for new in get_news:
        list_news_formated.append((new["title"], new["url"]))

    return list_news_formated
