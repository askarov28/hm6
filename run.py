from main import User, UserService

user = UserService()

# user_service=User(name='Uluk', email='uluk228666@gmail.com', age= 18)
# user.add_user(user_service)

find= user.find_user_by_email('uluk228666@gmail.com')
if find:
    print (f"Ползователь найден : {find.name},{find.email},{find.age}")