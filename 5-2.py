'''Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.'''

my_file = open("5-2.txt", "r")
content = my_file.readlines()
print(content)
my_lines = len(content)
print(f"Количество строк: {my_lines}")
i = 1
for el in content:
        word = len(el) - 1
        print(f"{i} строка: {word} букв(ы)")
        i +=1
