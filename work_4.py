"""ООП-обектное орентирование программирование """
"""ПОЛИМОРФИЗ"""

# str+str-конкaнтeнация ctrok


# class Cat:
#     def __init__(self,name,preferens):
#         self.name=name
#         self.preferens=preferens        

#     def info(self):
#         print(f"я кот. Меня зовут {self.name}. Мне {self.preferens} года")

#     def make_sound(self):
#         print("Мяу!")    

# class Dog:
#     def __init__(self,name,preferens):
#         self.name=name
#         self.preferens=preferens        

#     def info(self):
#         print(f"я собака. Меня зовут {self.name}. Мне {self.preferens} года")

#     def make_sound(self):
#         print("Гаф!")    


# cat=Cat("васька",2)
# dog=Dog("Мухтар",3)

# for animal in (cat,dog):
#     animal.info()
#     animal.make_sound()



# class PaymentMethod:
#     def pey(self, amount):
#         pass

# class CreditCard(PaymentMethod):
#     def pey(self, amount):
#         return f"Cумма {amount}, оплачивается по кредитной карте"
    
# class PayPal(PaymentMethod):
#     def pey(self, amount):
#         return f"Cумма {amount}, оплачивается по PayPal"   
    
# class BankTransfer(PaymentMethod):
#     def pey(self, amount):
#         return f"Cумма {amount}, оплачивается по банковскому переводу "    
    

# payments=[CreditCard(),PayPal(),BankTransfer()]

# for payment in payments:
#     print(payment.pey(100))


class Employee:
    def colculate_salary(self,name,furstname,yaer,amout):
        self.name=name
        self.furstname=furstname
        self.year=yaer
    def display_info(self):
        return f" Имя-{self.name}\n Фамилия-{self.furstname} \n Год рождения-{self.yaer}"
    
class  FullTimeEmployee(Employee):
    def colculate_salary(self, name, furstname, yaer, amout):
        return  f" Имя-{name} \n Фамилия-{furstname} \n Год рождения-{yaer} \n Бозовая зарплата {amout*1.2}"
    
class  PartTimeEmployee(Employee):
    def colculate_salary(self, name, furstname, yaer, amout):
        time=0.5
        self.time=time
        num = amout *1.2*0.5 
        return  f" Имя-{name} \n Фамилия-{furstname} \n Год рождения-{yaer} \n зарплата {num}"
    
name=[FullTimeEmployee(),PartTimeEmployee()] 

for namer in name:
    print(namer.colculate_salary("Ulugbek","Askarov",2006,20000))
    
