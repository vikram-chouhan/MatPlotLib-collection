import matplotlib.pyplot as pl
import numpy as np
yr=np.arange(2002,2012)
cs=[]
ip=[]

for i in yr:
    c=int(input(f"enter CS percentage in {i}"))
    i=int(input(f"enter IP percentage in {i}"))
    cs.append(c)
    ip.append(i)
    
pl.plot(yr,cs,'c',marker="o",markersize="6",markeredgecolor='y',label="cs")
pl.plot(yr,ip,'b',marker="x",markersize="8",markeredgecolor='r',label="ip")
pl.xlabel("year")
pl.ylabel("percentage")
pl.title("performance")
pl.grid(True)
pl.legend()
pl.show()
