import sqlite3
connection = sqlite3.connect('DB.db')
cursor = connection.cursor()
query = ('INSERT INTO my_table (first_name, last_name, age) '
         'values ("Andrey", "Bihun", 42)')
cursor.execute(query)
connection.commit()

data = [
    ('Igor', 'Fdsfs', 33),
    ('Maksim', 'Yhgfg', 29),
    ('Denis', 'Wwerer', 22),
    ('Vova', 'Jghggh', 12),
]
query = ('INSERT INTO my_table (first_name, last_name, age) '
         'values (?, ?, ?)')

cursor.executemany(query, data)
connection.commit()