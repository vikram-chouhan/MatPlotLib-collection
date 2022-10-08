import matplotlib.pyplot as pl
x=["CT1",'CT2','CT3','CT4']
eleven=[48,43,79,95]
twelve=[58,68,85,98]

pl.plot(x,eleven,'c',marker="o",markersize="6",markeredgecolor='y',label="XI Result")
pl.plot(x,twelve,'b',marker="x",markersize="8",markeredgecolor='r',label="XII Result")
pl.xlabel("Examination Name")
pl.ylabel("percentage")
pl.title("Performance for past 2 years")
pl.legend()
pl.show()
