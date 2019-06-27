class Product:

	def __init__(self, name, description, grade, favorite, categories, stores):
		self.name = name
		self.description = description
		self. grade = grade
		self.favorite = favorite
		self.categories = categories
		self.stores = stores

class Category:

	def __init__(self, name, products):
		self.name = name
		self.products = products

class Store:

	def __init__(self, name, adress, products):
		self.name = name
		self.adress = adress
		self.products = products