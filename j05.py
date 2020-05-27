# rootpy I/O
from rootpy.io import root_open

# rootpy for histograming
from rootpy.plotting import Hist, HistStack, Legend, Canvas

# rootpy for matplotlib 
import rootpy.plotting.root2matplotlib as rplt
import matplotlib.pyplot as plt

xsec1 = (4043.5)*1000
xsec2 = (6268.2)*1000

lumi = 150

tot_evt = 100000

weight1 = xsec1 * lumi / tot_evt
weight2 = xsec2 * lumi / tot_evt 


myfile1 = root_open("W-mass.root")
myfile2 = root_open("Wmass.root")

myhist1 = myfile1.mass.Clone()
myhist2 = myfile2.mass.Clone()

# Find maximum bin
maxbin_n1 = myhist1.GetMaximumBin()
maxbin_n2 = myhist2.GetMaximumBin()

# Find maximum X value
maxX_n1 = myhist1.GetXaxis().GetBinCenter(maxbin_n1)
maxX_n2 = myhist2.GetXaxis().GetBinCenter(maxbin_n2)


##
# -  Normalize --- #


myhist1.Scale(weight1)
myhist2.Scale(weight2)
##


# find maximum Y value 
maxY_n1 = myhist1.GetBinContent(maxbin_n1)
maxY_n2 = myhist2.GetBinContent(maxbin_n2)

print("max bin, x, y:" ,maxbin_n1 ,maxX_n1 ,maxY_n1)
print("max bin, x, y:" ,maxbin_n2 ,maxX_n2 ,maxY_n2)




## -- Trial
G=(myhist1)
H=(myhist2)




## --Set parameters for plotting
plt.rcParams["figure.figsize"] = (10,6)
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)
plt.title("W Transverse mass",fontsize=20)
plt.grid(which='major', linestyle='-.')
plt.xlabel("M$_{T}$ [GeV]", fontsize=15)
plt.ylabel("Number of Events | 3GeV", fontsize=15)
plt.text(270.0,13300000.0, '150 fb$^{-1}$ [14 TeV]', ha='center',va='center',fontsize=15)
#plt.plot(myhist1, label='W+')
#plt.plot(myhist2, label='W-')
#plt.legend(['W+', 'W-'], fontsize=15)
plt.minorticks_on()


## --Draw hist
rplt.hist(H, linewidth=3,label='W$^{+}$',color="royalblue")
rplt.hist(G, linewidth=3,label='W$^{-}$',color="green")

## --stacking
#rplt.hist(myhist1, stacked=True, normed = True)
#rplt.hist(myhist2, stacked=True, normed = True)
#plt.xticks([0,20,40,60,80,100,120,140,160,180,200])
#plt.yticks([0,20,40,60,80,100,120,140,160])
plt.legend(fontsize=15)
#plt.show()

plt.savefig("w_complete2.png")

