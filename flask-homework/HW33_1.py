from flask import Flask
import random

app = Flask(__name__)

def generate_random_names(num_names):
    names = ['Name1', 'Name2', 'Name3', 'Name4', 'Name5']
    random_names = random.sample(names, num_names)
    return random_names

@app.route('/users')
def get_users():
    random_names = generate_random_names(3) 
    return '\n'.join(random_names)

def generate_random_books(num_books):
    books = ['Book_name1', 'Book_name2', 'Book_name3', 'Book_name4', 'Book_name5']
    random_books = random.sample(books, num_books)
    html_list = '<ul>\n'
    for book in random_books:
        html_list += f'<li>{book}</li>\n'
    html_list += '</ul>'
    return html_list

@app.route('/books')
def get_books():
    random_books_html = generate_random_books(3)
    return random_books_html

if __name__ == '__main__':
    app.run(debug=True)

# Створити функції для обробки таких запитів:
# GET /users – має повертати рандомний список імен (будь-яку кількість)
# GET /books – має повертати рандомний список книжок (будь-яку кількість) у вигляді html списку