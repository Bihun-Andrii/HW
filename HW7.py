phone_book = {
    'Igor': 132434,
    'Diana': 254345,
}

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
        if name in phone_book:
           print(f"{name} is exist, please enter another name")
        else:
            phone_book[name] = number
            print (phone_book.keys())
        
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
        print (phone_book[name])    

#Створити телефонну книгу, яка матиме наступні команди:
#stats: кількість записів
#add: додати запис
#delete <name>: видалити запис за іменем (ключем)
#list: список всіх імен в книзі
#show <name>: детальна інформація по імені
#Записи не мають повторюватися, заборонено перезаписувати записи, тільки видаляти і додавати заново.    