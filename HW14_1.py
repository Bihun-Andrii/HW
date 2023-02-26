phone_book = {
    'Igor': 132434,
    'Diana': 254345,
}

import json
import re

json_data = json.dumps(phone_book)
with open (r'C:\01_Education\03_IT\04_Pyhon\Laba\HW\phone_book.txt', 'a') as file:
    file.write(json_data)

print (phone_book.keys(),phone_book.values())

while True:
    user_input = input('Enter a command: ')
    split_input = user_input.split()
   
    command = split_input[0]
    
    if len(split_input) > 1:
        name = split_input[1]
    else:
        name = None

    if len(split_input) > 2:
        number = split_input[2]
    else:
        number = None      
    
    if command == 'stats':
        print(len(phone_book))

    elif command == 'add':
        check_phone = re.match(r'\+380\d{9}$|380\d{9}$|0\d{9}$', number)
        
        if name in phone_book:
           print(f"{name} is exist, please enter another name")
        else:
            if check_phone:
                print("Corect phone format")
                phone_book[name] = number
                print (phone_book.keys())
            else:
                print("Incorect phone format")
          
    elif command == 'delete':
        if phone_book.get(name) == None:
           print(f"{name} is missing, please enter an existing name")
        else:
           del phone_book[name]
           print(phone_book.keys())
    
    elif command == 'list':
        if len(split_input) == 1:
           name = None
           print (phone_book.keys())

    elif command == 'show':
        if phone_book.get(name) == None:
           print(f"{name} is not available in the phone book, please enter another name")   
        else: print (phone_book[name])    


# 1. До завдання, в якому ви реалізовували телефонну книгу, 
# додати валідацію номера телефону за допомогою RegEx. 
# Врахувати можливість декількох форматів: +380XXXXXXXXX, 380XXXXXXXXX, 0XXXXXXXXX
    