"""Importing 'requests' and 'BeautifulSoup' modules"""
import requests
from bs4 import BeautifulSoup


def request_file(url):
    """Function to make a request to web page of products"""
    with open("parsed_cat.html", 'w', encoding="utf-8") as file:
        link = f"https://www.podarkoff.com.ua{url}"
        request = requests.get(link, timeout=10)
        file.write(request.text)


def parsing(url):
    """Function to pars file 'parsed_cat'"""
    request_file(url)
    with open("parsed_cat.html", 'r', encoding="utf-8") as file:
        item = BeautifulSoup(file, "html.parser")
        names = item.find_all('a', {"class": "product_name src-name-height"})
        prices = item.find_all('div', {"class": "price_block"})
        photos = item.find_all('a', {"class": "src-img-height"})
        item_name = [name.text for name in names]
        item_price = [price.text for price in prices]
        item_photo = [photo.find("img").get("src") for photo in photos]
        products = list(zip(item_name, item_photo, item_price))
        return products

#DeFakto
