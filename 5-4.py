'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл.'''

with open("5-4.txt", "r") as my_file:
    content = my_file.readlines()
    my_dict = dict(Zero='Ноль', One='Один', Two='Два', Three='Три', Four='Четыре', Five='Пять',
               Six='Шесть', Seven='Семь', Eight='Восемь', Nine='Девять', Ten='Десять')
    my_list = list()
    my_list1 = list()
    for el in content:
        el = el.split(' ')
        my_list.append(el)
    for el in my_list:
        el[0] = my_dict.get(el[0])
        el = ' '.join(el)
        my_list1.append(el)

with open("5-4-1.txt", "w") as new_file:
    new_file.writelines(my_list1)



