"""ООП-обектное орентирование программирование """
"""ИНКАПСУЛЯЦИЯ  """

class PublicExample:# Публичный класс
    def __init__(self,value): 
        self.value=value # Публичный атребут 

    def info(self):
        return self.value # Публичный метод

public=PublicExample(23)
print(public.info())  # Вызов публичного метода 
print(public.value) # Доступ к публичному атрибуду


class ProtectedExample: #  Защищеный класс
    def __init__(self, value): 
       self._value= value#  Защищеный атрибут
    def info(self):
        return self._value #Защищеный метод

protected= ProtectedExample(43)
print(protected.info()) # Это работает но противоречит принципам инкапсуляции
print(protected._value) # Можно получить значеник напрямую, но это не рекомендуется


class PrivateExample:
     def __init__(self, value): 
        self.__value= value # Приватный атребут

     def __info(self): # Приватный метод
         return self.__value
     
     def acces_private(self):
         return self.__info()
     
private=PrivateExample(12)

# print(private.__info()) 

# print(private.__value)

# print(private.acces_private())

print(private._PrivateExample__info())

import datetime

class Car:
    def __init__(self,marka,model,year,mileage):
        self.marka=marka
        self.model=model
        self.year=year
        self.mileage=mileage
    
    
    def info(self):
       return f'Марка - {self.marka}\nМодель - {self.model}'


    def _calculete_age(self):
        current=datetime.datetime.now().year
        return f'Возраст машины - {current - self._year}'

    def __update_mileage(self,mileage_update= 1000):
        self.__mileage = mileage_update
        return self.__mileage

    def set_mileag(self):
        return self.__update_mileage
    
car=Car("Mazda","Demio",2008,140000)

print(car.info())
print(car._calculete_age())
print
