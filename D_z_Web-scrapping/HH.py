
from urllib.parse import urljoin
from pprint import pprint
import fake_headers# генерит фейковые заголовки позволяет притворится браузером
import requests
from bs4 import BeautifulSoup
import io

headers_gen = fake_headers.Headers(browser="opera", os="linux")



response = requests.get("https://spb.hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=python&search_field=name&search_field=description&excluded_text=&area=1&area=2&salary=&currency_code=RUR&only_with_salary=true&experience=doesNotMatter&order_by=relevance&search_period=1&items_on_page=20", headers=headers_gen.generate())#запрос со сгенерированными заголовками
html_data = response.text
KEYWORDS = ['Django', 'Flask', 'Python']
hh_main = BeautifulSoup(html_data, "lxml")
a11y_main_content_tag = hh_main.find("div", id ="a11y-main-content")
serp_item_tag = a11y_main_content_tag.find_all("div", class_="serp-item")

vacancy_list=[]
for item_tag in serp_item_tag:
    header_tag = item_tag.find("h3")
    header_text = header_tag.text
    a_tag = header_tag.find("a")
    link = a_tag["href"]
    link = urljoin("https://habr.com", link)

    vacancy_response = requests.get(link, headers=headers_gen.generate())
    vacancy = BeautifulSoup(vacancy_response.text, "lxml")
    user_content = vacancy.find("div", class_="g-user-content")
    description = user_content.text


    if KEYWORDS[0] in description or KEYWORDS[1] in description or KEYWORDS[2] in description:


        city_tegs=item_tag.find("div",class_="vacancy-serp-item-company")
        city_teg = city_tegs.find("div", class_="vacancy-serp-item__info")
        city_= city_teg("div", class_="bloko-text")
        city = (city_[1].text).replace(u'\xa01\xa0', ' ')

        company_tegs = city_tegs.find("div", class_="vacancy-serp-item__meta-info-company")
        company_teg = company_tegs.find("a")
        company = company_teg.text

        salary_tegs = vacancy.find("div", class_="vacancy-title")
        salary_teg = salary_tegs.find("span", class_="bloko-header-section-2 bloko-header-section-2_lite")
        salary = (salary_teg.text).replace(u'\xa0', ' ')

        vacancy_list.append([link,salary,company,city])

with open("new_vacancy.json", "w", encoding='utf-8') as f:
    for i, j in enumerate(vacancy_list):
        s = io.StringIO(','.join(vacancy_list[i]))
        f.write(','.join(vacancy_list[i]))
        f.write('\n')


