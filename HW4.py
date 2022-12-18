age = input ('Enter your age: ') 

if age.isdigit():
    age = int(age)
    if age % 2 == 0:
        print ("It is double number")
    else:
        print ("It is unpaired number")
else:
    print ("Length is ", len(age), " characters.")

   