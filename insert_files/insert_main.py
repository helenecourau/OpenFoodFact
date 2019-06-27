import requests
import mysql.connector

import insert_class
import pwd

cnx = mysql.connector.connect(user=pwd.user, password= pwd.password,
                              host='localhost',
                              database='healthy_food')

cursor = cnx.cursor()

PRODUCT = insert_class.Insert('https://fr.openfoodfacts.org/categorie/guimauves.json')
PRODUCT.request()
PRODUCT.insert_product()
PRODUCT.insert_category()
PRODUCT.request_store()
PRODUCT.insert_store()
select_id_nom_store = """SELECT id, nom FROM store """
query2 = """SELECT id, nom FROM product """
PRODUCT.insert_store_product(select_id_nom_store, PRODUCT.unique_store)
PRODUCT.insert_store_product2(query2, PRODUCT.list_dict_id_store_product)
PRODUCT.request_category()
PRODUCT.insert_category_product()
PRODUCT.insert_category_product2()
PRODUCT.insert_store_product3()
PRODUCT.insert_category_product3()

cnx.commit()
cursor.close()
cnx.close()