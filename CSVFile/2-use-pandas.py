import pandas as pd
import re

file_path = '/home/ehsan/Desktop/ImportData/CSVFile/posts-100.csv'

# load csv file with pd.read_csv
posts_csv = pd.read_csv(file_path)
print(posts_csv)

# load five first row 
print(posts_csv.head())

# Specify row by define n 
print(posts_csv.head(n=6))

# load data from url (remote file)
# remote_file = ''

# data_url = pd.read_csv(remote_file, header=None)
# print(data_url)

# load data by defined how many rows that wanted
posts_small = pd.read_csv(file_path, nrows=3, skiprows=3)
print(posts_small)

# Specify row by using function
post_odd = pd.read_csv(file_path, skiprows=lambda x: x%2 != 0)
print(post_odd.head())

# loading certain columns with usecols
post_columns = pd.read_csv(file_path, usecols=[1,4,8])
print(post_columns.head())
print(post_columns.columns)

# using prefix to set name for csv file doesn't have header
post_columns = pd.read_csv(file_path, header=None, prefix='Col')
print(post_columns.columns)

# Set columns name
header_fields = ["Id","PostTypeId","CreationDate","Score","ViewCount",
                "LastActivityDate","Title","Tags","AnswerCount","CommentCount",
                "FavoriteCount","ClosedDate"]
post_columns = pd.read_csv(file_path, names=header_fields)
print(post_columns.head())

# Read csv file has heder 
file_path_1 = '/home/ehsan/Desktop/ImportData/CSVFile/posts-100-header.csv'
post_header = pd.read_csv(file_path_1 )
print(post_header.columns)
print(post_header[['Id', 'Title']].head())

# Do not know file have header or not 
post_reader = pd.read_csv(file_path_1, header='infer')
print(post_reader.columns)

# Using Type and specify Type
post_reader = pd.read_csv(file_path_1, usecols=[0,1,2,7])
print(post_reader.dtypes)

post_reader = pd.read_csv(file_path_1, usecols=[0,1,2,7], dtype={'PostTypeId': float})
print(post_reader.dtypes)

# Apply Function to Columns
post_tags =pd.read_csv(file_path_1, usecols=[0,1,2,7])
print(post_tags.head())
print(post_tags.iloc[1])
print(post_tags.iloc[1]['Tags'])

post_tags =pd.read_csv(file_path_1, usecols=[0,1,2,7], converters={'Tags':lambda x: re.findall('<[A-Za-z0-9_-]*>',x)})
print(post_tags.head())
print(post_tags.iloc[1]['Tags'])
print(type(post_tags.iloc[1]['CreationDate']))


post_tags = pd.read_csv(file_path_1, usecols=[0,1,2,7], parse_dates=['CreationDate'])
print(post_tags.dtypes)


# Missing Values
post_reader = pd.read_csv(file_path_1, usecols=[0, 3, 4, 8, 9, 10], na_filter=False)
print(post_reader.head())
# can not converted str to float if na_filter=False
post_reader = pd.read_csv(file_path_1, usecols=[0, 3, 4, 8, 9, 10], na_filter=True, dtype={'ViewCount': float})
print(post_reader.head())

# post_reader = pd.read_csv(file_path_1, usecols=[0, 3, 4, 8, 9, 10], keep_default_na="sad")
# print(post_reader.head())


print("==========================================================")
# load tsv file tab seperated value
file_path_2 = '/home/ehsan/Desktop/ImportData/CSVFile/posts-100.tsv'
post_reader = pd.read_csv(file_path_2, sep='\t')
print(post_reader.head())




