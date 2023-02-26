from datetime import datetime

class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        self.log_error()

    def log_error(self):
        start_time = datetime.now()
        with open('error_log.txt', 'w') as file:
            file.write(f'{start_time}: {self.message}')

raise MyCustomException("Custom exception is occurred")

# Написати кастомний Exception клас, MyCustomException, який має повідомляти "Custom exception is occured".
# В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл.