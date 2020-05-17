# rootpy for histograming
from rootpy.plotting import Hist, HistStack, Legend, Canvas

import matplotlib
matplotlib.use('Agg')


# rootpy fod matplotlib
import rootpy.plotting.root2matplotlib as rplt
import matplotlib.pyplot as plt

#pyroot
import ROOT

## --file name, Tree name
file_name = "ntuple.root"
tree_name = "mytree"

## --Hist define
h1 = Hist(200, 82, 100)

## --open file and read tree
root_file = ROOT.TFile.Open(file_name,'read')
tree = root_file.Get(tree_name)

## --start eve. loop
for Nevent, event in enumerate(tree):
        print(Nevent, event.signal)
        h1.Fill(event.signal)

## --close file
root_file.Close()


## --set parametres for plotting
plt.rcParams["figure.figsize"] = (7,5)
plt.rc('xtick', labelsize=20)
plt.rc('ytick', labelsize=20)
plt.title("Gauss distribution", fontsize=20)
plt.grid(which='major', linestyle='-')
plt.minorticks_on()

## --draw hist
rplt.hist(h1, linewidth=3, color="royalblue")
#plt.show()
plt.savefig("SSIBAL.png")

