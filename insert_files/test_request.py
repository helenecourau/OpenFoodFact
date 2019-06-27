import requests
import mysql.connector

cnx = mysql.connector.connect(user='xx', password='xx',
                              host='localhost',
                              database='healthy_food')

cursor = cnx.cursor()
 
'''class Insert:

	def __init__(self, url):
		self.url = url
		self.list_clean = []

	def request(self):
		global info_product
		info_product = {}
		foods = []
		object_json = requests.get(self.url)
		object_json = object_json.json()
		self.list_clean = object_json['products']
		for dico in self.list_clean:
			for key, value in dico.items():
				if dico.get('stores') and dico.get('categories') and dico.get('product_name') and dico.get('nutrition_grades'):
					info_product = {
						"nom":dico['product_name'],
						"grade":dico['nutrition_grades'],
						"description":dico['ingredients_text_debug'],
						"url":dico['url'],
						}
					foods.append(info_product)'''

def insert_store_product(self):
		list_dict_id_store_product = []
		list_dict_id_store_product2 = []
		dict_id_nom_store = {}
		dict_id_nom_store2 = {}
		select_id_nom_store = """SELECT id, nom FROM store """
		cursor.execute(select_id_nom_store)
		for int_id, str_nom in cursor:
			dico = {int_id:str_nom}
			dict_id_nom_store.update(dico)
		for dict_self_store2 in self.unique_store:
			for key_store, value_product in dict_self_store2.items():
				for int_id2, str_nom2 in dict_id_nom_store.items():
					if key_store == str_nom2:
						dict_id_store_product = {int_id2 : value_product}
				list_dict_id_store_product.append(dict_id_store_product)
		'''query2 = """SELECT id, nom FROM product """
		cursor.execute(query2)
		for int_id, str_nom in cursor:
			dico = {int_id:str_nom}
			dict_id_nom_store2.update(dico)
		for dict_self_store2 in list_dict_id_store_product:
			for key_store, value_product in dict_self_store2.items():
				for int_id2, str_nom2 in dict_id_nom_store.items():
					if value_product == str_nom2:
						dict_id_store_product = {int_id2 : int_id}
				list_dict_id_store_product2.append(dict_id_store_product)	
		print(list_dict_id_store_product2)'''

insert_store_product()
print(foods)
					


'''cnx.commit()

cursor.close()
cnx.close()'''

'''https://fr.openfoodfacts.org/categorie/sucettes
https://fr.openfoodfacts.org/categorie/guimauves
https://fr.openfoodfacts.org/categorie/cookies-au-chocolat
https://fr.openfoodfacts.org/categorie/assortiments-de-chocolats
https://fr.openfoodfacts.org/categorie/pizzas-aux-trois-fromages
https://fr.openfoodfacts.org/categorie/chips-paysannes
https://fr.openfoodfacts.org/categorie/chips-au-sel-et-vinaigre'''
