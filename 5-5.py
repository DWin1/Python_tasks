'''Создать (программно) текстовый файл, записать в него программно набор чисел,
разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.'''

from functools import reduce

with open("5-5.txt", "w") as my_file:
    my_str = input('Введите числа через пробел >> ')
    my_file.write(my_str)

with open("5-5.txt", "r") as my_file:
    content = my_file.read()
    content = content.split(' ')
    print(content)

my_list = list()

for el in content:
    el = int(el)
    my_list.append(el)

def my_reduce(prev_el, el):
    return prev_el + el

print(f"Сумма чисел в файле {reduce(my_reduce, my_list)}")