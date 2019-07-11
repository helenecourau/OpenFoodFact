# -*- coding: Utf-8 -*
'''This class retrieve the data from the OpenFoodFact.
API and store it in a list. This list is used by the other classes.
Warning : OpenFoodFact database is a little messy.'''

import requests
import re

import constants


class Request:
    '''Requests and parses data from the OpenFoodFact API'''

    def __init__(self, cat):
        self.cat = cat
        self.url = constants.general + constants.research\
            + self.cat + constants.format_research
        # this is the list used by the other classes
        self.foods, self.duplicate_entries = [], []
        self.list_id_product_id_category, self.list_dict_id_product = [], []
        self.dict_id_product = {}

    def request(self):
        '''Requests and parses data from the OpenFoodFact API'''
        object_json = requests.get(self.url)
        object_json = object_json.json()
        list_clean = object_json['products']  # the object json from the API
        # has a lot of data and we only need the data from product
        for dico in list_clean:  # this loop screens the dict in the list and
            # put the info we need in a dico and each dico in self.foods list
            if dico.get("stores") and dico.get("categories")\
                and dico.get("product_name")\
                and dico.get("nutrition_grades")\
                    and dico.get("ingredients_text_debug"):
                # we take only the product with store,
                # category and nutrition grade
                # because we need all those fields
                info_product = {
                    "name": dico["product_name"].capitalize().strip(),
                    "grade": dico["nutrition_grades"],
                    "description": dico["ingredients_text_debug"],
                    "url": dico["url"],
                    "category": dico["categories"],
                    "store": dico["stores"],
                    }
                if info_product["name"] not in self.duplicate_entries:
                    self.duplicate_entries.append(info_product["name"])
                    self.foods.append(info_product)

    def list_categories_product(self, id_category, cursor):
        '''Insert the data in the intermediate_table categories_products'''
        for product_name in self.duplicate_entries:
            for int_id, str_name in cursor.items():
                if str_name == product_name:
                    insert_categories_product = {"id_category": id_category,
                                                 "id_product": int_id}
                    self.list_id_product_id_category.append(insert_categories_product)

    def split(self):
        '''Splits the store string in list values and maintains
        the link between each store and category and the products.'''
        self.store, self.unique_store, duplicate_entries = [], [], []
        for i, first_value in enumerate(self.foods):
            stores_product = {"name": first_value["store"]}
            for key_store, value_store in stores_product.items():
                value_store = re.sub(", ", ",", value_store)
                value_store = value_store.split(',')
            for i, final_value in enumerate(value_store):
                stores = {"name": final_value.capitalize()}
                unique_store = {final_value.capitalize(): first_value["name"]}
                self.unique_store.append(unique_store)  # this list
                # is used to create the lists for the intermediate tables
                if stores["name"] not in duplicate_entries:
                    duplicate_entries.append(stores["name"])
                    # this list is used to insert stores in the database
                    self.store.append(stores)

    def id_product(self, liste, cursor):
        '''Generates a list with the id
        of the store and the name of the product'''
        for dico in liste:
            for key_store, value_product in dico.items():
                for int_id, str_name in cursor.items():
                    if key_store == str_name:
                        self.dict_id_product = {int_id: value_product}
                self.list_dict_id_product.append(self.dict_id_product)

    def id_id(self, liste, cursor):
        '''Generates a list with the id of the
        store and the id of the product'''
        self.list_dict_id_product = []
        for dico in liste:
            for key_store, value_product in dico.items():
                for int_id, str_name in cursor.items():
                    if value_product == str_name:
                        self.dict_id_product = {"id_store": key_store,
                                                "id_product": int_id}
            self.list_dict_id_product.append(self.dict_id_product)
