import sqlite3

con = sqlite3.connect("db.db") # приєднання до файла (бд) database.db якщо такого файлу нема воно його створить
cur = con.cursor() # створення об'єкта курсора