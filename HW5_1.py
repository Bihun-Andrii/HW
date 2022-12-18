value = input ('Please enter something: ') 
for simbol in value:   
    if simbol.isdigit():
        simbol = int(simbol)
        if simbol % 2 == 0:
            print (f"{simbol} - it is double number")
        else:
            print (f"{simbol} - it is unpaired number")
    elif simbol.islower():
        print (f"{simbol} - it is small letter")
    elif simbol.isupper():
        print (f"{simbol} - it is capital letter")
    else:
        print (f"{simbol} - it is simbol")