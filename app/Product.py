'''
name: Mert Arda Asar
date: 17.08.2021

Product class represents each product from etsy.com
Product class has name, image and price attributes
'''

class Product:

    name = ""
    image = ""
    price = 0

    def __init__(self, name, image, price):
        self.name = name
        self.image = image
        self.price = price

    def convert_to_json(self):

       return {
           'name':self.name,
           'image':self.image,
           'price':self.price
       }