import sqlite3
from pprint import pprint

connection = sqlite3.connect("Base_21.sqlite")
cursor = connection.cursor()

query = ('SELECT age as Age, COUNT(age) as Users FROM users GROUP by age')
res = cursor.execute(query)
pprint(res.fetchall()) 

#3. Написати sql запит, який виведе інформацію про вік (кількість років)
#   та кількість користувачів, які відповідають цьому віку.