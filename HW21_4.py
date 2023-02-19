import sqlite3
from pprint import pprint

connection = sqlite3.connect("Base_21.sqlite")
cursor = connection.cursor()

query = ('SELECT age as Age, COUNT(age) as Users '
         'FROM users GROUP by age ORDER BY Users desc, Age desc')
res = cursor.execute(query)
pprint(res.fetchall()) 

#4. Написати sql запит, який буде робити те саме, що і в завданні 3, 
#   але виводити дані відсортовані по кількості користувачів у спадаючому порядку
#   та по віку у зростаючому порядку.