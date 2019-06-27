import requests
import mysql.connector

cnx = mysql.connector.connect(user='root', password='Ln19221418!',
                              host='localhost',
                              database='healthy_food')

cursor = cnx.cursor()
 
class Insert:

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
		for key, value in dico.items():
				if dico.get('stores') and dico.get('categories') and dico.get('product_name') and dico.get('nutrition_grades'):
					info_product = {
						"nom":dico['product_name'],
						"grade":dico['nutrition_grades'],
						"description":dico['ingredients_text_debug'],
						"url":dico['url'],
						}
					foods.append(info_product)
					


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
