from datetime import datetime

def my_deco (func):
    def wrap():
        func()
        print(f'Function {func} was called on {datetime.now()}')
    return wrap 

@my_deco
def my_func():
    enter = input ('Press "Enter" to start a function ')
 
my_func()

#Написати власний декоратор, задачею якого має бути друк назви функції і часу, 
# коли вона була викликана. Декоратор має працювати для різних функцій однаково
