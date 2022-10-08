import matplotlib.pyplot as ag
import numpy as np
x=["Maths","science","english","hindi","SST"]
y1=[80,93,75,91,68]
y2=[84,91,72,87,84]
y3=[72,84,67,89,71]
y4=[46,96,78,87,98]
A= np.arange(5)
ag.bar(x,y1,width=0.2,color="c",label="term 1")
ag.bar(A+0.2,y2,width=0.2,color="m",label="CT 1")
ag.bar(A+0.4,y3,width=0.2,color="g",label="term 2")
ag.bar(A+0.6,y4,width=0.2,color="yellow",label="CT 2")
ag.xlabel("SUBJECTS")
ag.ylabel("PERCENTAGE")
ag.title("Performance in 5 subjects")
ag.legend()
ag.show()
