"""1. Создание класса для работы с базой данных
Напишите класс DatabaseManager, который будет использовать SQLite3 для подключения к базе данных. Реализуйте методы для открытия и закрытия соединения.
2. Класс для управления таблицей
Создайте класс User, который будет управлять таблицей users в SQLite3. Реализуйте методы для добавления нового пользователя, получения пользователя по ID и удаления пользователя.
3. Наследование и работа с несколькими таблицами
Реализуйте классы Admin и Customer, которые будут наследовать от класса User. Добавьте дополнительные поля для каждой роли и методы для работы с соответствующими таблицами admins и customers.
4. Поиск данных в базе
Напишите метод в классе DatabaseManager, который будет принимать имя пользователя и возвращать его данные из таблицы users. Используйте SQL-запросы для поиска данных.
5. Работа с транзакциями
Добавьте в класс DatabaseManager метод, который будет выполнять несколько операций с базой данных в одной транзакции. Реализуйте простую логику для добавления нескольких записей в таблицу и откат транзакции в случае ошибки.
"""

import sqlite3

class DatabaseManager:
    def __init__(self, db_name='user.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def get_users(self):
         self.cursor.execute(""" SELECT * FROM users WHERE User IN (1)""")   
     

    def close(self):
        self.db.close()      

    
class User:
    def __init__(self,cursor,user_name,email):
        
        self.users = user_name
        self.email=email
        self.cursor=cursor     
        self.create_table()

    def create_table(self,cursor,connection):
        
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            user_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
        """)
    def user(self,cursor):
        user_name = input('Введите ФИО:') 
        email =  input('Введите электроную почту:')
        cursor.execute("""
        INSERT INTO users (user_name, email)
        VALUES (?, ?)
    """, (user_name,email))
        self.connection.commit()
    
    def add_user(self,user_name, email,cursor):
         cursor.execute("INSERT INTO books (user_name, email) VALUES (?, ?, ?)", (user_name,email))


class Admin(User):
    def __init__(self, cursor, user_name, email):
        super().__init__(cursor, user_name, email)
        


    def de(self):
         id_delete= int(input(":"))
         self.cursor.execute("DELETE * FROM users WHERE id = ?",(id_delete,)) 
         
         self.connection.commit()
          


class Customer(User):
     def __init__(self, cursor, user_name, email):
          super().__init__(cursor, user_name, email)
     def get(self):
          id_get=int(input(":"))
          self.cursor.execute("SELECT * FROM users WHERE id = ?",(id_get,))
          print(self.cursor.execute.fetchone())          

admin = Admin('cursor','maxim','dssda')
admin.de()

costumer=Customer()
costumer.get()
             
user = User('fwdfwds','sfdsfdsf','sdfdsf')
user.add_user()          

                  
