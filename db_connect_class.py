'''This class connects the project to the database'''
import pwd

import mysql.connector


class Db_connect:
    '''The select and the insert to
    the database are in the following methods'''

    def __init__(self):
        self.cnx = mysql.connector.connect(user=pwd.user,
                                           password=pwd.password,
                                           host="localhost",
                                           database="healthy_food")
        self.cursor = self.cnx.cursor()
        self.dict_cursor = {}

    def insert(self, query, values_list):
        '''Insert data in the databse'''
        self.cursor.executemany(query, values_list)
        self.cnx.commit()

    def select(self, query):
        '''Select data from the database
        and insert them in a dictionnary'''
        self.dict_cursor = {}
        self.cursor.execute(query)
        for int_id, str_name in self.cursor:
            dico = {int_id: str_name}
            self.dict_cursor.update(dico)

    def close(self):
        '''Close cursor'''
        self.cursor.close()
        self.cnx.close()
