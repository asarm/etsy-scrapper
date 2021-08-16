from mysql import connector
import functions
from Product import Product

def db_connection():
    USER = "root"
    PASSWORD = ""
    HOST = "localhost"
    PORT = "3306"
    DATABASE = "sociality"

    try:
        mydb = connector.connect(user=USER, password=PASSWORD,
                                 host=HOST, port=PORT, database=DATABASE,
                                 auth_plugin='mysql_native_password')
        cursor = mydb.cursor()
        print("DB IS FOUND\n")
    except:
        print("DB DOES NOT FOUND.\nDB IS CREATING...")
        mydb = connector.connect(user=USER, password=PASSWORD,
                                 host=HOST, port=PORT, auth_plugin='mysql_native_password')
        cursor = mydb.cursor()
        cursor.execute("CREATE DATABASE sociality")

        mydb = connector.connect(user='root', password='asdffdsa1',
                                 host='localhost', database='sociality',
                                 auth_plugin='mysql_native_password')
        cursor = mydb.cursor()
        cursor.execute(
            "CREATE TABLE products(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), image VARCHAR(255), price FLOAT)")
        print("DB IS CREATED SUCCESSFULLY.")

    return mydb, cursor


def add_product(url):
    mydb, cursor = db_connection()
    print("Product is adding from " + url)
    try:
        product_data = functions.fetch_product(url)
        product = Product(name=product_data['product_name'], price=product_data['product_price'], image=product_data['product_img'])

        sql_insert_query = """INSERT INTO products(name, image, price) VALUES (%s,%s,%s)"""
        # tuple to insert at placeholder
        data_tuple = (product.name, product.image, product.price)
        cursor.execute(sql_insert_query, data_tuple)

        mydb.commit()
        print("Product is added successfully.\n")
    except:
        print("A problem was occurred. Please check your url.")

def get_product(product_id):
    mydb, cursor = db_connection()
    query = "SELECT * FROM products WHERE id =" + str(product_id)
    cursor.execute(query)
    result = cursor.fetchall()

    if len(result) <= 0:
        print("Product could not found.")
        return None
    else:
        product = Product(name=result[0][1], image=result[0][2], price=result[0][3])
        return product

def get_all_products():
    mydb, cursor = db_connection()

    query = "SELECT * FROM products"
    cursor.execute(query)
    result = cursor.fetchall()

    if len(result) <= 0:
        print("Products table is empty.")
        return None
    else:
        return result

# example usage of each function

#url = "https://www.etsy.com/uk/listing/531135817/miniature-brass-helicopter-model-kit?ref=related-5"
#add_product(url)
#get_product(7)
#get_all_products()