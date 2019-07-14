# stata file representing STATistics + DatA ==> dta 
import pandas as pd 
import os 

ROOT_DIR = os.getcwd()
stata_path = os.path.join(ROOT_DIR, 'BinaryFile', 'data', 'posts-100.dta')


posts_stata = pd.read_stata(stata_path)

# Read like data frame pandas 
print(type(posts_stata))

print(dir(posts_stata))
print(posts_stata)
print(posts_stata.head())
print(posts_stata.columns)
print(posts_stata.iloc[1])
print('\n')
print(posts_stata['Id'])
print('\n')

posts_stata_reader = pd.read_stata(stata_path, chunksize=3)
for chunk in posts_stata_reader:
    print(chunk)

