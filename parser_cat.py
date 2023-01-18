"""Importing 'requests' and 'BeautifulSoup' modules"""
import requests
from bs4 import BeautifulSoup


def request_page():
    """Function to make a request to web page of categories"""
    with open("parsed.html", 'w', encoding="utf-8") as file:
        url = "https://www.podarkoff.com.ua/cat/40/"
        request = requests.get(url, timeout=10)
        file.write(request.text)


def buttons():
    """Function to pars file 'parsed'"""
    request_page()
    with open("parsed.html", 'r', encoding="utf-8") as file:
        item = BeautifulSoup(file, "html.parser")
        names = item.find_all('div', {"class": "subcat-name"})
        cat_name = [name.find('a').text for name in names]
        cat_links = [link.find('a').get("href") for link in names]
        categories = dict(zip(cat_name, cat_links))
        return categories


#DeFakto
