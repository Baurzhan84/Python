# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# # (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# import time
#
# class TrafficLight:
#
#     def running(self):
#         self.__color = 'red'
#         print('red')
#         time.sleep(7)
#         self.__color = 'yellow'
#         print('yellow')
#         time.sleep(2)
#         self.__color = 'green'
#         print('green')
#
#
# a = TrafficLight()
# a.running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
#
# class Road:
#
#     def __init__(self, length, width, weight):
#         self.length = length
#         self.width = width
#         self.weight = weight
#
#
#     def multiple(self):
#         return self.length*self.width*self.weight
#
#
#
# r = Road(20,5000,25)
# print(r.multiple())

#
# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии ().
# Проверить работу примера
# на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
#
# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
# #
# class Position(Worker):
#     def get_full_name(self):
#          print(f'{self.name} {self.surname} {self.position}')
#
#     def get_total_income(self):
#         print(f'Доход: {self._income["wage"] + self._income["bonus"]}')
#
# p = Position('b', 'b', 'man', 120, 20)
# p.get_total_income()
# p.get_full_name()

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self,speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('Машина тронулась')
    def stop(self):
        print('Машина остановилась')
    def turn(self):
        print('Машина поворачивает')
    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена')
        else:
            print('Скорость нормальная')




class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена')
        else:
            print('Скорость нормальная')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышена')
        else:
            print('Скорость нормальная')


tc = TownCar(60, 'black', 'BMW')
tc.go()
tc.show_speed()
tc.turn()

wc = WorkCar(30, 'black', 'bmw')
wc.show_speed()