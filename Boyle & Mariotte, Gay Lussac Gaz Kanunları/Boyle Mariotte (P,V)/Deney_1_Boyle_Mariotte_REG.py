
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#data
x = np.array([0.05,0.052,0.054,0.056,0.058,0.060])
y = np.array([0.9960,0.9446,0.9191,0.8879,0.8743,0.8382])
data = (x,y)
data = pd.DataFrame(data)
data.index = ['x','y']  # type: ignore
data.columns =  ["1","2","3","4","5","6"]  # type: ignore
data # type: ignore

# Deney 1 - Boyle Mariotte

#plot a linear regression graph
sns.regplot(x,y, color="red", marker="+",scatter_kws={"s": 30},    line_kws={"linewidth": 0.5}, ci=None,truncate=True,order=1,robust=True) # type: ignore
plt.xlabel("V (L)")
plt.xlim(0.048,0.062)
plt.ylim(0.80,1.0250)
plt.ylabel("P (atm)")

plt.title("Boyle-Mariotte Deneyi Lineer Regresyon Grafiği")
plt.grid(   axis="both",    which="both",    color="black",    linestyle="-",    linewidth=0.5)
plt.savefig("fiziko lab\Deney 1\Boyle Mariotte (P,V)\Grafikler")
plt.show()





