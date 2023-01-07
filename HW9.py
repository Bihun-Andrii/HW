def my_generator(size):
    a,b = 0,1
    for _ in range (size):
        yield a
        a,b = b, a+b
size = int(input('Please enter quantity of numbers for the Fibonacci sequence: '))
print (list (my_generator(size)))