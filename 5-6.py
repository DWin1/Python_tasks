'''Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}'''

from functools import reduce
def sum_list(prev_el, el):
    return int(prev_el) + int(el)

with open("5-6.txt", "r") as my_file:
    my_dict = {}
    for line in my_file:
        key, *value = line.split()
        my_dict[key] = value
    print(my_dict)

for el in my_dict:
    el1 = my_dict[el]
    value_replace = []
    for el2 in el1:
        if el2 == '—':
            el1.remove('—')
    print(f"el1 {el1}")
    for el2 in el1:
        el3 = el2
        print(f"el3 {el3}")
        el3 = el3.split('(')
        print(f"el3 {el3}")
        el3.pop(1)
        value_replace.extend(el3)
    el1.clear()
    el1.extend(value_replace)

my_dict1 = my_dict.copy()
print('my_dict1', my_dict1)
for el in my_dict1:
    el1 = my_dict[el]
    print("el1", el1)
    el2 = reduce(sum_list, el1)
    print("el2", el2)
    el1.clear()
    el1.append(el2)
print(my_dict1)
#не получилось заменить в словаре список на строку



