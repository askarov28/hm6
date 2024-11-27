class Vehicle:
    def __init__(self, name, max_speed, distance):
        self.name = name
        self.max_speed = max_speed
        self.distance = distance

    def display_info(self):
        print(f'Тип транспорта - {self.name}. Макс скорость - {self.max_speed} км/час. Расстояние - {self.distance}') 

    def calculate_travel_time(self):
        return 0
    
class Car(Vehicle):
    def __init__(self, name, max_speed, distance):
        super().__init__(name, max_speed, distance)
        
    def calculate_travel_time(self):
        return f'Название транспорта - {self.name}  Время поездки - {self.distance / self.max_speed} часа'
    
class Bicycle(Vehicle):
    def __init__(self, name, max_speed, distance):
        super().__init__(name, max_speed, distance)

    def calculate_travel_time(self):
        return f'Название транспорта - {self.name}  Время поездки - {(self.distance / self.max_speed) * 1.2} часов'
    
class Plane(Vehicle):
    def __init__(self, name, max_speed, distance):
        super().__init__(name, max_speed, distance)

    def calculate_travel_time(self):
        return f'Название транспорта - {self.name}  Время поездки - {self.distance / self.max_speed + 1} часа'
    
def calculate_and_display_travel(vehicle):
    vehicle.display_info()
    time = vehicle.calculate_travel_time()
    print(f'Время: {time}')


Vehicle_1 = Car('Mersedes Benz Gt63AMG', 360, 500)
Vehicle_2 = Bicycle("Steels", 50, 500)
Vehicle_3 = Plane("BOING", 350, 500)
        
calculate_and_display_travel(Vehicle_1)
calculate_and_display_travel(Vehicle_2)
calculate_and_display_travel(Vehicle_3)