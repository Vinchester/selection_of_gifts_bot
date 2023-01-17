import requests
from bs4 import BeautifulSoup

file = open("parsed.html", 'w', encoding="utf-8")
url = "https://www.podarkoff.com.ua/cat/40/"
r = requests.get(url)
file.write(r.text)
def buttons():
    file1 = open("parsed.html", 'r', encoding="utf-8")
    item = BeautifulSoup(file1, "html.parser")
    cat_name = []
    cat_links = []
    names = item.find_all('div', {"class": "subcat-name"})
    for x in names:
        cat_name.append(x.find('a').text)
        cat_links.append(x.find('a').get("href"))
    # all = dict.fromkeys(cat_name, cat_links)
    all = dict(zip(cat_name, cat_links))
    print(all)
    return all

