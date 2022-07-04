'''Создать текстовый файл (не программно). Построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет
оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней
величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32'''

from statistics import mean

try:
    my_file = open("5-3.txt", "r")
    content = my_file.readlines()
    my_list = list()
    line_list = list()
    salary = list()
    for el in content:
        el = el.replace(' \n', '')
        line_list = el.split(' ')
        my_list.extend(line_list)

    for i in range(1, len(my_list), 2):
        my_list[i] = float(my_list[i])
        salary.append(my_list[i])
        if my_list[i] < 20000:
            print(f"Оклад сотрудника {my_list[i - 1]} менее 20 000 р.")

    print(salary)
    salary1 = mean(salary)
    print(f"Средний оклад {salary1} р.")

except IOError:
    print("Произошла ошибка ввода-вывода!")
