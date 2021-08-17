'''
name: Mert Arda Asar
date: 17.08.2021

db.py file contains the main operations which are using the database.
Provides database connection with adding, listing and searching operations.
'''

from mysql import connector
import functions
from Product import Product
import config


class MysqlOperator:

    # If database connection is successful = True
    is_connected = False

    '''
        Tries to connect db. Auth information is set at config.py.
        If desired database, which keeps products' data,  does not exist, creates automatically.
    '''
    def db_connection(self):
        # Checks if desired db is exist
        try:
            mydb = connector.connect(user=config.DB_USER, password=config.DB_PASSWORD,
                                     host=config.DB_HOST, port=config.DB_PORT, database=config.DB_DATABASE,
                                     auth_plugin='mysql_native_password')
            cursor = mydb.cursor()
            self.is_connected = True
            print("DB IS FOUND\n")
            return mydb, cursor

        # Creates desired db and table automatically. Table name is products.
        except:
            print("DB DOES NOT FOUND.\nDB IS CREATING...")
            try:
                mydb = connector.connect(user=config.DB_USER, password=config.DB_PASSWORD,
                                         host=config.DB_HOST, port=config.DB_PORT, auth_plugin='mysql_native_password')
                cursor = mydb.cursor()
                query = "CREATE DATABASE " + config.DB_DATABASE
                cursor.execute(query)

                mydb = connector.connect(user=config.DB_USER, password=config.DB_PASSWORD,
                                         host=config.DB_HOST, port=config.DB_PORT, database=config.DB_DATABASE,
                                         auth_plugin='mysql_native_password')
                cursor = mydb.cursor()
                cursor.execute(
                    "CREATE TABLE products(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), image VARCHAR(255), price FLOAT)")
                print("DB IS CREATED SUCCESSFULLY.")
                self.is_connected = True
                return mydb, cursor

            # Returns None if connection information is wrong (from config.py).
            except:
                return None, None

    ''' 
        Inserts a new product from given url at products table. 
        Returns True or False based on operation status.
    '''
    def add_product(self, url):
        mydb, cursor = self.db_connection()

        print("Product is adding from " + url)
        try:
            product_data = functions.fetch_product(url)
            product = Product(name=product_data['product_name'], price=product_data['product_price'],
                              image=product_data['product_img'])

            sql_insert_query = """INSERT INTO products(name, image, price) VALUES (%s,%s,%s)"""
            # tuple to insert at placeholder
            data_tuple = (product.name, product.image, product.price)
            cursor.execute(sql_insert_query, data_tuple)

            mydb.commit()
            print("Product is added successfully.\n")
            return True
        except Exception as e:
            print(f"A problem was occurred. Please check your url.\n{e}")
            return False

    '''
        If db information is wrong, returns 'connection_error' string.
        Returns a product object which has given id. If given id does not found, returns None.
    '''
    def get_product(self, product_id):
        mydb, cursor = self.db_connection()

        if mydb == None:
            return 'connection_error'

        query = "SELECT * FROM products WHERE id =" + str(product_id)
        cursor.execute(query)
        result = cursor.fetchall()

        if len(result) <= 0:
            print("Product could not found.")
            return None
        else:
            product = Product(name=result[0][1], image=result[0][2], price=result[0][3])
            return product

    '''
        If db information is wrong, returns 'connection_error' string.
        Returns all products from the products table ordered by id. If the table is empty, returns None.  
        Returned object type is an array.
    '''
    def get_all_products(self):
        mydb, cursor = self.db_connection()

        if mydb == None:
            return 'connection_error'

        query = "SELECT * FROM products ORDER BY id DESC"
        cursor.execute(query)
        result = cursor.fetchall()

        if len(result) <= 0:
            print("Products table is empty.")
            return None
        else:
            return result

    '''
        Checks if there is any object which contains given keyword. 
        Returns object(s), which contain keyword, as an array.
    '''
    def search_product(self, title):
        mydb, cursor = self.db_connection()

        query = f"SELECT * FROM products WHERE name LIKE '%{title}%' ORDER BY id DESC"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        return result