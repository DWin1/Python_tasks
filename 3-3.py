'''Реализовать функцию my_func(), которая принимает три позиционных
аргумента и возвращает сумму наибольших двух аргументов.'''

a = int(input('Введите первое число >> '))
b = int(input('Введите первое число >> '))
c = int(input('Введите первое число >> '))


def my_func(arg1, arg2, arg3):
    if arg1 >= arg2:
        max1 = arg1
        if arg2 >= arg3:
            max2 = arg2
        else:
            max2 = arg3
        #max2 = arg2 if arg2 >= arg3 else max2 = arg3 - опять ошибка в тернарном операторе?
    else:
        max1 = arg2
        if arg1 >= arg3:
            max2 = arg1
        else:
            max2 = arg3
    res = max1 + max2
    return res

print(f"Сумма наибольших двух чисел {my_func(a, b, c)}")