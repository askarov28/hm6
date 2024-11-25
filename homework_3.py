#1 Задание
"""Создайте класс BankAccount, который будет моделировать банковский счет. Используйте инкапсуляцию, чтобы защитить данные счета.
Требования:
Создайте приватный атрибут _balance, который будет хранить баланс счета.
Реализуйте методы:
deposit(amount) для пополнения счета (добавляет сумму к балансу). Если сумма отрицательная, выведите сообщение об ошибке.
withdraw(amount) для снятия денег. Если сумма превышает баланс, выведите сообщение о недостатке средств.
get_balance() для получения текущего баланса.
Добавьте валидацию, чтобы пользователь не мог напрямую изменить баланс счета."""

class BankAccount:
    def __init__(self,money):
        self.money=money

    def _balance(self):
        print(f"Ваш баланс состовляет {self.money}сом")  

    def deposit(self):
        name=float(input("Пополнить счёт: "))  
        self.name=name
        print(f"Ваш баланс состовляет {self.money+self.name}coм")    
        if  self.name<0:
            print("Ошибка")

    def withdraw(self):
        name=float(input("Введите сумму для вывода: ")) 
        self.name=name
        print(f"Возмите деньги пожалуйста")
        if self.name<self.money:
            print("У вас не дастаточно средств ")

    def get_balance(self):
        print(f"Ваш баланс состовляет {self.money}сом")    

money=BankAccount(0)
money._balance()  
money.deposit()   
money.withdraw()    
money.get_balance()  