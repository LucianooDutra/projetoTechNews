import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        time.sleep(1)

        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# print(fetch("https://blog.betrybe.com/"))


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    links = selector.css("h2.entry-title a::attr(href)").getall()

    return links


# print(scrape_updates(fetch("https://blog.betrybe.com/")))


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    url = selector.css("div.nav-links a.next::attr(href)").get()

    if url:
        return url
    else:
        return None


# print(scrape_next_page_link(fetch("https://blog.betrybe.com/")))


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)

    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().replace("\xa0", "")
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("span.author a.url::text").get()
    reading_time = selector.css("li.meta-reading-time::text").get()
    new_reading_time = reading_time.strip().split(" ")[0]
    summary = selector.xpath("string(//p)").get()
    new_sumary = "".join(summary).strip().replace("\xa0", "")
    category = selector.css("div.meta-category span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(new_reading_time),
        "summary": new_sumary,
        "category": category,
    }


# print(
#     scrape_news(fetch("https://blog.betrybe.com/carreira/trybetalks-gaules/"))
# )


# Requisito 5
def get_tech_news(amount):

    content_page = fetch("https://blog.betrybe.com/")

    list_links = []

    while len(list_links) <= int(amount):
        list_links.extend(scrape_updates(content_page))
        link_next_page = scrape_next_page_link(content_page)
        content_page = fetch(link_next_page)

    result = []

    for link in list_links[: int(amount)]:
        content_page = fetch(link)
        data_page = scrape_news(content_page)

        result.append(data_page)

    create_news(result)

    return result


# print(get_tech_news(10))
