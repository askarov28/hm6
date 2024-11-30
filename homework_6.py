import sqlite3 
 
me = sqlite3.connect('geks.db') 
cursor = me.cursor() 
 
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS users( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        full_name VARCHAR (30) NOT NULL, 
        number INT DEFAULT NUUL     
      ) 
""") 

def register():
    full_name = input("Введите ФИО: ") 
    number= int(input("Введите свой номер телефона :"))

me.commit()    
register()

def delete_geek_by_id(geek_id):
    """Функция для удаления записи по id"""
    cursor.execute('''
    DELETE FROM geeks WHERE id = ?
    ''', (geek_id,))
    me.commit()
    print(f"Запись с id {geek_id} успешно удалена!")