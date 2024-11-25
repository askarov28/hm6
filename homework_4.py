# Базовый класс Vehicle:
# Метод calculate_travel_time() возвращает 0 по умолчанию.
# Метод display_info() выводит информацию о транспортном средстве (тип и характеристики).
# Конструктор принимает параметры: название транспорта и максимальная скорость.
# Классы-наследники:
# Класс Car:
# Метод calculate_travel_time() рассчитывает время поездки как расстояние, деленное на максимальную скорость.
# Класс Bicycle:
# Метод calculate_travel_time() увеличивает расчетное время поездки на 20% (учитывая остановки).
# Класс Plane:
# Метод calculate_travel_time() добавляет фиксированное время на взлет и посадку (например, 1 час) к расчету времени.
# Функция calculate_and_display_travel(vehicle, distance):
# Принимает объект класса Vehicle и расстояние.
# Вызывает методы display_info() и calculate_travel_time() для расчетов.
# Корректно работает для всех классов-наследников.
# Пример использования:
# Создать объекты для автомобиля, велосипеда и самолета с заданными характеристиками.
# Рассчитать и вывести время на преодоление расстояния 500 км для каждого транспорта.

class Vehicle:
    def calculate_travel_time(self,type,xar,max,amout):
        self.type=type
        self.xar=xar
        self.max=max
    def  display_info(self):
        return f'Тип кузова -{self.type} Характеристика авто -{self.xar}'  
    

class Car:
    def calculate_travel_time(self, type, xar, amout, max):
        self.max=max
        return f'Тип кузова -{type} Характеристика авто -{xar} Махсимальная скорость -{max}км Время поездки{amout//max }'  
    

class Bicycle:
    def calculate_travel_time(self, type, xar, amout,max):
        return f'Тип кузова -{type} Характеристика велосипеда -{xar} Махсимальная скорость -{max}км  Время поездки{amout//max *20}'
    

class Planet:
    def calculate_travel_time(self, type, xar, amout,max):
        return f'Тип кузова -{type} Характеристика самалёта -{xar} Время взлёта -{max}км  Время полёта{amout//max}'
    

car=Car("Седан","Турбина",500,180)   
bicycle=Bicycle("steels","Горный",500,90)
planet=Planet('Boing','Грузавой',500,2600)

for calculate_and_display in (car,bicycle,planet):
    print(calculate_and_display.calculate_travel_time())


        