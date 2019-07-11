'''With all the following classes requests and inserts the URL from main'''

import request_class
import db_connect_class
import constants


class Request_insert_url:
    '''Calls other classes to request, parse
    and insert the URL from OpenFoodFact'''

    def __init__(self):
        pass

    def request_insert_url(self, cat, id_category):
        '''Request the url, then parse and insert products, stores and categories
        Then parse and insert the intermediate tables'''

        self.id_category = id_category
        self.cat = cat

        REQUEST = request_class.Request(self.cat)
        REQUEST.request()
        REQUEST.split()

        DB = db_connect_class.Db_connect()
        DB.insert(constants.add_product, REQUEST.foods)
        DB.insert(constants.add_store, REQUEST.store)
        DB.insert(constants.add_category, constants.category)

        DB.select(constants.select_id_name_product)
        REQUEST.list_categories_product(self.id_category,
                                        DB.dict_cursor)
        DB.insert(constants.add_category_product,
                  REQUEST.list_id_product_id_category)

        DB.select(constants.select_id_name_store)
        REQUEST.id_product(REQUEST.unique_store, DB.dict_cursor)
        list_id_store_value_product = REQUEST.list_dict_id_product
        DB.select(constants.select_id_name_product)
        REQUEST.id_id(list_id_store_value_product, DB.dict_cursor)
        DB.insert(constants.add_store_product, REQUEST.list_dict_id_product)
