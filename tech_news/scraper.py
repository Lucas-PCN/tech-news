import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        sleep(1)
        response = requests.get(
            url,
            headers={"User-Agent": "Faker user-agent"},
            timeout=3,
        )

        if response.status_code != 200:
            return None

        return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    hrefs_list = selector.css(".cs-overlay-link::attr(href)").getall()
    return hrefs_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css(".nav-links.next::attr(href)").get()

    if not next_page:
        return None

    return next_page


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
