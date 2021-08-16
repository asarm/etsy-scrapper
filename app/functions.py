'''
- Adding Product Function: Gets the product link as an input, scraps the data from the website, saves the data to the database, and returns the Product Object (product_id, name, image, price)
- Product Detail Function: Gets the product_id as input and returns the Product Object (product_id, name, image, price)
- Listing Products Function: Returns all the products in the database as an array.
'''
from bs4 import BeautifulSoup
import requests

url = "https://www.etsy.com/uk/listing/772695061/brass-or-silver-leaf-bookmark-set"
def fetch_product(url):
    # keeps product information (name, price and img)
    product_data = dict()

    r = requests.get(url)
    source = BeautifulSoup(r.content, "lxml")

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