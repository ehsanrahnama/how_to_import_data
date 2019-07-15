import os 
from sqlalchemy import create_engine

ROOT_DIR = os.getcwd()
database_path = os.path.join(ROOT_DIR, 'SQLFile', 'importing_sqlite.db')

engine = create_engine(f'sqlite:///{database_path}')

print(type(engine))
print(20*'-----')
print(engine.table_names())
print(engine.url)
print(engine.driver)

