import matplotlib.pyplot as pl
import numpy as np
time=np.linspace(1,12,4)
day1=[34,45,34,47]
day2=[35,37,48,49]

pl.plot(time,day1,'c',marker="o",markersize="6",markeredgecolor='y',label="DAY 1")
pl.plot(time,day2,'b',marker="x",markersize="8",markeredgecolor='r',label="DAY 2")
pl.xlabel("Time")
pl.ylabel("Max Temperature")
pl.title("Temperature graph")
pl.legend()
pl.show()
