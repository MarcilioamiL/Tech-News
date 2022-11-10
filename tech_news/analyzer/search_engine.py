from tech_news.database import search_news

from datetime import datetime


def df_forma(new_forma):
    new_list = []
    for i in new_forma:
        new_formation = (i["title"], i["url"])
        new_list.append(new_formation)
    return new_list


# Requisito 6
def search_by_title(title):
    return df_forma(search_news({"title": {"$regex": title, "$options": "i"}}))


# Requisito 7
def search_by_date(date):
    try:
        datetime.fromisoformat(date)
    except ValueError:
        raise ValueError("Data inválida")
    pattern = date[8:10]+'/'+date[5:7]+'/'+date[:4]
    return df_forma(search_news(
        {"timestamp": {"$regex": pattern, "$options": "i"}}
    ))


# Requisito 8
def search_by_tag(tag):
    return df_forma(search_news(
        {"tags": {"$regex": tag, "$options": "i"}}
    ))


# Requisito 9
def search_by_category(category):
    return df_forma(search_news(
        {"category": {"$regex": category, "$options": "i"}}
    ))
