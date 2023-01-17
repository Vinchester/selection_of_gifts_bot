import requests
from bs4 import BeautifulSoup


file = open("parsed_cat.html", 'w', encoding="utf-8")
def pars(url):
    url = f"https://www.podarkoff.com.ua{url}"
    r = requests.get(url)
    file.write(r.text)

    file1 = open("parsed_cat.html", 'r', encoding="utf-8")

    item = BeautifulSoup(file1, "html.parser")
    item_name = []
    names = item.find_all('a', {"class": "product_name src-name-height"})
    for x in names:
        item_name.append(x.text)
    item_photo = []
    urls = item.find_all('a', {"class": "src-img-height"})
    for x in urls:
        item_photo.append(x.find("img").get("src"))
    item_price = []
    prices = item.find_all('div', {"class": "price_block"})
    for x in prices:
        item_price.append(x.text)
    products = list(zip(item_name, item_photo, item_price))

    return products
