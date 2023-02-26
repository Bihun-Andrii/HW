from datetime import datetime

def log_function (func):
    def wrap(*args, **kwargs):
        with open("My_log.txt", 'w') as file:
            file.write(f'{func.__name__} was started on {datetime.now()}') 
        return func(*args, **kwargs)
    return wrap

@log_function
def my_funс():
   pass

my_funс()
    
#2. Написати декоратор, який буде записувати в файл назву функції, 
# яку він декорує, і писати час її виклику.

