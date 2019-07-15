import psycopg2
import pandas as pd
from sqlalchemy import create_engine

conn = psycopg2.connect("dbname='importing_postgres' user='postgres' host='localhost' password='mypass'")
#  password='mypass'
cursor = conn.cursor()

cursor.execute("SELECT * FROM posts;")

print(cursor.fetchone())

# using pandas
posts = pd.read_sql("SELECT * FROM posts limit 5", con=conn)
print(posts)

# Close and Commit connection
conn.commit()
conn.close()

print(40*"---")
# Using SQLAlchemy

engine = create_engine('postgres://postgres:mypass@localhost/importing_postgres')
print(engine.table_names())
print(engine.driver)

posts_df = pd.read_sql_table('posts', con=engine, index_col='Id')

print(posts_df.head())
