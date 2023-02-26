import sqlite3
from pprint import pprint

connection = sqlite3.connect("Base_21.sqlite")
cursor = connection.cursor()

query = ('SELECT * FROM users WHERE age > 30')
res = cursor.execute(query)
pprint(res.fetchall()) 

#1. Написати sql запит, який вибере усі записи із таблиці users старше 30 років.