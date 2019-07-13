'''This file allows the user to interact with the database.'''
import random
from script import pwd
import mysql.connector

from script import request_insert_url_class
from script import erase_class
from script import constants

CNX = mysql.connector.connect(user=pwd.user, password=pwd.password,
                              host="localhost",
                              database="healthy_food")

CURSOR = CNX.cursor()


class Loop:
    '''This class contains the loops to interact with the user'''

    def __init__(self):
        self.list_bad_product, self.list_good_product = [], []
        self.bad_good_product_id = {}
        self.id_bad = int

    def reboot(self):
        '''Erase the database and inserts new data'''
        database_reboot = str
        while database_reboot not in ("o", "n"):
            try:
                database_reboot = input(constants.ask_init).lower()
                assert database_reboot in ("o", "n")
            except AssertionError:
                print("Ce n'est ni un 'o' ni un 'n'. Veuillez recommencer.")
            if database_reboot == "o":
                print(constants.init)
                erase_class.erase()
                REQUEST_INSERT_URL = \
                    request_insert_url_class.Request_insert_url()
                REQUEST_INSERT_URL.request_insert_url("snack", 1)
                REQUEST_INSERT_URL.request_insert_url("soda", 2)
                REQUEST_INSERT_URL.request_insert_url("yaourt", 3)
                REQUEST_INSERT_URL.request_insert_url("viande", 4)
                REQUEST_INSERT_URL.request_insert_url("sauce", 5)
                print(constants.init_ok)

    def category_fav_choice(self):
        '''The user chooses between seeing
        the products list and the categories'''
        first_choice = 0
        while first_choice != 2:
            list_saved_product = []
            try:
                first_choice = int(input(constants.first_choice))
                assert first_choice in (1, 2)
            except ValueError:
                print("\nIl faut entrer un numéro.\n")
            except AssertionError:
                print(constants.error)
            if first_choice == 1:
                print(constants.fav)
                CURSOR.execute(constants.select_saved_product)
                for (bad_name, product_id, name,
                     description, url, grade) in CURSOR:
                    dico = {"name_bad": bad_name, "id": product_id,
                            "name_good": name, "description": description,
                            "url": url, "grade": grade}
                    list_saved_product.append(dico)
                for dico in list_saved_product:
                    print(constants.print_fav.format(dico["name_bad"],
                          dico["id"], dico["name_good"],
                          dico["url"], dico["grade"].capitalize()))
            elif first_choice == 2:
                CURSOR.execute(constants.SELECT_ID_NAME_CATEGORY)
                for int_id, str_name in CURSOR:
                    print("{} : {}".format(int_id, str_name))

    def category(self):
        '''Select a category to display the products'''
        category_choice = 0
        while category_choice < 1 or category_choice > 5:
            try:
                category_choice = int(input(constants.category_choice))
                assert category_choice >= 1 and category_choice <= 5
            except ValueError:
                print("\nIl faut entrer un numéro.\n")
            except AssertionError:
                print("\nIl faut entrer un numéro entre 1 et 5.\n")
            if category_choice >= 1 and category_choice <= 5:
                category_choice_dict = {"name": category_choice}
                CURSOR.execute(constants.select_product, category_choice_dict)
                for product_id, name, description, url, grade, store in CURSOR:
                    dico = {"id": product_id, "name": name,
                            "description": description,
                            "url": url, "grade": grade, "store": store}
                    if dico["grade"] in ("c", "d", "e"):
                        self.list_bad_product.append(dico)
                    else:
                        self.list_good_product.append(dico)

    def product(self, list_bad_product):
        '''Choose the product to replace'''
        select_product = -1
        next_step = True
        list_select, list_id = [], []
        while next_step is True:
            for dico in list_bad_product[constants.begin:constants.end]:
                list_select.append(dico)
                list_id.append(dico["id"])
                print("{} : {}".format(dico["id"], dico["name"].capitalize()))
            try:
                select_product = int(input(constants.choose_product))
                assert select_product == 0 or select_product in list_id
            except ValueError:
                print("\nIl faut entrer un numéro.\n")
            except AssertionError:
                print(constants.error_product)
            if select_product == 0:
                constants.begin = constants.begin + constants.space
                constants.end = constants.end + constants.space
                if constants.end >= len(list_bad_product):
                    print("Retour à la case départ!")
                    constants.begin = 0
                    constants.end = 5
                select_product = -1
            elif select_product in list_id:
                for dico in list_bad_product:
                    if select_product == dico["id"]:
                        self.id_bad = dico["id"]
                        print(constants.chosen_product
                              .format(dico["id"], dico["name"],
                                      dico["grade"].capitalize()))
                        next_step = False

    def fav(self, list_good_product, bad_good_product_id, id_bad):
        '''Register a product'''
        replace_product = str
        while replace_product != "o":
            random_number = random.randrange(len(list_good_product))
            select_good_product = list_good_product[random_number]
            print(constants.better_product.format
                  (select_good_product["id"], select_good_product["name"],
                   select_good_product["url"],
                   select_good_product["grade"].capitalize(),
                   select_good_product["description"],
                   select_good_product["store"]))
            try:
                replace_product = input(constants.replace)
                assert replace_product in ("a", "o")
            except AssertionError:
                print("Ce n'est ni 'o' ni 'a', recommencez svp.")
            if replace_product == "o":
                bad_good_product_id = {"id_bad_product": id_bad,
                                       "id_good_product": select_good_product["id"]}
                CURSOR.execute(constants.add_replace_product,
                               bad_good_product_id)
                CNX.commit()
                print("Le produit a bien été enregistré.")
