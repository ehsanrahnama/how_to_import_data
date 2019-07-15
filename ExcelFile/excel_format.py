import pandas as pd 
import os 

# It has should installed xlrd by pip 

ROOT_DIR = os.getcwd() 
excel_path = os.path.join(ROOT_DIR, 'ExcelFile', 'stackoverflow.xlsx' )
excel_path_2 = os.path.join(ROOT_DIR,'ExcelFile', 'stackoverflow-one.xlsx')

excel_file = pd.ExcelFile(excel_path)

print(type(excel_file))

# sheet name of excel file 
print(excel_file.sheet_names)

# Change to Data Frame like as Pandas Data Frame
# Can work like pandas 
excel_df = excel_file.parse()
print(type(excel_df))
print(excel_df.head())

# read_excel is another attrib for loading excel file
posts_excel = pd.read_excel(excel_path_2)
print(type(posts_excel))
print(posts_excel.columns)
print(posts_excel.head())

# Specify Columns
posts_excel = pd.read_excel(excel_path_2, usecols=[0, 3])
print(posts_excel.head())
print(posts_excel.columns)

posts_excel = pd.read_excel(excel_path_2, usecols='A:C').columns # A to C
print(posts_excel)

posts_excel = pd.read_excel(excel_path_2, usecols='A,C').columns # A and C
print(posts_excel)

# Use Sheet name of file excel
 
post_dict = pd.read_excel(excel_path, sheet_name=None)
print(type(post_dict))
print(post_dict.keys())
print(post_dict['Posts'].head())

# Handle Missing Columns 
post_dict = pd.read_excel(excel_path, sheet_name='Users').head() 
print(40*'-')
post_dict =pd.read_excel(excel_path, sheet_name='Users', usecols=range(1,9), skiprows=1).head()
print(post_dict)

print(40*'-')
print('\n')
post_dict = pd.read_excel(excel_path, sheet_name=2, nrows=3, skiprows=1).head() # sheet_name= string, integer
print(post_dict)
print('\n')

# Change Data Type of columns
posts_excel = pd.read_excel(excel_path, sheet_name=2, usecols=range(1,9), skiprows=1).dtypes
print(posts_excel)
print(40*'-')

posts_excel = pd.read_excel(excel_path, sheet_name=2, usecols=range(1,9), skiprows=1, dtype={'PostTypeId':str}).dtypes
print(posts_excel)
print('\n')


# Using Converter
posts_excel = pd.read_excel(excel_path, sheet_name=2, usecols=range(1,9), skiprows=1,
                            converters={'Id':lambda x: x+1000}).head()
print(posts_excel)
print('\n')

# Handle NAN Value

posts_excel = pd.read_excel(excel_path, sheet_name='Posts', usecols=[0, 7, 8], skiprows=1, keep_default_na=False)
print(posts_excel.head())