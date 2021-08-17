'''
name: Mert Arda Asar
date: 17.08.2021

A Flask web app to scrape data from etsy.com using product url.
Fetches and saves to database desired product's main image, name and price.
This application can be used as an api or on the web with an user interface.

app.py file contains the main functions that able to run the application.
Application is initializes and url paths with their functions can be found in this script.
'''

from flask import Flask, redirect
from flask import render_template
from db import MysqlOperator
from flask import request
from flask import jsonify
import functions

app = Flask(__name__, template_folder='template')
mysqlOperator = MysqlOperator()


@app.route('/')
def home():
    all_products = mysqlOperator.get_all_products()

    if all_products == 'connection_error':
        return "Application could not connect to db. Please check your db information from config.py."

    if all_products == None:
        products = {
            'products': [],
            'total_products': 0
        }
    else:
        products = {
            'products': all_products,
            'total_products': len(all_products)
        }

    return render_template('all_products.html', title='Home', products=products)


@app.route('/product/<id>', methods=['GET'])
def product_detail(id):
    product = mysqlOperator.get_product(id)

    if product == 'connection_error':
        return "Application could not connect to db. Please check your db information from config.py."

    return render_template('product_detail.html', title='Detail', product=product)


@app.route('/add_product/', methods=['POST', 'GET'])
def add_product():
    if request.method == 'POST':
        url = request.form.get('p_url')
        try:
            mysqlOperator.add_product(url)
        except:
            print("There is a problem.")
        return redirect("/", code=302)
    else:
        return redirect("/", code=302)

@app.route('/search', methods=['POST', 'GET'])
def search_product():
    title = ""
    if request.method == 'POST':
        title = request.form.get('title')
        print(title)
        products = mysqlOperator.search_product(title)
    else:
        products = []

    result = {'products':products, 'total_products':len(products), 'search_key':title}
    return render_template('search_result.html', title="Search", products=result)

# Routing functions for the API
@app.route('/api/all_products', methods=['GET'])
def all_products():
    products = mysqlOperator.get_all_products()

    if products == 'connection_error':
        return "Application could not connect to db. Please check your db information from config.py."

    response = []

    for product in products:
        response.append(functions.list_to_json(product))

    return jsonify(response)

@app.route('/api/get_product/<id>', methods=['GET'])
def get_product(id):
   product = mysqlOperator.get_product(id)

   if product == 'connection_error':
       return "Application could not connect to db. Please check your db information from config.py."

   if product == None:
       response = "Given id does not found.\nPlease use '/api/all_products' to list all products.\nUsage: api/get_product/<product_id>\n"
       return response

   response = product.convert_to_json()
   response['id'] = id

   return jsonify(response)

@app.route('/api/add_product/', methods=['POST'])
def add_new():
   try:
      url = request.args.get('url')
      operation = mysqlOperator.add_product(url)
      if not operation:
          return "500"
      return "200"
   except:
      return "Please check your url.\nUsage: /api/add_product/?url=<etsy_url>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)