import requests
import mysql.connector
import re

cnx = mysql.connector.connect(user='xx', password='xx',
                              host='localhost',
                              database='healthy_food')

cursor = cnx.cursor()

class Insert:

	def __init__(self, url):
		self.url = url
		self.foods, self.store, self.unique_store, self.list_dict_id_store_product = [], [], [], []
		self.key_store = str

	def request(self):
		object_json = requests.get(self.url)
		object_json = object_json.json()
		list_clean = object_json['products']
		for dico in list_clean:
			if dico.get('stores') and dico.get('categories') and dico.get('product_name') and dico.get('nutrition_grades'):
				for key, value in dico.items():
					info_product = {
						"nom":dico['product_name'],
						"grade":dico['nutrition_grades'],
						"description":dico['ingredients_text_debug'],
						"url":dico['url'],
						"category":dico['categories'],
						"store":dico['stores'],
						}
				self.foods.append(info_product)
		print(self.foods)

	def insert_category(self):
		category = ['Sucettes'], ['Marshmallows'], ['Cookies au chocolat'], ['Assortiments de chocolats'], ['Pizzas aux trois fromages'], ['Chips paysannes'], ['Chips au sel et vinaigre']
		add_category = ("INSERT IGNORE INTO category "
              "(nom) "
              "VALUES (%s)")
		cursor.executemany(add_category, category)
		cnx.commit()

	def insert_product(self):
		add_product = """INSERT IGNORE INTO product (nom, description, url, grade) VALUES (%(nom)s, %(description)s, %(url)s, %(grade)s)"""
		cursor.executemany(add_product, self.foods)
		cnx.commit()
	
	def request_store(self):
		for i, first_value in enumerate(self.foods):
			stores_product = {"nom":first_value["store"]}
			for key_store, value_store in stores_product.items():
				value_store = re.sub(", ",",",value_store)
				value_store = value_store.split(',')
			for i, final_value in enumerate(value_store):
				stores ={"nom":final_value}
				unique_store ={final_value:first_value["nom"]}
			self.store.append(stores)
			self.unique_store.append(unique_store)

	def insert_store(self):
		add_store = """INSERT IGNORE INTO store (nom) VALUES (%(nom)s)"""
		cursor.executemany(add_store, self.store)
		cnx.commit()

	def insert_store_product(self, query, liste):
		self.list_dict_id_store_product = []
		self.dict_id_nom_store = {}
		self.dict_id_store_product = {}
		cursor.execute(query)
		for int_id, str_nom in cursor:
			dico = {int_id:str_nom}
			self.dict_id_nom_store.update(dico)
		for dict_store in liste:
			for key_store, value_product in dict_store.items():
				for int_id2, str_nom2 in self.dict_id_nom_store.items():
					if key_store == str_nom2:
						self.dict_id_store_product = {int_id2 : value_product}
			self.list_dict_id_store_product.append(self.dict_id_store_product)
		
	def insert_store_product2(self, query, liste):
		self.list_dict_id_store_product = []
		self.dict_id_nom_store = {}
		self.dict_id_store_product = {}
		cursor.execute(query)
		for int_id, str_nom in cursor:
			dico = {int_id:str_nom}
			self.dict_id_nom_store.update(dico)
		for dict_store in liste:
			for key_store, value_product in dict_store.items():
				for int_id2, str_nom2 in self.dict_id_nom_store.items():
					if value_product == str_nom2:
						self.dict_id_store_product = {"id_store":key_store, "id_product":int_id2}
			self.list_dict_id_store_product.append(self.dict_id_store_product)

	def insert_store_product3(self):
		add_store_product = """INSERT IGNORE INTO Store_product (id_store, id_product) VALUES (%(id_store)s, %(id_product)s)"""
		cursor.executemany(add_store_product, self.list_dict_id_store_product)
		cnx.commit()

	def request_category(self):
		self.categories, self.unique_category = [], []
		for i, first_value in enumerate(self.foods):
			categories_product = {"nom":first_value["category"]}
			for key_store, value_category in categories_product.items():
				value_category = re.sub(", ",",",value_category)
				value_category = value_category.split(',')
			for i, final_value in enumerate(value_category):
				unique_category ={final_value:first_value["nom"]}
				self.unique_category.append(unique_category)

	def insert_category_product(self):
		self.dict_id_nom_category, self.dict_id_category_product = {}, {}
		self.list_dict_id_category_product = []
		select_id_nom_category = """SELECT id, nom FROM category """
		cursor.execute(select_id_nom_category)
		for int_id, str_nom in cursor:
			dico = {int_id:str_nom}
			self.dict_id_nom_category.update(dico)
		for dict_category in self.unique_category:
			for key_category, value_product in dict_category.items():
				for int_id2, str_nom2 in self.dict_id_nom_category.items():
					if key_category == str_nom2:
						self.dict_id_category_product = {int_id2 : value_product}
						self.list_dict_id_category_product.append(self.dict_id_category_product)

	def insert_category_product2(self):
		self.dict_id_nom_category = {}
		self.dict_id_category_product = {}
		self.list_dict_id_category_product_final = []
		select_id_nom_category = """SELECT id, nom FROM product """
		cursor.execute(select_id_nom_category)
		for int_id, str_nom in cursor:
			dico = {int_id:str_nom}
			self.dict_id_nom_category.update(dico)
		for dict_category in self.list_dict_id_category_product:
			for key_store, value_product in dict_category.items():
				for int_id2, str_nom2 in self.dict_id_nom_category.items():
					if value_product == str_nom2:
						self.dict_id_category_product = {"id_category":key_store, "id_product":int_id2}
						self.list_dict_id_category_product_final.append(self.dict_id_category_product)

	def insert_category_product3(self):
		add_category_product = """INSERT IGNORE INTO Category_product (id_category, id_product) VALUES (%(id_category)s, %(id_product)s)"""
		cursor.executemany(add_category_product, self.list_dict_id_category_product_final)
		cnx.commit()

 
 
 
