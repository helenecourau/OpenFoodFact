'''Used by request_insert_url_class to clear the database'''
import pwd
import mysql.connector

CNX = mysql.connector.connect(user=pwd.user, password=pwd.password,
                              host="localhost",
                              database="healthy_food")

CURSOR = CNX.cursor()

def erase():
    '''Clear all the database'''
    CURSOR.execute("SET FOREIGN_KEY_CHECKS = 0")
    CURSOR.execute("TRUNCATE Category")
    CURSOR.execute("TRUNCATE Product")
    CURSOR.execute("TRUNCATE Store")
    CURSOR.execute("TRUNCATE Store_product")
    CURSOR.execute("TRUNCATE Category_product")
    CURSOR.execute("TRUNCATE Fav_product")
    CURSOR.execute("SET FOREIGN_KEY_CHECKS = 1")