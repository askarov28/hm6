#1 Задание
grades=[1,2,3,4,5,6,7,8,9,10]
class Students:
    def __init__(self,name,age,grades):
        self.name= name
        self.age=age
        self.grades=grades
    def avereg_grades(self):
       self.gra= sum(grades)/len(grades)
       print(f"Ф.И.О-{self.name} Возраст-{self.age} Балл-{self.gra}")
students=Students("Аскаров Улугбек","19",grades)      
students.avereg_grades()

#2 Задание
class Movie:
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.name=duration

    
    def duration_category(self):
        name=int(input("Введите длительность в минутах: "))
        self.name=name
        if name<=60:
            print("короткий")
            self.is_duration=True
        elif name<=120:
            print("средний") 
            self.is_duration=True

        elif name> 120:
            print("длинный") 
            self.is_duration=True

        else:
            print("Введите повторно")   

    def info(self):
        print(f"Название-{self.title} Режиссёр-{self.director} Длительность в минутах-{self.name}")        

    
movie=Movie("rrr","rrrr","name")
movie.duration_category()
movie.info()


    
