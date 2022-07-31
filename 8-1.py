'''Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
@staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.'''


class Date():

    @classmethod
    def to_int(cls, self):
        date1 = self.split('-')
        day = int(date1[0])
        month = int(date1[1])
        year = int(date1[2])
        print(f"Введенная дата {day}.{month}.{year}")


    @staticmethod
    def valid(my_date):
        date1 = my_date.split('-')
        day = int(date1[0])
        month = int(date1[1])
        year = int(date1[2])
        if day > 31:
            print('Введен некорректный день')
        elif month > 12:
            print ('Введен некорректный месяц')
        else:
            print('Дата корректна')


d = '30-20-2020'
my_date = Date()
my_date.to_int(d)
my_date.valid(d)

Date.to_int(d)
Date.valid(d)



