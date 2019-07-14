# using scipy to import matlab file 

import os 
import scipy.io

ROOT_DIR = os.getcwd()
mat_path = os.path.join(ROOT_DIR, 'BinaryFile', 'data', 'posts-100.mat')

posts_mat = scipy.io.loadmat(mat_path)
print(type(posts_mat))
print(posts_mat.keys())
print(type(posts_mat['posts']))
print(posts_mat['posts'])
