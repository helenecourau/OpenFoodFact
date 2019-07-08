# -*- coding: Utf-8 -*
'''This class retrieve the data from the OpenFoodFact API and store it in a list.
This list is used by the other classes.
Warning : OpenFoodFact database is a little messy.'''

import requests

class Request:
    '''Requests and parses data from the OpenFoodFact API'''

    def __init__(self, url):
        self.url = url
        self.foods, self.duplicate_entries = [], [] #this is the list used by the other classes

    def request(self):
        '''Requests and parses data from the OpenFoodFact API'''
        object_json = requests.get(self.url)
        object_json = object_json.json()
        list_clean = object_json['products'] #the object json from the API
        #has a lot of data and we only need the data from product
        for dico in list_clean: #this loop screens the dict in the list and
        #put the info we need in a dico and each dico in self.foods list
            if dico.get("stores") and dico.get("categories") and dico.get("product_name")\
            and dico.get("nutrition_grades") and dico.get("ingredients_text_debug"):
            #we take only the product with store, category and nutrition grade
            #because we need all those fields
                info_product = {
                    "name":dico["product_name"].capitalize().strip(),
                    "grade":dico["nutrition_grades"],
                    "description":dico["ingredients_text_debug"],
                    "url":dico["url"],
                    "category":dico["categories"],
                    "store":dico["stores"],
                    }
                if info_product["name"] not in self.duplicate_entries:
                    self.duplicate_entries.append(info_product["name"])
                    self.foods.append(info_product)
