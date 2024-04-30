"""
Plotting timestep variables
"""

import numpy as np
import matplotlib.pyplot as plt
import pyPLUTO as pp
import pandas as pd 
import h5py
import seaborn as sns   
import os
sns.set_style("ticks")

dir = os.getcwd()
print(dir)
wdir = dir+"/data/"
nlinf = pp.nlast_info(w_dir=wdir)

# functions
def gamma(v):
    return 1/np.sqrt(1-v**2)


# last timestep
# timestep=str(nlinf["nlast"])
# data = h5py.File(wdir + "data.000"+str(nlinf["nlast"])+".dbl.h5", "r")
# rho = pd.DataFrame(data["Timestep_"+str(nlinf["nlast"])+"/vars/rho"])
# v = pd.DataFrame(data["Timestep_"+str(nlinf["nlast"])+"/vars/vx1"])
# p = pd.DataFrame(data["Timestep_"+str(nlinf["nlast"])+"/vars/prs"])

# timestep = str(nlinf["time"]).split(".")[0]
timestep = 990
time = nlinf["time"]

data = h5py.File(wdir + "data.0"+str(timestep)+".dbl.h5", "r")
rho = pd.DataFrame(data["Timestep_"+str(timestep)+"/vars/rho"])
v = pd.DataFrame(data["Timestep_"+str(timestep)+"/vars/vx1"])
p = pd.DataFrame(data["Timestep_"+str(timestep)+"/vars/prs"])

coord=pd.DataFrame(data["cell_coords" ]["X"])

print(v[0].max(), gamma(v[0].max()))

# plotting timestep

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1, figsize=(10,10), sharex=True,)
# plt.subplots_adjust(hspace = 0.3)
plt.rc('font', weight='bold')

sns.scatterplot(x=coord[0], y=rho[0] , marker=".",color="red",ax=ax1,)
ax1.set(xscale="log",)# ylabel=r"$\rho$"+r" $(m_p\, g\,cm^{-3})") #title="t="+ str(nlinf["time"])[:-2]+"s")
ax1.set_ylabel(r"$\rho$ $(m_p\, g\,cm^{-3})$", weight='bold')

# ax1.(ylabel=r"$\rho$"+r" $(m_p\, g\,cm^{-3})$",weight="bold")

sns.scatterplot(x=coord[0], y=v[0] , marker=".",color="blue",ax=ax2)    
ax2.set(xscale="log",)
ax2.set_ylabel(ylabel=r"$\beta$", weight='bold')

sns.scatterplot(x=coord[0], y=gamma(v[0]) , marker=".",color="purple",ax=ax3)
ax3.set(xscale="log", ylabel=r"$\gamma$")

sns.scatterplot(x=coord[0], y=p[0] , marker=".",color="green", ax=ax4)
ax4.set(xscale="log",xlabel="r (light-second)", ylabel=r"$p$ $(dyn \, cm^{-2})$")
ax4.set_ylabel(ylabel=r"$p$ $(dyn \, cm^{-2})$", weight="bold")
ax4.set_xlabel(xlabel="r (light-second)", weight="bold")
plt.tight_layout()

plt.savefig("images/timestep_"+str(timestep)+".jpeg")
plt.show()
data.close()