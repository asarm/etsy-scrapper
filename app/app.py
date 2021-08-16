from flask import Flask, redirect
from flask import render_template
import db
from flask import request

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
   all_products = db.get_all_products()

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
   product = db.get_product(id)

   return render_template('product_detail.html', title='Detail', product=product)

@app.route('/add_post/', methods=['POST', 'GET'])
def add_post():
   if request.method == 'POST':
      url = request.form.get('p_url')
      try:
         db.add_product(url)
      except:
         print("There is a problem.")
      return redirect("/", code=302)
   else:
      return redirect("/", code=302)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000)