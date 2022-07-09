''' Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.'''


class Car:
    speed = 0
    color = "color"
    name = "name"
    is_police = False

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        print('Машина повернула')

    def show_speed(self):
        print(f"Текущая скорость автомобиля {speed} кмч")


class Towncar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Вы превышаете скорость 60 кмч на городском автомобиле")
        else:
            print(f"Текущая скорость автомобиля {speed} кмч")


class Sportcar(Car):
    speed = 100


class Workcar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Вы превышаете скорость 40 кмч на рабочем автомобиле")
        else:
            print(f"Текущая скорость автомобиля {speed} кмч")


class Policecar(Car):
    is_police = True


workcar_1 = Workcar()
workcar_1.speed = 80
print(f"Police car = {workcar_1.is_police}")
workcar_1.show_speed()

towncar_1 = Towncar()
towncar_1.speed = 80
print(f"Police car = {towncar_1.is_police}")
towncar_1.show_speed()

police_1 = Policecar()
print(f"Police car = {police_1.is_police}")
