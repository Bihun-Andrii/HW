import sqlite3
from pprint import pprint

db = sqlite3.connect("book_store.sqlite")
cursor = db.cursor()

query = ("SELECT purchase.id, purchase.date, users.first_name, users.first_name "
"FROM purchase LEFT JOIN users on purchase.user_id=users.id")

res=cursor.execute(query)
pprint(res.fetchall())

# 2. Написати запит, який виведе дату покупки і імʼя користувача, що її здійснив. 
#    Результат має бути представлений у форматі: purchases.id, purchases.date, user.first_name, user.last_name