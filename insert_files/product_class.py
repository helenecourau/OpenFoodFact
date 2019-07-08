# -*- coding: Utf-8 -*
'''This class inserts the products data in the product table of the database.
It relies on the list from request_class'''

import pwd
import mysql.connector

CNX = mysql.connector.connect(user=pwd.user, password=pwd.password,
                              host="localhost",
                              database="healthy_food")

CURSOR = CNX.cursor()

class Product:
    '''Inser product in database'''

    def __init__(self, request):
        self.request = request

    def insert_product(self):
        '''Inser product in database'''
        add_product = """INSERT IGNORE INTO product (name, description, url, grade)\
        VALUES (%(name)s, %(description)s, %(url)s, %(grade)s)"""
        CURSOR.executemany(add_product, self.request)
        CNX.commit()