''' Продолжить работу над заданием. В программу должна попадать строка из слов,
разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее функцию int_func()'''


my_word = input('Введите слова >> ').split()

def upper1(arg1):
    list1 = list(arg1)
    len1 = len(list1)
    for i in range(len1):
        list1[i] = list1[i].capitalize()
    my_str = (' ').join(list1)
    return my_str

print(upper1(my_word))