from tech_news.database import search_news



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



# Requisito 8
def search_by_tag(tag):



# Requisito 9
def search_by_category(category):
