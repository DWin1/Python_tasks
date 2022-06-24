'''6. Реализовать функцию int_func(), принимающую слова из маленьких
латинских букв и возвращающую их же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.'''

my_word = input('Введите слова >> ').split()

def upper1(arg1):
    list1 = list(arg1)
    len1 = len(list1)
    for i in range(len1):
        list1[i] = list1[i].capitalize()
    my_str = (' ').join(list1)
    return my_str

print(upper1(my_word))
