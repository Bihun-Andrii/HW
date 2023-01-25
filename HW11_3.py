class MyContextManager:
    def __enter__(self):
        print("1==========")
    
    def __exit__(self, exc_type, exc_val, exc_tb):
                     
        if exc_type == KeyError:
            print(f'Key {name} does not exist')
            print("2==========")
            
        else:
            print(f'Phone number is {value}')
            print("2==========")
        return True
       
my_dict = {
    'Diana': 254345,
    'Igor':38574
    }

with MyContextManager():
    name = input('Enter a name: ')
    value = my_dict[name]    

print('End of program')
     
#Написати власний менеджер контексту, задачею якого буде друкувати "==========" – 
# 10 знаків дорівнює перед виконанням коду та після виконання коду, 
# таким чином виділяючи блок коду символами дорівнює.
# У випадку виникнення будь-якої помилки вона має бути надрукована текстом, 
# проте програма не має завершити своєї роботи.