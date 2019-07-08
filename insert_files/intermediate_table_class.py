# -*- coding: Utf-8 -*
'''This class converts the stores-products list and the categories-products list in id-id list
and inserts the lists in the intermediate tables of the database'''
import pwd

import mysql.connector

CNX = mysql.connector.connect(user=pwd.user, password=pwd.password,
                              host="localhost",
                              database="healthy_food")

CURSOR = CNX.cursor()

class Intermediate_table:

    def __init__(self):
        self.dict_cursor = {}
        self.dict_id_product = {}
        self.list_dict_id_product = []

    def cursor(self, query):
        '''Generates dictionaries with the name and id of the products, categories and stores'''
        CURSOR.execute(query)
        for int_id, str_name in CURSOR:
            dico = {int_id:str_name}
            self.dict_cursor.update(dico)

    def id_product(self, liste):
        '''Generates a list with the id of the category or the store and the name of the product'''
        for dico in liste:
            for key_store_category, value_product in dico.items():
                for int_id2, str_name2 in self.dict_cursor.items():
                    if key_store_category == str_name2:
                        self.dict_id_product = {int_id2 : value_product}
            self.list_dict_id_product.append(self.dict_id_product)

    def id_id(self, liste):
        '''Generates a list with the id of the category or the store and the id of the product'''
        self.dict_id_product = {}
        self.list_dict_id_product = []
        for dico in liste:
            for key_store_category, value_product in dico.items():
                for int_id2, str_name2 in self.dict_cursor.items():
                    if value_product == str_name2:
                        self.dict_id_product = {"id_store":key_store_category, "id_product":int_id2}
            self.list_dict_id_product.append(self.dict_id_product)

    def insert(self, add_table):
        '''Inserts the id-id lists in the intermediate tables'''
        CURSOR.executemany(add_table, self.list_dict_id_product)
        CNX.commit()