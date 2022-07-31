'''4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные
типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

5.Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
оргтехники на склад и передачу в определённое подразделение компании. Для хранения данных
о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
любую подходящую структуру (например, словарь).

6.Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на склад,
нельзя использовать строковый тип данных. Подсказка: постарайтесь реализовать в проекте
«Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.'''


class only_int(Exception):
    def __init__(self, txt):
        self.txt = txt

class Warehouse:
    in_stock = []
    count_equip = 0
    count_printer = 0
    count_scaner = 0
    count_xerox = 0

    def equip_in_stock(self):
        print("Техника в наличии")
        for el in Warehouse.in_stock:
            print(f'Название: {el[0]}, Объем упаковки, м3: {el[1]}, Вес, кг: {el[2]}, '
                  f'Всего шт: {el[4]},в подразделении, шт: {el[5]}')

    def counts(self):
        Warehouse.count_printer = Office_equip.printers[0][4]
        Warehouse.count_scaner = Office_equip.scaners[0][4]
        Warehouse.count_xerox = Office_equip.xeroxs[0][4]
        Warehouse.count_equip = Warehouse.count_printer + Warehouse.count_scaner + Warehouse.count_xerox
        print(f'Всего {Warehouse.count_printer} принтер(ов), в подразделении {Warehouse.in_stock[0][5]} \n'
              f'Всего {Warehouse.count_scaner} сканер(ов), в подразделении {Warehouse.in_stock[1][5]} \n'
              f'Всего {Warehouse.count_printer} копир(ов), в подразделении {Warehouse.in_stock[2][5]} \n')

    def trans_to_dep(self):
        while True:
            a = input('Что хотите передать в подразделение? 1 - Принтер, 2 - Сканер, 3 - Копир, q - Выход ')
            if a != 'q':
                b = input('Сколько единиц? ')
                try:
                    if (not b.isdigit()):
                        raise only_int('Вводите только числа!')
                except only_int as m:
                    print(m)
                else:
                    b = int(b)

                if a == '1':
                    if b > Warehouse.count_printer:
                        print('На складе нет столько принтреров!')
                    else:
                        Warehouse.in_stock[0].pop(5)
                        Warehouse.in_stock[0].insert(5, b)
                        break
                elif a == '2':
                    if b > Warehouse.count_scaner:
                        print('На складе нет столько сканеров!')
                    else:
                        Warehouse.in_stock[1].pop(5)
                        Warehouse.in_stock[1].insert(5, b)
                        break
                elif a == '3':
                    if b > Warehouse.count_xerox:
                        print('На складе нет столько копиров!')
                    else:
                        Warehouse.in_stock[0].pop(5)
                        Warehouse.in_stock[2].insert(5, b)
                        break
                else:
                    print('Введите корректный номер')
            elif a == 'q':
                break


class Office_equip(Warehouse):
    printers = []
    scaners = []
    xeroxs = []
    def __init__(self, name, pack_vol, weight):
        self.pack_vol = pack_vol  # объем упаковки
        self.weight = weight  # масса
        self.name = name

    def add_to_stock(self):
        for el in Office_equip.printers:
            Office_equip.printers[0].append(0)
            Warehouse.in_stock.extend(Office_equip.printers)
        for el in Office_equip.scaners:
            Office_equip.scaners[0].append(0)
            Warehouse.in_stock.extend(Office_equip.scaners)
        for el in Office_equip.xeroxs:
            Office_equip.xeroxs[0].append(0)
            Warehouse.in_stock.extend(Office_equip.xeroxs)


class Printer(Office_equip):
    def __init__(self, name, pack_vol, weight, print_res, pcs):
        super().__init__(name, pack_vol, weight)
        self.print_res = print_res
        self.pcs = pcs

    def add_printer(self):
        new_print = [self.name, self.pack_vol, self.weight, self.print_res, self.pcs]
        Office_equip.printers.append(new_print)


class Scaner(Office_equip):
    def __init__(self, name, pack_vol, weight, scan_res, pcs):
        super().__init__(name, pack_vol, weight)
        self.scan_res = scan_res
        self.pcs = pcs

    def add_scaner(self):
        new_scaner = [self.name, self.pack_vol, self.weight, self.scan_res, self.pcs]
        Office_equip.scaners.append(new_scaner)


class Xerox(Office_equip):
    def __init__(self, name, pack_vol, weight, copy_res, pcs):
        super().__init__(name, pack_vol, weight)
        self.copy_res = copy_res
        self.pcs = pcs

    def add_xerox(self):
        new_xerox = [self.name, self.pack_vol, self.weight, self.copy_res, self.pcs]
        Office_equip.xeroxs.append(new_xerox)

my_warehouse = Warehouse()
scaner1 = Scaner("Сканер1", 1, 20, 300, 10)
printer1 = Printer("Принтер1", 1, 20, 300, 10)
xerox1 = Xerox("Ксерокс1", 1, 20, 300, 10)

scaner1.add_scaner()
printer1.add_printer()
xerox1.add_xerox()

Office_equip.add_to_stock(my_warehouse)
my_warehouse.equip_in_stock()
my_warehouse.counts()
my_warehouse.trans_to_dep()
my_warehouse.counts()
