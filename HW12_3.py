from datetime import datetime

class MyCustomException (Exception):
    start_time=datetime.now()
    file = open(r'C:\01_Education\03_IT\04_Pyhon\Laba\HW\My_log.txt', "w")
    file.write(f'{Exception} was occured on {start_time}')
    pass
 
raise MyCustomException('Custom exception is occured')

# Написати кастомний Exception клас, MyCustomException, який має повідомляти "Custom exception is occured".
# В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл.
