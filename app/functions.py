'''
name: Mert Arda Asar
date: 17.08.2021

functions.py file contains required functions to scraping data from url and converting a list of products to json.
'''

from bs4 import BeautifulSoup
import requests


def fetch_product(url):
    # keeps product information (name, price and img)
    product_data = dict()

    r = requests.get(url)
    source = BeautifulSoup(r.content, "html.parser")

    # name could be fetch directly from url instead using bs
    product_name = source.find("h1").text.strip()
    product_price = source.find("div", {"class": "wt-display-flex-xs wt-align-items-center"}).text.strip().split()[0]
    # removes currency symbol
    product_price = product_price[1:]
    img = source.find("img", {"class": "wt-max-width-full wt-horizontal-center wt-vertical-center carousel-image wt-rounded"})
    product_img = img['src']

    # a dictionary is using to make more understandable and useful to returning data
    product_data['product_name'] = product_name
    product_data['product_price'] = product_price
    product_data['product_img'] = product_img

    return product_data

# Converts a list which contains a product information to json object
def list_to_json(product):
    return {
            'id': product[0],
            'name': product[1],
            'img_url': product[2],
            'price': product[3]
            }