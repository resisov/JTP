import argparse
from rootpy.io import root_open
import rootpy.ROOT as ROOT
from rootpy.plotting import Hist, HistStack, Legend, Canvas
import rootpy.plotting.root2matplotlib as rplt
import matplotlib.pyplot as plt

# --Setup parser
parser = argparse.ArgumentParser()
parser.add_argument('infile', type=str,
            help="python W_anal.pyyour INPUT_ROOTFILE_PATH")
parser.add_argument('--save', type=bool,default=False,
            help="--save True/False")
parser.add_argument('--TCanvas', type=bool,default=False,
            help="--TCanvas True/False")

args = parser.parse_args()




# --Set your Delphes/libDelphes.so path, header path
ROOT.gSystem.Load("/x5/cms/jwkim/Delphes_NEW/Delphes3.4.2/libDelphes.so")

try:
  ROOT.gInterpreter.Declare('#include "classes/DelphesClasses.h"')
  ROOT.gInterpreter.Declare('#include "external/ExRootAnalysis/ExRootTreeReader.h"')
except:
  pass



# Read & Write File
inputFile = args.infile

if args.save:
	outputFile = root_open("W-mass.root","recreate")

# Create chain of root trees
chain = ROOT.TChain("Delphes")
chain.Add(inputFile)

# Create object of class ExRootTreeReader
treeReader = ROOT.ExRootTreeReader(chain)
numberOfEntries = treeReader.GetEntries()

# Get pointers to branches used in this analysis
branchMET = treeReader.UseBranch("MissingET")
branchElectron = treeReader.UseBranch("Electron")

# Define histograms
histMass = ROOT.TH1F("mass", "W^{+} Transverse Mass",100, 0, 300.0)



# --EventLoop start
for entry in range(0, numberOfEntries):
	# Load selected branches with data from specified event
	treeReader.ReadEntry(entry)

	# If event contains at least 1 electrons
	if branchElectron.GetEntries() == 0:
		continue
	
	# Take e, ve
	elec = branchElectron.At(0)
	metc = branchMET.At(0)


	TVmass = (elec.P4() + metc.P4()).Mt()

	# Plot their transverse mass
	histMass.Fill(TVmass)


# I/O
if args.save:
	outputFile.write()
	outputFile.close()

# -- EventLoop Ends

# --Show histogram using TCanvas
if (not args.save and args.TCanvas ):

	c1 = ROOT.TCanvas()
	c1.cd()
	histMass.GetXaxis().SetTitle("M_{T} [GeV]")
	histMass.GetYaxis().SetTitle("Events")
	histMass.Draw("Hist")
	dummy=input("Press Enter to continue...")


# --Show histogram using Matplotlib
if (not args.save and not args.TCanvas):
	# Set parametres for plotting
	plt.rcParams["figure.figsize"] = (10,6)
	plt.rc('xtick', labelsize=15)
	plt.rc('ytick', labelsize=15)
	plt.title("Transverse mass", fontsize=25)
	plt.xlabel("$M_{T} [GeV]$",fontsize=15)
	plt.ylabel("Events",fontsize=15)
	
	plt.grid(which='major', linestyle='-.')
	
	# Draw hist
	rplt.hist(histMass,linewidth=3, color="royalblue",label="W^{+} transverse mass")
	plt.xticks([0,20,40,60,80,100,120,140,160,180,200])
	plt.yticks([0,20,40,60,80,100,120,140])
	plt.legend()
	plt.show()

