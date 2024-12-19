import sqlite3

class Movies:
    def __init__(self, db_name='cinema.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS films(
            id INTEGER PRIMARY KEY,
            title TEXT UNIQUE NOT NULL,
            release_year INT NOT NULL,
            genre TEXT,
            rating REAL
        )
        """)
        self.connection.commit()


class Users:
    def __init__(self, cursor):
        self.cursor = cursor
        self.create_table_users()

    def create_table_users(self):
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            user_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            registration_date DATE
        )
        """)
        self.connection.commit()


class Reviews:
    def __init__(self, cursor):
        self.cursor = cursor
        self.create_table_reviews()

    def create_table_reviews(self):
        self.cursor.execute('''   
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            movie_id INTEGER NOT NULL,
            review_text TEXT,
            rating REAL NOT NULL,
            review_date DATE DEFAULT CURRENT_DATE,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (movie_id) REFERENCES films(id)
        )        
        ''')
        self.connection.commit()


class Methods(Movies, Users, Reviews):
    def __init__(self, db_name='cinema.db'):
        Movies.__init__(self, db_name)
        Users.__init__(self, self.cursor)
        Reviews.__init__(self, self.cursor)

    
    def get_year(self):
        self.cursor.execute('''SELECT * FROM films WHERE release_year IN (2011, 2010, 2012)''')
        return self.cursor.fetchall() 
   
    def get_rating(self):
        self.cursor.execute('''SELECT * FROM reviews WHERE rating = 5''')
        return self.cursor.fetchall()

    def get_name(self):
        self.cursor.execute('''SELECT * FROM users WHERE user_name = ?''', ('John',)) 
        return self.cursor.fetchone()

    def get_genre(self):
        self.cursor.execute('''SELECT genre FROM films WHERE rating = ?''', (7,))        
        return self.cursor.fetchone()
   
    def get_id(self):
        self.cursor.execute(('''SELECT movie_id FROM films WHERE id = ?''', (5,)))
        return self.cursor.fetchone()
    

movie = Methods()
print(movie.get_name())  
print(movie.get_year())  
print(movie.get_rating())  
print(movie.get_genre()) 
print(movie.get_id())
