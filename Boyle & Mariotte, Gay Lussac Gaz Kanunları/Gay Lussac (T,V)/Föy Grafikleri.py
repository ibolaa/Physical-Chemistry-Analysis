# %%
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# %%
# %%
t = np.array([26,31,37,43,48])
v = np.array([48,49,50,51,52])
m = 0.1783
b = 43.40127
x = np.linspace(-300,100,100)
y= m*x + b
data =(t,v)
data = pd.DataFrame(data)
data.index = ["t","v"] #type: ignore
data.columns = ["1","2","3","4","5"] #type: ignore


# %%
# Use similar to plt.figure() except use tuple unpacking to grab fig and axes
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 6))

axes.plot(x,y,color="blue",markersize=10, linewidth=0.5)
axes.set_xlabel('T (°C)')
#set the x limit to x axis cross the y axis
plt.xlim(-273.15,100)
plt.ylim(0,100)
axes.set_ylabel('V (mL)')
axes.set_title('(2) Gay Lussac')
axes.grid(   axis="both",    which="both",    color="black",    linestyle="-",    linewidth=0.5)

plt.show()
#fig.savefig("Gay Lussac (T,V)\Gay Lussac Föy Grafikleri.png")

# %%


# %%



