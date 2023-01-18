from datetime import datetime

def my_deco (func):
    def wrap(*args, **kwargs):
        func(*args, **kwargs)
    return wrap 

@my_deco
def my_func(funk_name='My function', start_time=datetime.now()):
    enter = input ('Press "Enter" to start a function ')
    print(f'{funk_name} was started on {start_time}')
 
my_func()

#Написати власний декоратор, задачею якого має бути друк назви функції і часу, 
# коли вона була викликана. Декоратор має працювати для різних функцій однаково
