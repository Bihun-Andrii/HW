from datetime import datetime

def my_deco (func):
    def wrap(*args, **kwargs):
        return func(*args, **kwargs)
    return wrap
      

@my_deco
def my_func(funk_name='My function', start_time=datetime.now()):
    enter = input ('Press "Enter" to start a function ')
    print(f'{funk_name} was started on {start_time}')
    file = open(r'C:\01_Education\03_IT\04_Pyhon\Laba\HW\My_function.txt', "w")
    file.write(f'{funk_name} was started on {start_time}') 
    
 
my_func()

#2. Написати декоратор, який буде записувати в файл назву функції, 
# яку він декорує, і писати час її виклику.
