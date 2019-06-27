import mysql.connector
import pwd

cnx = mysql.connector.connect(user=pwd.user, password= pwd.password,
                              host='localhost',
                              database='healthy_food')

cursor = cnx.cursor()

def erase():
	cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
	cursor.execute("TRUNCATE Category")
	cursor.execute("TRUNCATE Product")
	cursor.execute("TRUNCATE Store")
	cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

erase()