my_dict = {
    'Diana': 254345,
    'Igor':38574
    }
counter = 3

while True and counter:
    name = input('Enter a name: ')
    print("1==========")
    
    try:
        value = my_dict[name]
    except KeyError:
        print(f'Key {name} does not exist')
        print("2==========")
    else:
        print(f'Phone number is {value}')
        print("2==========")
    finally:
        counter -=1
        print('End of program')

print ('You reached limit')

#Написати конструкцію try ... except ... else ... finally, 
# яка буде робити точно те ж, що і менеджер контексту із попереднього завдання.


        

  

   
   
  







#Написати конструкцію try ... except ... else ... finally, яка буде робити точно те ж,
# що і менеджер контексту із попереднього завдання.