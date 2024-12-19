import sqlite3

connect = sqlite3.connect('library.db')
cursor = connect.cursor()

cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT UNIQUE NOT NULL,
        author TEXT NOT NULL,
        year INTEGER
    )
""")

def book():
    title = input("Название книги: ")
    author = input("Автор книги: ")
    year = int(input("Год издания: "))
    cursor.execute("""
        INSERT INTO books (title, author, year)
        VALUES (?, ?, ?)
    """, (title, author, year))
    connect.commit()

def add_book(title, author, year):
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    connect.commit()

def find_book_by_title(title):
    cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
    return cursor.fetchone()

def update_book_year(title, new_year):
    cursor.execute("UPDATE books SET year = ? WHERE title = ?", (new_year, title))
    connect.commit()
    print(f'Год издания книги "{title}" был обновлен на {new_year}')

def delete_book_by_title(title):
    cursor.execute("DELETE FROM books WHERE title = ?", (title,))
    connect.commit()
    print(f'Книга с названием "{title}" была удалена')


book()  
add_book("Биринчи мугалим", "Ч.Айтматов", 1962) 
