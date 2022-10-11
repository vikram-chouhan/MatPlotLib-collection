import pandas as pn
import numpy as np
#List
l = [1,2,3,4]
a = pn.Series(l)
print("List Series")
print(a,"\n")

#Tuple
t =(1,2,3,4,5)
b = pn.Series(t)
print("Tuple Series {b}")
print(b,"\n")

#Dictionary
d = {"d1":'mon','d2':'tue','d3':'wed'}
c = pn.Series(d)
print("Dictionary Series")
print(c,"\n")

#Array
ar = np.arange(0,20,5)
k = pn.Series(ar)
print("Array Series")
print(k,"\n")

#Adding 2 series
_add = a+k
print(_add,"\n")

#Multiplying 2 Series
_m = a*k
print("Multiplying 2 Series")
print(_m,"\n")

#Accessing value in a series
print("Accessing value in a series")
print(d["d1"],"\n")
