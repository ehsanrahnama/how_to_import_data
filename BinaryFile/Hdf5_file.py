# HDF5 Stand for Hierarchical Data Format 5
## h5py library

import os 
import h5py

ROOT_DIR = os.getcwd()
h5_path = os.path.join(ROOT_DIR, 'BinaryFile', 'data', 'posts-100.h5')

h5_file = h5py.File(h5_path, 'r')
print("KEY:",list(h5_file.keys()))
dataset_h5 = h5_file['posts']
print(type(dataset_h5))
print('\n')
print(dir(dataset_h5))


for post in dataset_h5['table']:
    print(post)


# using pandas

import pandas as pd 

posts_hdf = pd.read_hdf(h5_path, 'posts')

print(posts_hdf.columns)
print(posts_hdf.keys())

posts_hdf = pd.read_hdf(h5_path, 'posts', start=2, stop=5, columns=['CreationDate', 'Title', 'Tags'])
print(posts_hdf)

posts_hdf = pd.read_hdf(h5_path, 'posts', columns=['Score', 'Tags'], where='Score>10 or Tags="<machine-learning>"')
print(posts_hdf.head())
