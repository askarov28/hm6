# """ООП-обектное орентирование программирование """

# hello_geeks ="Geeks"# Змеиный регистр

# HelloGeeks= "Geeks"# Вепблюжий регистр

# class Car:# Шаблон или чертеж
#     def __init__(self,motor,wheel,body):#__init__- Это конструктор 
#         self.motor = motor# self-Ссылка на текущий обьект
#         self.wheel = wheel# атрибут класса
#         self.body = body

#         self.bak= 20
#         self.is_start = False #Флажок

#     def info(self):# Фуекция внутри класса превращается в метод
#         print(f"мотор-{self.motor} колесо-{self.wheel} кузов-{self.body}")

#     def start(self):
#         if self.bak>0:
#             self.is_start=True
#             print(" машина заведена ")
#         else:
#             print("У машины нет топлива ")
#     def stop(self):
#         self.is_start= False
#         print("Машина заглушина")

#     def drive(self,city):
#         if self.is_start== True:
#             print(f"Машина едет b {city}")
#         else:
#             print(" машина заведена ")

            

# car= Car('v6','R20','M')# Экземпляр класса 
# car.info()
# car.start()
# car.drive("АОЭ")

# name=("Asko","isko","Sema")
# name_1=list(name)
# name_1.append("Aslan")
# name_3=tuple(name_1)
# print(name_3)

# class Book:
#     def __init__(self, avtor,book_name,year):
#         self.avtor= avtor
#         self.book_name= book_name
#         self.year= year

#     def info(self):
#         print(f"Автор кники-{self.avtor}  Название книги-{self.book_name}  Сколько ему годов-{self.year}")    

# book=Book("Пушкин","Сказка о рыбаке и рыбки","10")   
# book.info()
    