import sqlite3
from pprint import pprint

db = sqlite3.connect("DB_store.sqlite")
cursor = db.cursor()

table_users = ('CREATE TABLE IF NOT EXISTS users ('
         'id INTEGER PRIMARY KEY AUTOINCREMENT,'
         'first_name TEXT,'
         'last_name TEXT,'
         'age INTEGER NOT NULL)')

table_publishing_house = ('CREATE TABLE IF NOT EXISTS publishing_house ('
         'id INTEGER PRIMARY KEY AUTOINCREMENT,'
         'name TEXT,'
         'rating INTEGER default 5 )')
         
table_books = ('CREATE TABLE IF NOT EXISTS books ('
         'id INTEGER PRIMARY KEY AUTOINCREMENT,'
         'title TEXT,'
         'author TEXT,'
         'year INTEGER NOT NULL,'
         'price INTEGER NOT NULL,'
         'publishing_house_id,'
         'FOREIGN KEY (publishing_house_id) references publishing_house(id) )')
                
table_purchases = ('CREATE TABLE IF NOT EXISTS purchases ('
         'id INTEGER PRIMARY KEY AUTOINCREMENT,'
         'user_id,'
         'book_id,'
         'date INTEGER NOT NULL,'
         'FOREIGN KEY (user_id) references users(id),'
         'FOREIGN KEY (book_id) references books(id) )')

cursor.execute(table_users)
cursor.execute(table_publishing_house)
cursor.execute(table_books)
cursor.execute(table_purchases)

#1. Для обліку інформації про користувачів, книжки, видавництва та продажі створити наступні таблиці:
# users: id, first_name, last_name, age
# publishing_house: id, name, rating (default 5)
# books: id, title, author, year, price, publishing_house_id
# purchases: id, user_id, book_id, date

# При цьому:
# publishing_house_id — це FOREIGN KEY таблиці publishing_houses
# user_id —  це FOREIGN KEY таблиці users
# book_id —  це FOREIGN KEY таблиці books