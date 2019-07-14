# How to import SAS (statistical analysis software) ==> sas7bdat, pandas

## using sas7bdat
import os
from sas7bdat import SAS7BDAT

ROOT_DIR = os.getcwd()
sas_file_path = os.path.join(ROOT_DIR, 'BinaryFile', 'data', 'posts-100.sas7bdat')

with SAS7BDAT(sas_file_path) as sas_file:
    user_sas_df = sas_file.to_data_frame()
    print(sas_file)
    print(user_sas_df)
    print(type(user_sas_df))

print(20*'---')


print("COLUMNS: ", sas_file.column_names)
print(sas_file.header)

print(20*'---')
print('\n')


## using pandas

import pandas as pd 

posts_sas = pd.read_sas(sas_file_path)

print(posts_sas.head())
print(posts_sas.columns)
print('\n')

posts_sas_reader = pd.read_sas(sas_file_path, chunksize=4)
print(posts_sas_reader.read())