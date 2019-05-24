import requests
 
object_json = requests.get('https://fr.openfoodfacts.org/categorie/popcorn_sucre.json')
object_json = object_json.json()

ma_liste = object_json['products']
mon_dictionnaire = ma_liste[0]

for cle, valeur in mon_dictionnaire.items():
	if cle == 'product_name' or cle == 'nutrition_grades' or cle == 'stores' or cle == 'ingredients' or cle == 'categories':
		info_product = {
		"product_name":mon_dictionnaire['product_name'],
		"nutrition_grades":mon_dictionnaire['nutrition_grades'],
		"stores":mon_dictionnaire['stores'],
		"ingredients":mon_dictionnaire['ingredients'],
		"categories":mon_dictionnaire['categories']
		}

print(info_product)