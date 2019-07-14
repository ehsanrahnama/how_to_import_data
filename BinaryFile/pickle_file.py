import pickle
import os

ROOT_DIR = os.getcwd()
pkl_path = os.path.join(ROOT_DIR, 'BinaryFile', 'data', 'posts-100.pkl')

with open(pkl_path, 'rb') as pickle_file:
    posts_pickle = pickle.load(pickle_file)

print(type(posts_pickle)) # It is Data Frame 
print(posts_pickle.head())

# using pandas 
import pandas as pd 

posts_pickle = pd.read_pickle(pkl_path)
print(posts_pickle.columns)