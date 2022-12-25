phone_book = {
    'Igor': 132434,
    'Diana': 254345,
}

print (phone_book.keys())

while True:
    user_input = input('Enter a command: ')
    split_input = user_input.split()
   
    command = split_input[0]
    name = split_input[1]
    number = split_input[2]
 
    if phone_book.get(name) is None:  #тут у мене щось не виходить - як зробити, щоб можно було ввести лише command?
        phone_book[name] = 0
        
    if command == 'stats':
        print(len(phone_book))

    elif command == 'add':
        phone_book[name] = number
        print (phone_book.keys())
        
    elif command == 'delete':
        del phone_book[name]
        print(phone_book.keys())
    
    elif command == 'list':
        print (phone_book.keys())

    elif command == 'show':
        for key, value in phone_book.items():
            print (key)
            print(value) 

#Створити телефонну книгу, яка матиме наступні команди:
#stats: кількість записів
#add: додати запис
#delete <name>: видалити запис за іменем (ключем)
#list: список всіх імен в книзі
#show <name>: детальна інформація по імені
#Записи не мають повторюватися, заборонено перезаписувати записи, тільки видаляти і додавати заново.    