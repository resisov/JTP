from rootpy.tree import Tree
from rootpy.io import root_open
from random import gauss


f = root_open("ntuple.root", "recreate")

tree = Tree("mytree")
tree.create_branches(
        {'signal' : 'F' }
)

mean = 91
sigma = 2

for i in range(10000):
        tree.signal = gauss(mean, sigma)
        tree.fill()

tree.write()
f.close()

