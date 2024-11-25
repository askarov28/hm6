# """ООП-обектное орентирование программирование """
# "Наследование"

# class Game:#Родительский класс
#     def __init__(self,game_name,game_year,company,grapics):
#         self.game_name=game_name
#         self.game_yaer=game_year
#         self.company=company
#         self.grapics=grapics
    
#     def info(self):
#         print(f"Game-{self.game_name}-{self.game_yaer}-{self.company}-{self.grapics}-{self.myltiplayer}")

# # game=Game("Csgo2","2009","Walf","4k") 
# # game.info()    

# class Roblox(Game):
#     def __init__(self, game_name, game_year, company,grapics,myltiplayer):
#         #super().__init__(game_name, game_year, company, grapics)
#         Game.__init__(self, game_name, game_year, company,grapics)
#         self.myltiplayer=myltiplayer
#         self.name="player"
#         self.gender="None"
#         self.skin="None"
#         self.hp="100"
    
#     def info(self):
#         return super().info()
    
#     def info_plyaer(self):
#         print(f"Игрок- {self.name}-{self.gender}- {self.skin}- {self.hp}XP")
    
#     def edit_player(self):
#         name=input("Введите имя игрока: ")
#         gender=input("Введите пол игрока: ")
#         skin=input("Введите облик для игрока: ")
#         self.name=name
#         self.gender=gender
#         self.skin=skin
        

# roblox=Roblox('Roblox',2006,"Roblox Corp.",'ultra',"yes")        
# roblox.info()
# roblox.edit_player()
# roblox.info_plyaer()


# class Strike(Roblox):
#     def __init__(self, game_name, game_year, company, grapics, myltiplayer):
#         super().__init__(game_name, game_year, company, grapics, myltiplayer)


class Animals:
    def __init__(self,name,):
        self.name=name

    def eat(self):
        print(f"{self.name}-едят")    
  


class Walker:
    def __init__(self,name):
        self.name=name

    def walk(self):
        print(f"{self.name}-ходит")    


class Swimmer:
    def __init__(self,name):
      self.name=name 
     
     
    def swim(self):
        print(f"{self.name}-плавает")   
    

class Flyer:
    def __init__(self,name):
      self.name=name  
     
    def fly(self):
        print(f"{self.name}-летает")   


class Penguin(Animals,Walker,Swimmer,Flyer):
    def __init__(self, name):
        super().__init__(name)
    def ship(self):
        print(f"{self.name}-может ходить и плавать ")

penguin=Penguin("Пингвин")
penguin.ship()

class Duck(Animals,Walker,Swimmer,Flyer):
    def __init__(self, name):
        super().__init__(name)
    def discribe(self):
        print(f"{self.name}-может ходить,плавать и летать")

duck=Duck("Утка")        
duck.discribe()

class Bat(Animals,Flyer):
    def __init__(self, name):
        super().__init__(name)
    def discribe(self):
        print(f"{self.name}-может летать")

bat=Bat("Летучая мышь")        
bat.discribe()       
   
class Zoo(Animals,Walker,Swimmer,Flyer):
    def __init__(self, name):
        super().__init__(name)

animals=Animals("Все животные")
animals.eat()
walker=Walker("Медведь")   
walker.walk()
swimmer=Swimmer("Утка") 
swimmer.swim
flyer=Flyer("Калибрий")
flyer.fly()

        

        