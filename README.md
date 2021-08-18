etsy-scrapper

It takes the product URL belonging to ETSY and scrapes the product information from the site (name, main image url and price).
It saves this information in MYSQL database. 
Shows the product detail when it is selected. 

<h2>USAGE</h2>

Install requirements from requirements.txt using pip install -r requirements.txt </br> 
Change your db information from config.py. </br>
Run app/app.py file to use web application.</br>
Dockerization does not work for now. Mysql connection could not complated.

<h3>Usage as an api</h3>
<li>Adding new product </li>
http://192.168.1.62:5000/add_product/?url=https://www.etsy.com/uk/listing/531135817/miniature-brass-helicopter-model-kit?ref=related-5

<h2>Listing the Products From Database</h2>
<img src="images/all_products.png" width="90%">
<h2>Viewing the Product's Detail</h2>
<img src="images/product.png" width="90%">
<h2>Searching Result</h2>
<img src="images/search.png" width="90%">
<h2>MYSQL DB Products Table</h2>
<img src="images/db_table.png" width="90%">
