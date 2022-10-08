import matplotlib.pyplot as ag

x=["Maths","science","english","hindi","SST"]
y=[80,93,75,91,68]
c=["c","r","y","b","g"]
ag.bar(x,y,width=0.5,color=c)
ag.xlabel("SUBJECTS")
ag.ylabel("PERCENTAGE")
ag.title("Performance in 5 subjects")
ag.show()
