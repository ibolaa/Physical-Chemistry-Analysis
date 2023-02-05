
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


v=np.array([50,52,54,56,58,60])
p=np.array([1009.2,957.2,931.3,899.7,885.9,849.4])
data =(v,p)


# Use similar to plt.figure() except use tuple unpacking to grab fig and axes
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
axes[0].plot(v,p, color="blue", marker="+",markersize=10, linewidth=0.5)
axes[0].set_xlabel('V (mL)')
axes[0].set_xlim(48,62)
axes[0].set_ylabel('P (hpa)')
axes[0].set_ylim(840,1020)
axes[0].set_title('(2)Boyle Mariotte hpa / ml'); #; hides Out[]
axes[0].grid(   axis="both",    which="both",    color="black",    linestyle="-",    linewidth=0.5)

axes[1].plot(1/v,p,marker='+',color="blue",markersize=10, linewidth=0.5)
axes[1].set_xlabel('1/V (mL)')
axes[1].set_xlim(0.016,0.021)
axes[1].set_ylabel('P (hpa)')
axes[1].set_ylim(825,1025)
axes[1].set_title('(1) Boyle Mariotte 1/v / hpa'); #; hides Out[]
axes[1].grid(   axis="both",    which="both",    color="black",    linestyle="-",    linewidth=0.5)
plt.show()
fig.title('Boyle Mariotte (P,V) Föy Grafikleri') # type: ignore
fig.savefig("fiziko lab\Deney 1\Boyle Mariotte (P,V)\Grafikler")












