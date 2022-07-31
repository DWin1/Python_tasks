'''Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.'''


class ZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


a = 100
b = 10

try:
    if b == 0:
        raise ZeroDivisionError("На ноль делить нельзя")
except ValueError:
    print("Вы ввели не число!")
except ZeroDivisionError as err:
    print(err)
else:
    print(a / b)
