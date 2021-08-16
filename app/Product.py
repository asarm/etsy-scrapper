'''
- Adding Product Function: Gets the product link as an input, scraps the data from the website, saves the data to the database, and returns the Product Object (product_id, name, image, price)
- Product Detail Function: Gets the product_id as input and returns the Product Object (product_id, name, image, price)
- Listing Products Function: Returns all the products in the database as an array.
'''
class Product:
    name = ""
    image = ""
    price = ""
    def __init__(self, name, image, price):
        self.name = name
        self.image = image
        self.price = price