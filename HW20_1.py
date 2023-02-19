import sqlite3
connection = sqlite3.connect('DB.db')
cursor = connection.cursor()
query = ('CREATE TABLE my_table ('
         'id INTEGER PRIMARY KEY AUTOINCREMENT,'
         'first_name TEXT,'
         'last_name TEXT,'
         'age INTEGER)')
cursor.execute(query)



