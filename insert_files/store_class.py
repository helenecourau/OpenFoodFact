'''This class inserts the stores data in the store table of the database.
It relies on the list from split_class'''
import pwd

import mysql.connector

CNX = mysql.connector.connect(user=pwd.user, password=pwd.password,
                              host="localhost",
                              database="healthy_food")

CURSOR = CNX.cursor()

class Store:

    def __init__(self, store_list):
        self.store_list = store_list

    def insert_store(self):
        add_store = """INSERT IGNORE INTO store (name) VALUES (%(name)s)"""
        CURSOR.executemany(add_store, self.store_list)
        CNX.commit()