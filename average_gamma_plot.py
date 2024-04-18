"""""
Average Lorentz factor evolution plot
"""""

import matplotlib.pyplot as plt
import h5py
import glob
import pandas as pd

dir = os.getcwd()
wdir = dir+"/data/"
wdir=sorted(glob.glob(wdir+"*.dbl.h5"), key=lambda file: int(file.split(".",)[1]))

def gamma(v):
    return 1/(1-v*v)**0.5

def average_gamma_plot(files):

    avg_gamma  = []
    coord = []

    for file in files: 
        
        data = h5py.File(file, "r")
        coords=pd.DataFrame(data["node_coords" ]["X"])
        time = list(data.keys())[0]
        print(time)

        v = pd.DataFrame(data[time+"/vars/vx1"])
        
        print(max(v[0]), gamma(max(v[0])))

        # m=gamma*rhos + (3+v**2)*p

        # max_v = v[0].idxmax()
        # print(max_v)

        # gam_avg = (gamma[:max_v]*m[:max_v]*(cells[:max_v])**2).sum()/(m[:max_v]*(cells[:max_v])**2).sum()

        avg_v = v[0].mean()

        avg_gamma = gamma(avg_v)
        print(gam_avg)

        avg_gamma.append(gam_avg)
        coord.append(coords[0][v[0].idxmax()])
        data.close()

    plt.plot(coord, avg_gamma marker=".",color="black")

        
    