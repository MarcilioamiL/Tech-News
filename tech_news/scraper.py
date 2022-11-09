from parsel import Selector
import requests
from time import sleep


# Requisito 1
def fetch(url, timeout=1):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    base_url = Selector(html_content)
    return base_url.css("h2.entry-title > a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    base_url = Selector(html_content)
    return base_url.css("a.next::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    return {
        "category": selector.css("div.entry-details span.label::text").get(),
        "comments_count": len(selector.css("ol.comment-list::text").getall()),
        "summary": (
            selector.xpath("string(//div[@class='entry-content']//p[1])")
            .get()
            .strip()
        ),
        "tags": selector.css("a[rel='tag']::text").getall(),
        "timestamp": selector.css("li.meta-date::text").get(),

    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
