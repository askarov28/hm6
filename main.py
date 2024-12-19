from work_7 import Datebase

class User:
    def __init__(self,name, email, age):
        self.name=name
        self.email=email
        self.age=age

class UserService:
    def __init__(self, db_name='users.db'):
        self.db=Datebase()

    def add_user(self, user):
        if self.find_user_by_email(user.email):
            print("пользователь с таким  email уже существует ")   
            return
        self.db.add_user(user)
        print("Ползователь добавлен ")     

    def find_user_by_email(self, email):
        user_data= self.db.get_user(email)
        if user_data:
            return User(name=user_data[1], email=user_data[2], age=user_data[3])
        else:
            print("Ползователь не найден ") 

    def delet_user_by_email(self, email):
        delete_user=self.find_user_by_email(email)
        if delete_user:
            self.db.delet_user_by_email(email)
        else:
            None

    def close(self):
        self.db.close()           
