'''Main file'''

import loop_class
import db_connect_class
import constants

MAINLOOP = 0
while MAINLOOP != 1:
    LAST = 0
    LOOP = loop_class.Loop()
    LOOP.reboot()
    LOOP.category_fav_choice()
    LOOP.category()
    LOOP.product(LOOP.list_bad_product)
    LOOP.fav(LOOP.list_good_product, LOOP.bad_good_product_id, LOOP.id_bad)
    while LAST not in(1, 2):
        try:
            LAST = int(input(constants.end_programm))
            assert LAST in (1, 2)
        except ValueError:
            print("Il faut entrer un numéro.\n")
        except AssertionError:
            print("Ce n'est ni un '1' ni un '2'. Veuillez recommencer.\n")
        if LAST == 1:
            MAINLOOP = 1

DB = db_connect_class.Db_connect()
DB.close()
