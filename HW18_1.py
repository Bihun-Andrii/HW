class Bot:
    def __init__(self, name):
        self.name = name
       
    def say_name(self):
        print(self.name)

    def send_message (self, message):
        self.message = message
        print(self.message)

some_bot = Bot('Marvin')
some_bot.say_name()
some_bot.send_message('Hello')

# 1. Створити клас Bot з атрибутом name та методами say_name та send_message. 
# send_message має приймати параметри self і message і має друкувати message. 
# Метод say_name має друкувати значення атрибуту name.