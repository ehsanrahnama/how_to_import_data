from sqlalchemy import create_engine
import pandas as pd 

engine = create_engine('mysql+mysqlconnector://ehsan:12345@localhost:3306/importing_mysql')

print(engine.table_names())
print(engine.dialect)
print(engine.driver)


# Load as Data Frame
posts_df = pd.read_sql_table('posts', con=engine, index_col='Id')
print(posts_df)
print(posts_df.columns)
print(posts_df.head())

posts = pd.read_sql_table('posts', engine, columns=['Id', 'CreationDate', 'Tags'])
print(posts.head())
print(20*'------')
print(posts.iloc[1][1])
print(type(posts.iloc[1][1]))

posts = pd.read_sql_table('posts', engine, columns=['Id', 'CreationDate', 'Tags'], 
                        parse_dates={'CreationDate':{'format': '%Y-%m-%dT%H:%M:%S.%f'}}) # or parse_dates=['CreationDate']
print(type(posts.iloc[1][1]))
print(posts.iloc[1][1])
