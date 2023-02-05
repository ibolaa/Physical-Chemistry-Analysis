# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#data
P = np.array([0.05,0.052,0.054,0.056,0.058,0.060])
V = np.array([0.9960,0.9446,0.9191,0.8879,0.8743,0.8382])
data = (P,V)
data = pd.DataFrame(data)
data.index = ['P','V']  # type: ignore
data.columns =  ["1","2","3","4","5","6"]  # type: ignore
data # type: ignore

# Deney 1 - Boyle Mariotte

#plot a linear regression graph
sns.regplot(P*V,P, color="blue", marker="+",scatter_kws={"s": 30},    line_kws={"linewidth": 0.5}, ci=None,truncate=True,order=1,robust=True) # type: ignore
plt.xlabel("P (atm)")
plt.xlim(0.049,0.051)
plt.ylabel("P.V (atm.L)")
plt.ylim(0.049,0.062)

plt.title(" Boyle Mariotte PV / P")
plt.grid(   axis="both",    which="both",    color="black",    linestyle="-",    linewidth=0.5)
plt.savefig("Boyle_Mariotte_PVP.png")
plt.show()







# %%



