# -*- coding: Utf-8 -*
'''Main file'''
import random
import pwd
import mysql.connector

import request_insert_url_class
import erase_class

CNX = mysql.connector.connect(user=pwd.user, password=pwd.password,
                              host="localhost",
                              database="healthy_food")

CURSOR = CNX.cursor()

MAINLOOP = 1
while MAINLOOP == 1:
    DATABASE_REBOOT = str
    while DATABASE_REBOOT not in ("o", "n"):
        try:
            DATABASE_REBOOT = input("Voulez-vous réinitialiser la base de donnée?\
            	\nTapez 'o' pour oui et 'n' pour non : ").lower()
            if DATABASE_REBOOT == "o":
                print("La base de donnée est en train de se réinitialiser\
                	\nVeuillez patienter 30 secondes.")
                erase_class.erase()
                REQUEST_INSERT_URL = request_insert_url_class.Request_insert_url()
                REQUEST_INSERT_URL.request_insert_url\
                ("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=snacks&page_size=500&json=1", 1)
                REQUEST_INSERT_URL.request_insert_url("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=soda&page_size=500&json=1", 2)
                REQUEST_INSERT_URL.request_insert_url("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=yaourt&page_size=500&json=1", 3)
                REQUEST_INSERT_URL.request_insert_url("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=viande&page_size=500&json=1", 4)
                REQUEST_INSERT_URL.request_insert_url("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=sauce&page_size=500&json=1", 5)
                print("La base données a été réinitialisée!")
            if DATABASE_REBOOT not in ("o", "n"):
                print("Ce n'est ni un 'o' ni un 'n'. Veuillez recommencer.")
        except ValueError:
            print("Il faut une lettre!")

    FIRST_CHOICE = 0

    while FIRST_CHOICE != 2:
        LIST_SAVED_PRODUCT = []
        try:
            FIRST_CHOICE = int(input("Si vous souhaitez consulter vos favoris, tapez 1.\
            	\nSi vous souhaitez accéder à notre catalogue, tapez 2 :"))
            if FIRST_CHOICE == 2:
                DICT_CURSOR = {}
                SELECT_ID_NAME_CATEGORY = """SELECT id, name FROM category ORDER BY id """
                CURSOR.execute(SELECT_ID_NAME_CATEGORY)
                for int_id, str_name in CURSOR:
                    dico = {int_id:str_name}
                    DICT_CURSOR.update(dico)
                for int_id, str_name in DICT_CURSOR.items():
                    print("{} : {}".format(int_id, str_name))
            elif FIRST_CHOICE == 1:
                print("\nVoici vos produits sauvegardés :\n")
                SELECT_SAVED_PRODUCT = """SELECT Bad.name, Product.id,
                Product.name, Product.description, Product.url, Product.grade 
                FROM Fav_product
                INNER JOIN Product
                ON Product.id = Fav_Product.id_good_product
                INNER JOIN Product as Bad
                ON Bad.id = Fav_product.id_bad_product"""
                CURSOR.execute(SELECT_SAVED_PRODUCT)
                for bad_name, product_id, name, description, url, grade in CURSOR:
                    dico = {"name2" : bad_name, "id" : product_id, "name":name,\
                    "description":description, "url":url, "grade":grade}
                    LIST_SAVED_PRODUCT.append(dico)
                for dico in LIST_SAVED_PRODUCT:
                    print("\nProduit remplacé : {}\nProduit de remplacement:\
                    	\nNuméro d'identification : {}\nNom : {}\nURL : {}\nNote :\
                    	{}\n".format(dico["name2"], dico["id"], dico["name"],\
                    		dico["url"], dico["grade"].capitalize()))
            else: print("\nCe n'est ni un '1' ni un '2'. Veuillez recommencer.\n")
        except ValueError:
            print("\nIl faut entrer soit 1 soit 2.\n")

    CATEGORY_CHOICE = 0

    while CATEGORY_CHOICE < 1 or CATEGORY_CHOICE > 6:
        try:
            CATEGORY_CHOICE = int(input("Sélectionnez la catégorie dont vous\
souhaitez consulter les produits en saisissant son numéro."))
            if CATEGORY_CHOICE >= 1 and CATEGORY_CHOICE <= 6:
                LIST_BAD_PRODUCT, LIST_GOOD_PRODUCT = [], []
                CATEGORY_CHOICE_DICT = {"name":CATEGORY_CHOICE}
                SELECT_PRODUCT = """SELECT Product.id, Product.name, Product.description,
                Product.url, Product.grade FROM Product INNER JOIN Category_product 
                ON Product.id = Category_product.id_product 
                WHERE Category_product.id_category = %(name)s
                ORDER BY Product.id """
                CURSOR.execute(SELECT_PRODUCT, CATEGORY_CHOICE_DICT)
                for product_id, name, description, url, grade in CURSOR:
                    dico = {"id" : product_id, "name":name,\
                    "description":description, "url":url, "grade":grade}
                    if dico["grade"] in ("c", "d", "e"):
                        LIST_BAD_PRODUCT.append(dico)
                    else:
                        LIST_GOOD_PRODUCT.append(dico)
            else: print("Ce n'est pas le numéro d'une catégorie.\
            	Merci de saisir le numéro d'une catégorie.")
        except ValueError:
            print("Il faut entrer un numéro entre 1 et 5.")

    BEGIN = 0
    END = 5
    SPACE = 5
    NEXT_STEP = True
    LIST_SELECT, LIST_ID = [], []
    BAD_GOOD_PRODUCT_ID = {}
    while NEXT_STEP == True:
        for dico in LIST_BAD_PRODUCT[BEGIN:END]:
            LIST_SELECT.append(dico)
            LIST_ID.append(dico["id"])
            print("\nNuméro d'identification : {}\nNom : {}\nURL : {}\nNote : {}\n"\
            	.format(dico["id"], dico["name"], dico["url"], dico["grade"].capitalize()))
        try:
            SELECT_PRODUCT = int(input("Sélectionnez le produit que vous souhaitez remplacer\
en saisissant son numéro ou affichez les 5 prochains produits en cliquant sur 0."))
            if SELECT_PRODUCT == 0:
                BEGIN = BEGIN + SPACE
                END = END + SPACE
                if END >= len(LIST_BAD_PRODUCT):
                    print("Retour à la case départ!")
                    BEGIN = 0
                    END = 5
            elif SELECT_PRODUCT in LIST_ID:
                for dico in LIST_BAD_PRODUCT:
                    if SELECT_PRODUCT == dico["id"]:
                        print("\nVoici le produit que vous avez choisi :\
\nNuméro d'identification : {}\nNom : {}\nURL : {}\nNote : {}\nDescription : {}\n"\
.format(dico["id"], dico["name"], dico["url"], dico["grade"].\
capitalize(), dico["description"]))
                        NEXT_STEP = False
            else:
                print("\nCe n'est ni 0 ni un des numéros d'identifiants de produit,\
recommencez svp.\n")
        except ValueError:
            print("Ce n'est ni 0 ni un des numéros d'identifiants de produit, recommencez svp.")
        except TypeError:
            print("Il faut entrer un chiffre, recommencez svp.")

    END = int
    while END != 0:
        RANDOM_NUMBER = random.randrange(len(LIST_GOOD_PRODUCT))
        SELECT_GOOD_PRODUCT = LIST_GOOD_PRODUCT[RANDOM_NUMBER]
        print("Voici un produit de remplacement : Numéro d'identification :\
{}\nNom : {}\nURL : {}\nNote : {}\nDescription : {}\n".format\
        	(SELECT_GOOD_PRODUCT["id"], SELECT_GOOD_PRODUCT["name"], SELECT_GOOD_PRODUCT["url"],\
        	SELECT_GOOD_PRODUCT["grade"].capitalize(), SELECT_GOOD_PRODUCT["description"]))
        REPLACE_PRODUCT = input("Enregistrez le produit de remplacement en saisissant 'o'\
ou affichez un autre produit de remplacement en saisissant 'a'")
        if REPLACE_PRODUCT == "o":
            BAD_GOOD_PRODUCT_ID = {"id_bad_product" : dico["id"], \
            "id_good_product" :SELECT_GOOD_PRODUCT["id"]}
            ADD_REPLACE_PRODUCT = """INSERT IGNORE INTO Fav_product\
            (id_bad_product, id_good_product)\
            VALUES (%(id_bad_product)s, %(id_good_product)s)"""
            CURSOR.execute(ADD_REPLACE_PRODUCT, BAD_GOOD_PRODUCT_ID)
            CNX.commit()
            print("Le produit a bien été enregistré.")
            END = 0
        if REPLACE_PRODUCT == "a":
            pass

    TEST = input("Séléctionnez 1 pour terminer le programme et 2 pour retourner à l'accueil")
    if TEST == 1:
        pass
    if TEST == 2:
        MAINLOOP = 0
        print(MAINLOOP)