from tech_news.database import search_news

from datetime import datetime


def new_forma(new_forma):
    new_list = []
    for i in new_forma:
        new_formation = (i["title"], i["url"])
        new_list.append(new_formation)
    return new_list


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    return new_forma(news)


# Requisito 7
def search_by_date(date):
    try:
        datetime.fromisoformat(date)
    except ValueError:
        raise ValueError("Data inválida")
    pattern = date[8:10]+'/'+date[5:7]+'/'+date[:4]
    news = search_news(
        {"timestamp": {"$regex": pattern, "$options": "i"}}
    )
    return new_forma(news)


# Requisito 8
def search_by_tag(tag):
    news = search_news(
        {"tags": {"$regex": tag, "$options": "i"}}
    )
    return new_forma(news)


# Requisito 9
def search_by_category(category):
    news = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    return new_forma(news)
