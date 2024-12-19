import sqlite3

class Datebase:
    def __init__(self,db_name="users.db"):
        self.connection=sqlite3.connect(db_name)
        self.cursor= self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (40) NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER 
            )
        """)

        self.connection.commit()

    def add_user(self, user):
        self.cursor.execute(" INSERT INTO users (name, email, age) VALUES (?,?,?)",(user.name, user.email, user.age))
        
        self.connection.commit()

    def get_user(self, email):
        self.cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        return self.cursor.fetchone()
    
    def delet_user_by_email(self, email):
        self.cursor.execute("DELETE FROM users WHERE email = ?", (email,))
        self.connection.commit()
        print(f"пользователь с email {email} был удалён")

    def close(self):
        self.connection.close() 
