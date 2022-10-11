import matplotlib.pyplot as plt
m=['jan','feb','march','april','may','june','july','aug','sep','oct','nov','dec']
h=[68,74,85,96,102,101,95,92,92,89,81,71]
l=[47,53,62,72,80,83,82,80,77,67,56,48]

plt.plot(m,h,'c',linestyle="dashed" ,markeredgecolor="red", markersize=4,marker="o",label= "high temperature")
plt.plot(m,l,'g',linestyle="dotted" ,markeredgecolor="blue" ,marker="*",markersize=5,label= "low temperature")
plt.xlabel("months")
plt.ylabel("temperatures")
plt.title("avg temperature throughout the year")
plt.legend()
plt.show()
