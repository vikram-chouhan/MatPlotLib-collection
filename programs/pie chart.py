import matplotlib.pyplot as mt
l=[20,35,78,60]
mycolors=["blue","green","yellow","c"]
myexplode=[0,0,0.2,0]
mylabels=["mango","banana","guava","apple"]
mt.pie(l,colors=mycolors,explode=myexplode,labels=mylabels)
mt.legend()
mt.show()

