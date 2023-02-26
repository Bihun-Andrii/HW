import sqlite3
from pprint import pprint

connection = sqlite3.connect("Base_21.sqlite")
cursor = connection.cursor()

query = ('SELECT COUNT(id) FROM users WHERE age > 30')
res = cursor.execute(query)
pprint(res.fetchall()) 

#2. Написати sql запит, який виведе кількість записів в табліці users, що старше 30 років.