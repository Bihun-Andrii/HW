import sqlite3
from pprint import pprint

db = sqlite3.connect("book_store.sqlite")
cursor = db.cursor()

query = ('SELECT users.id, users.first_name, users.first_name, books.title '
'FROM purchase JOIN users on purchase.user_id=users.id '
'JOIN books on purchase.book_id=books.id '
'ORDER BY users.id')

res=cursor.execute(query)
pprint(res.fetchall())

# 3. Написати запит, який виведе всіх users і назви  всіх книжок, які вони купували, відсортувати дані за user_id. 
#    Результат має бути представлений у форматі: users.id, users.first_name, users.last_name, books.title