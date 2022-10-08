import numpy as np
import matplotlib.pyplot as mp

X= np.array(5)
x=["CT 1", "TERM 1","CT 2", "TERM 2"]
y1=[84,87,78,61]
y2=[61,75,70,80]
y3=[55,59,52,89]
y4=[84,92,94,96]

mp.bar(x,y1, width=0.2, color="c")
mp.bar(X+0.2,y2, width=0.2, color="y")
mp.bar(X+0.2,y3, width=0.2,color="g")
mp.bar(X+0.2,y4, width=0.2,color="m")
mp.show()
