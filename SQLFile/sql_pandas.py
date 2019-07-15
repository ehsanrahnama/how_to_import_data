import sqlite3
import os
import pandas as pd 


ROOT_DIR = os.getcwd()
database_path = os.path.join(ROOT_DIR, 'SQLFile', 'importing_sqlite.db')

stack_connection = sqlite3.connect(database_path)
posts_df = pd.read_sql('select * from posts;',con=stack_connection)


print(type(posts_df)) # Type = DataFrame 

print(posts_df.columns)
print(posts_df.head())
