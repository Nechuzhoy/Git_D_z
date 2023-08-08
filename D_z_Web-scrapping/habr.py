
from urllib.parse import urljoin
from pprint import pprint
import fake_headers
import requests
from bs4 import BeautifulSoup


headers_gen = fake_headers.Headers(browser="opera", os="linux")

response = requests.get("https://habr.com/ru/all/", headers=headers_gen.generate())
html_data = response.text


habr_main = BeautifulSoup(html_data, "lxml")
article_list_tag = habr_main.find("div", class_="tm-articles-list")

article_tags = article_list_tag.find_all("article")

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

all_articles = []
count = 0
for article_tag in article_tags:
    header_tag = article_tag.find("h2")
    link = header_tag.find("a")["href"]
    link = urljoin("https://habr.com", link)
    publication_time = article_tag.find("time")['datetime']
    header_text = header_tag.text
    count += 1
    all_articles.append(f'{count}: {publication_time} - {header_text} - {link}')
    article_response = requests.get(link, headers=headers_gen.generate())
    article = BeautifulSoup(article_response.text, "lxml")
    article_body_tag = article.find("div", id="post-content-body")
    article_body_text = article_body_tag.text
    for j, k in  enumerate(KEYWORDS):
        if KEYWORDS[j] in article_body_text:
            print(f' Есть слово, {KEYWORDS[j]} - {count}: {publication_time} - {header_text} - {link}')

print(f'Всего - {len(all_articles)} статей')
pprint(all_articles)