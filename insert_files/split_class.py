# -*- coding: Utf-8 -*
'''request_class produces a foods list with the data we need.
But stores and categories data are aggregate in a string.
This class splits the string in list values and maintains
the link between each store and category and the products.'''
import re

class Split:

    def __init__(self, request):
        self.request = request

    def split(self, key, list_name1, list_name2):
        duplicate_entries = []
        for i, first_value in enumerate(self.request):
            stores_category_product = {"name":first_value[key]}
            for key_store_category, value_store_category in stores_category_product.items():
                value_store_category = re.sub(", ", ",", value_store_category)
                value_store_category = value_store_category.split(',')
            for i, final_value in enumerate(value_store_category):
                stores_categories = {"name":final_value.capitalize()}
                unique_store_category = {final_value.capitalize():first_value["name"]}
                list_name2.append(unique_store_category) #this list
                #is used to create the lists for the intermediate tables
                if stores_categories["name"] not in duplicate_entries:
                    duplicate_entries.append(stores_categories["name"])
                    list_name1.append(stores_categories) #this list is used to insert stores in the database