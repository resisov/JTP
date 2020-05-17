import pandas as pd
from ROOT import *
from root_numpy import root2array, tree2array
from root_numpy import testdata
from IPython.display import display
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')

def Ntuple2array(filename, treename):
        f = TFile.Open(filename)
        mytree = f.Get(treename)
        data = tree2array(mytree)
        #data=list(itertools.chain(*data))
        data = pd.DataFrame(data)
        return data


data = Ntuple2array("ntuple.root","mytree")

branch_name_1 = "signal"
data_br_1   = data[branch_name_1]

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

plt.rc('xtick', labelsize = 20)
plt.rc('ytick', labelsize = 20)
plt.rcParams["figure.figsize"] = (12,12)
plt.xlabel('X',fontsize=25)
plt.ylabel('Number of events',fontsize=20)
plt.title("Gauss distribution",fontsize=20)

plt.grid(which='major', linestyle='-')
plt.minorticks_on()

bins = 200
plt.hist(data_br_1, bins=bins, histtype='step',linewidth=3, color="royalblue")
#plt.show()
plt.savefig("gauss.png")

