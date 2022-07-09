'''3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.'''


class Worker:
    income_d = {"wage": 10000, "bonus": 0.25}
    name = 'Имя'
    surname = 'Фамилия'
    position = 'Должность'
    _income = income_d


class Position(Worker):
    def get_full_name(self):
        self.name = input('Введите имя сотрудника >> ')
        self.surname = input('Введите фамилию сотрудника >> ')

    def get_total_income(self):
        self._income = self.income_d.get("wage") + self.income_d.get("wage") * self.income_d.get("bonus")
        print(f"Общий доход сотрудника {self.name} {self.surname} составляет {self._income} р.")


worker_1 = Position()
worker_1.get_full_name()
worker_1.get_total_income()
print(worker_1.name)
print(worker_1.surname)
