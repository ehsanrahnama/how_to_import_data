import numpy as np 

"""
    1. Using numpy for load file that has only numbers
    2. It is not working with simple text file  
"""

def simple_load_text(fname):
    loaded = np.loadtxt(fname)
    return loaded

slt = simple_load_text(fname='badges-five-numpy.txt')
print(slt)
print(slt.shape)
print(slt.size)

print("================================================")

def delimeter_load_text(fname, delimiter):
    loaded = np.loadtxt(fname=fname, delimiter=delimiter)
    return loaded

dlt = delimeter_load_text(fname='badges-five.txt', delimiter=',')
print(dlt)

print("================================================")

def columns_load_text(fname, delimiter, num1, num2):
    tuple_1 = (num1, num2)
    loaded = np.loadtxt(fname, delimiter=delimiter, usecols=tuple_1)
    return loaded

clt = columns_load_text(fname='badges-five.txt', delimiter=',', num1=0, num2=2)
print(clt)

print("================================================")

def skip_load_text(fname, delimiter, skiprows):
    loaded = np.loadtxt(fname=fname, delimiter=delimiter, skiprows=skiprows)
    return loaded

skiplt = skip_load_text('badges-five-header.txt', ',', 1)
print(skiplt)

print("================================================")

def increase_id(the_id):
    return int(the_id) + 1000

loaded = np.loadtxt(fname='badges-five-header.txt', delimiter=',', skiprows=1, dtype='uint16', 
                    converters={0:increase_id})
print(loaded)

print("================================================")

load_missong_value = np.genfromtxt('badges-five-missing-value.txt', delimiter=',', skip_header=1)
print(load_missong_value)







