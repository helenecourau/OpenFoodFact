# -*- coding: Utf-8 -*
'''This class inserts the categories data in the categories table of the database.
The categories are hard coded and not selected with the split method.
The products are requested with hard coded URL selected by category of products.
If the categories were selected with the split method,
we could have categories with too few products and I want to avoid that.'''
import pwd

import mysql.connector

CNX = mysql.connector.connect(user=pwd.user, password=pwd.password,
                              host="localhost",
                              database="healthy_food")

CURSOR = CNX.cursor()

class Category:

    def __init__(self, request):
        self.request = request
        self.list_id_product_id_category = []
        self.DICT_CURSOR = {}

    def insert_category(self):
        '''Insert categories in database'''
        category = ["Snack"], ["Soda"], ["Yaourt"], ["Viande"], ["Sauce"]
        add_category = ("INSERT IGNORE INTO category "
                        "(name) "
                        "VALUES (%s)")
        CURSOR.executemany(add_category, category)
        CNX.commit()

    def insert_categories_product(self, liste, id_category):
        '''Insert the data in the intermediate_table categories_products'''
        select_id_name_product = """SELECT id, name FROM product """
        CURSOR.execute(select_id_name_product)
        for int_id, str_name in CURSOR:
            dico = {int_id:str_name}
            self.DICT_CURSOR.update(dico)
        for product_name in liste:
            for key, value in self.DICT_CURSOR.items():
                if value == product_name:
                    insert_categories_product = {"id_category" :id_category, "id_product":key}
                    self.list_id_product_id_category.append(insert_categories_product)

    def insert_categories_product2(self):
        '''Inserts the id-id lists in the intermediate tables'''
        add_category_product = """INSERT IGNORE INTO Category_product (id_category, id_product)\
        VALUES (%(id_category)s, %(id_product)s) """
        CURSOR.executemany(add_category_product, self.list_id_product_id_category)
        CNX.commit()
