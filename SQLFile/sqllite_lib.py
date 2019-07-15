import sqlite3
import os 


ROOT_DIR = os.getcwd()
database_path = os.path.join(ROOT_DIR, 'SQLFile', 'importing_sqlite.db')

stack_connection = sqlite3.connect(database_path)
print(type(stack_connection))

stack_cursor = stack_connection.cursor()

stack_cursor.execute("select name from sqlite_master where type = 'table';")
print(stack_cursor.fetchone())
print(stack_cursor.fetchall())

row = stack_cursor.execute("select * from posts;").fetchall()
print(type(row)) # list of tuple
print(row[0]) 
print(type(row[0]))

row_1 = stack_cursor.execute("select * from posts limit 1 ;").fetchall()
row_2 = stack_cursor.execute("select Id, Score, Tags from posts limit 3 ;").fetchall()

print(row_1)
print(row_2)
