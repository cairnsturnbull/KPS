"""
Maximum Lorentz factor evolution plot
"""

import matplotlib.pyplot as plt
from multiprocessing import Pool
import h5py
import glob
import pandas as pd
import os
import time 
import pyPLUTO as pp

dir = os.getcwd()
wdir = dir+"/data/"
wdir=sorted(glob.glob(wdir+"*.dbl.h5"), key=lambda file: int(file.split(".",)[1]))[:100]

def gamma(v):
    return 1/(1-v*v)**0.5

def max_gamma_plot(files):
    
    start = time.process_time()
    percent_interval = len(wdir) // 100

    max_gamma  = []
    coord = []
    i=0
    
    for file in files:

        data = h5py.File(file, "r")
        coords=pd.DataFrame(data["node_coords" ]["X"])
        step = list(data.keys())[0]
         
        v = pd.DataFrame(data[step+"/vars/vx1"])

        max_gamma.append(gamma(max(v[0])))
        coord.append(coords[0][v[0].idxmax()])

        if int(step.split("_")[1]) % percent_interval == 0:

            end = time.process_time()
            i+=1

            print(step,i,"%,", end - start,"s")
       
        data.close()
       
    plt.scatter(coord, max_gamma, marker=".", color="black")
    plt.xlabel("r")
    plt.ylabel(r"$\gamma_{max}$")
    plt.xscale('log')
    plt.yscale('log')
    plt.title("Max gamma evolution")

    plt.savefig("images/gamma_max_plot.png")
    plt.show()

if __name__ == "__main__":

    with Pool(8) as p: 

        p.map(max_gamma_plot, [wdir])
        

# 10000 files  
        
# 2 cores: 104 seconds
# 5 cores: 101 seconds
# 6 cores: 101 seconds, 101
# 7 cores:  98 seconds, 94, 99
# 8 cores:  99 seconds
# 10 cores: 98 seconds, 103
# 12 cores: 102 seconds
        
        
# 100000 files 
        
# 7 cores: 44:50 (for running PLUTO)
# 7 cores:  344 seconds, 333
# 8 cores: 30:05, 215
