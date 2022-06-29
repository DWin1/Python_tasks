'''1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта
заработной платы сотрудника. Используйте в нём формулу:
(выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать
скрипт с параметрами'''

from sys import argv

f_obj, bonus_v, rate_v, hours_v = argv


def salary(hour, money, bonus):
    try:
        print(f'Сотрудник заработал {int(money) * int(hour) * (1 + int(bonus) / 100)}')
    except TypeError:
        print('Введены неверные данные')
        exit()


salary(hours_v, rate_v, bonus_v)
