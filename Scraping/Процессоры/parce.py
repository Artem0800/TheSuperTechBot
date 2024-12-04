import json
import requests
from bs4 import BeautifulSoup
from Scraping.cooki_head import cookies, headers

def get_api_id():
    url = "https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/"

    response = requests.get(url, headers=headers, cookies=cookies)

    with open("Scraping//Процессоры//index.html", "w", encoding="utf-8") as file:
        file.write(response.text)

    with open("Scraping//Процессоры//index.html", encoding="utf-8") as file:
        page = file.read()

    soup = BeautifulSoup(page, "lxml")

    l = []
    for i in soup.find_all("li", class_="pagination-widget__page"):
        l.append(i.get("data-page-number"))

    pagination_count = int(l[-1])
    id_api = []

    for item in range(1, pagination_count + 1):
        url = f"https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/?order=2&stock=now&p={item}"

        params = {
            'q': 'видеокарты игровые',
            'category': '17a89aab16404e77',
            'stock': 'now',
            'p': f'{item}',
        }

        response = requests.get(url, headers=headers, cookies=cookies, params=params)

        with open("Scraping//Процессоры//index.html", "w", encoding="utf-8") as file:
            file.write(response.text)

        with open("Scraping//Процессоры//index.html", encoding="utf-8") as file:
            page = file.read()

        soup = BeautifulSoup(page, "lxml")

        for i in soup.find_all("div", class_="catalog-product ui-button-widget"):
            id_api.append("https://www.dns-shop.ru/product/microdata/" + i.get("data-product"))

        print(item)

    print("Сбор id закончен")

    return id_api

def data_write_json_csv(link_api):
    result_data = []
    ai = []
    for ind, item in enumerate(link_api):
        response = requests.get(item, headers=headers, cookies=cookies)
        print(ind + 1, item)

        with open("Scraping//Процессоры//api.json", "w", encoding="utf-8") as file:
            json.dump(response.json(), file, indent=4, ensure_ascii=False)

        with open("Scraping//Процессоры//api.json", encoding="utf-8") as file:
            js = json.load(file)

        if js.get("data").get("aggregateRating") == None:
            result_data.append(
                {
                    "Id": "P" + str(ind),
                    "Название": js.get("data").get("name"),
                    "Описание": js.get("data").get("description"),
                    "Ссылка на товар": js.get("data").get("offers").get("url"),
                    "Стоимость": js.get("data").get("offers").get("price"),
                    "Средняя оценка": "Нету",
                    "Количество отзывов": "Нету",
                    "Картинки": js.get("data").get("image"),
                }
            )
            ai.append(
                {
                    "Название": js.get("data").get("name"),
                    "Стоимость": js.get("data").get("offers").get("price"),
                }
            )
        else:
            result_data.append(
                {
                    "Id": "P" + str(ind),
                    "Название": js.get("data").get("name"),
                    "Описание": js.get("data").get("description"),
                    "Ссылка на товар": js.get("data").get("offers").get("url"),
                    "Стоимость": js.get("data").get("offers").get("price"),
                    "Средняя оценка": round(js.get("data").get("aggregateRating").get("ratingValue"), 1),
                    "Количество отзывов": js.get("data").get("aggregateRating").get("reviewCount"),
                    "Картинки": js.get("data").get("image")
                }
            )
            ai.append(
                {
                    "Название": js.get("data").get("name"),
                    "Стоимость": js.get("data").get("offers").get("price"),
                }
            )

    with open(f"Scraping//Процессоры//result.json", "w", encoding="utf-8") as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)

    with open(f"AI//data.json", "a", encoding="utf-8") as file:
        json.dump(ai, file, indent=4, ensure_ascii=False)

    print("Запись в json файл закончена")

def procces():
    api = get_api_id()
    data_write_json_csv(api)

if __name__ == "__main__":
    procces()