# -*- coding: Utf-8 -*
'''With all the following classes
requests and inserts the URL from main'''
import request_class
import product_class
import category_class
import split_class
import store_class
import intermediate_table_class

class Request_insert_url:

    def __init__(self):
        pass

    def request_insert_url(self, url, id_category):
        self.url = url
        self.id_category = id_category

        REQUEST = request_class.Request(self.url)
        REQUEST.request()

        PRODUCT = product_class.Product(REQUEST.foods)
        PRODUCT.insert_product()

        store, unique_store, category, unique_category = [], [], [], []
        SPLIT = split_class.Split(REQUEST.foods)
        SPLIT.split("store", store, unique_store)
        SPLIT.split("category", category, unique_category)

        CATEGORY = category_class.Category(category)
        CATEGORY.insert_category()
        CATEGORY.insert_categories_product(REQUEST.duplicate_entries, self.id_category)
        CATEGORY.insert_categories_product2()

        STORE = store_class.Store(store)
        STORE.insert_store()

        select_id_name_store = """SELECT id, name FROM store """
        select_id_name_product = """SELECT id, name FROM product """
        add_store_product = """INSERT IGNORE INTO Store_product (id_store, id_product)
        VALUES (%(id_store)s, %(id_product)s)"""
        INTERMEDIATE_TABLE = intermediate_table_class.Intermediate_table()
        INTERMEDIATE_TABLE.cursor(select_id_name_store)
        INTERMEDIATE_TABLE.id_product(unique_store)
        INTERMEDIATE_TABLE.cursor(select_id_name_product)
        INTERMEDIATE_TABLE.id_id(INTERMEDIATE_TABLE.list_dict_id_product)
        INTERMEDIATE_TABLE.insert(add_store_product)
