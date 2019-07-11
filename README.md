# OpenFoodFact

Use OpenFoodFact data to offer alternative products.

Purpose
-----------------
This is a student project for OpenClassroom Python course. 

We want to suggest the user healthy products instead of unhealthy food.

Features
-----------------

* The user can choose between viewing his registered products or substitute other products.
* The system shows products categories.
* The user picks up a category.
* The system shows the products of the category.
* In the category, the user selects the product he wants to change.
* The system shows the healthy product to substitute.
* The user can register the healthy product in his database.
* The user can view his registered products.

Tech/framework used
-----------------
Python 3.7
MySQL
[OpenFoodFact API](https://en.wiki.openfoodfacts.org/API)

Description
-----------------

* main.py : to launch the programm.
* loop_class.py : all the interactions between the user and the programm.
* db_connect_class.py : all the interactions with the databse (insert, select).
* request_class.py : to request, parse and organize the datas from OpenFoodFact API.
* request_insert_url_class.py : for each url from OpenFoodFact API, select and insert the data in the database.
* erase_class.py : reset the database.
* constants.py : All the constants, select request and sentences for the users are here.
