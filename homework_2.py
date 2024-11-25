# Задание
class Animals:
    def __init__(self,name,):
        self.name=name

    def eat(self):
        print(f"{self.name}-едят")    
  

class Walker:
    def __init__(self,name):
        self.name=name

    def walk(self):
        print(f"{self.name}-ходит")    


class Swimmer:
    def __init__(self,name):
      self.name=name 
     
     
    def swim(self):
        print(f"{self.name}-плавает")   
    

class Flyer:
    def __init__(self,name):
      self.name=name  
     
    def fly(self):
        print(f"{self.name}-летает")   


class Penguin(Animals,Walker,Swimmer,Flyer):
    def __init__(self, name):
        super().__init__(name)
    def ship(self):
        print(f"{self.name}-может ходить и плавать ")

penguin=Penguin("Пингвин")
penguin.ship()


class Duck(Animals,Walker,Swimmer,Flyer):
    def __init__(self, name):
        super().__init__(name)
    def discribe(self):
        print(f"{self.name}-может ходить,плавать и летать")

duck=Duck("Утка")        
duck.discribe()


class Bat(Animals,Flyer):
    def __init__(self, name):
        super().__init__(name)
    def discribe(self):
        print(f"{self.name}-может летать")

bat=Bat("Летучая мышь")        
bat.discribe()       
   

class Zoo(Animals,Walker,Swimmer,Flyer):
    def __init__(self, name):
        super().__init__(name)

animals=Animals("Все животные")
animals.eat()
walker=Walker("Медведь")   
walker.walk()
swimmer=Swimmer("Утка") 
swimmer.swim
flyer=Flyer("Калибрий")
flyer.fly()

# 1 Задание:
"""Классы Транспортных Средств
Создайте базовый класс Vehicle (Транспортное средство):
Свойство name (название) — строка, задается при создании объекта.
Свойство max_speed (максимальная скорость) — целое число, также задается при создании объекта.
Метод display_info, который выводит информацию о транспортном средстве в формате:
 [name] имеет максимальную скорость [max_speed] км/ч"
 """

class Vehicle:
    def __init__(self,name,max_speed):
        self.name=name
        self.speed=max_speed

    def display_info(self):
        print(f"{self.name} - Эта машина  имеет максимальную скорость {self.speed} км/ч")    

car=Vehicle("АВАНТЕ",240)
car.display_info()


#2 Задание:
"""Создайте два класса-наследника:
Класс Car (Автомобиль):
Переопределите метод display_info, чтобы он выводил информацию в формате:
 
Автомобиль [name] может ехать с максимальной скоростью [max_speed] км/ч
 
Класс Bicycle (Велосипед):
Переопределите метод display_info, чтобы он выводил информацию в формате:
 
Велосипед [name] может ехать с максимальной скоростью [max_speed] км/ч"""

class Car:
    def __init__(self,name,max_speed):
        self.name=name
        self.speed=max_speed

    def display_info(self):
        print(f"Автомобиль {self.name} может ехать с максимальной скоростью {self.speed} км/ч")    

car=Car("АВАНТЕ",240)
car.display_info()


class Bicycle:
    def __init__(self,name,max_speed):
        self.name=name
        self.speed=max_speed

    def display_info(self):
        print(f"Велосипед {self.name} может ехать с максимальной скоростью {self.speed} км/ч")    

car=Bicycle("Stels",90)
car.display_info()


class Mot(Car,Bicycle):
    def __init__(self, name, max_speed):
        super().__init__(name, max_speed)

    def display_info(self):
        print(f"Автомобиль {self.name} может ехать с максимальной скоростью {self.speed} км/ч")  
        print(f"Велосипед {self.name} может ехать с максимальной скоростью {self.speed} км/ч")    


moto=Mot(10,90)
moto.display_info()