import requests
from bs4 import BeautifulSoup
from ScrapingNews.coki_head import cookies, headers
import json

def get_link_news():
    link_news = []
    url = f"https://www.playground.ru/news/hardware?p=1"
    response = requests.get(url, headers=headers, cookies=cookies)

    with open("ScrapingNews//index.html", "w", encoding="utf-8") as file:
        file.write(response.text)

    with open("ScrapingNews//index.html", encoding="utf-8") as file:
        page = file.read()

    bs = BeautifulSoup(page, "lxml")

    for i in bs.find_all("div", class_="post-title"):
        link_news.append(i.find("a").get("href"))

    return link_news

def get_data(url):
    result_data = []
    for index, item in enumerate(url):
        response = requests.get(item, headers=headers, cookies=cookies)

        with open("ScrapingNews//index2.html", "w", encoding="utf-8") as file:
            file.write(response.text)

        with open("ScrapingNews//index2.html", encoding="utf-8") as file:
            page = file.read()

        bs = BeautifulSoup(page, "lxml")

        name_title = bs.find("h1", class_="post-title").text.strip()
        data = bs.find("div", class_="post-metadata").find("time").get("data-balloon")

        text = ""
        for i in bs.find("main", class_="post post-full js-post").find_all("p"):
            text += f"{i.text.strip()}\n"

        result_data.append(
            {
                "Номер": index + 1,
                "Ссылка": item,
                "Название": name_title,
                "Дата": data,
                "Текст": text
            }
        )

        print(f"{index + 1}/{len(url)}")

    with open("ScrapingNews//news.json", "w", encoding="utf-8") as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)

def get_news():
    url = get_link_news()
    get_data(url)

if __name__ == "__main__":
    get_news()