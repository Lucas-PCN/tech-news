import requests
from time import sleep
from parsel import Selector
from tech_news.database import create_news


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
    next_page = selector.css("a.next.page-numbers::attr(href)").get()

    if not next_page:
        return None

    return next_page


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    comments_count = selector.css(".post-comments-simple h5::text").get() or 0
    summary = selector.xpath("string(//p)").get().strip()
    tags = selector.css(".post-tags a::text").getall()
    category = selector.css(".meta-category .label::text").get()

    dict_news = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
        }

    return dict_news


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    urls_list = []
    news = []

    while len(urls_list) <= amount:
        html_content = fetch(url)
        urls_list.extend(scrape_updates(html_content))
        url = scrape_next_page_link(html_content)

    for href in urls_list[0:amount]:
        infos_page = fetch(href)
        news.append(scrape_news(infos_page))

    create_news(news)
    return news
