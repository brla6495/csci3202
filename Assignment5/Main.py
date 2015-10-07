from Graph import *
from time import *
import sys

print ("")
print ("-----------------------------------------")
fileName = raw_input("Name of World File: ")
file = open(fileName, 'r')
print ("")
e = raw_input ("Value for e: ")
print ("-----------------------------------------")
print ("")
    
g = Graph(GRAPH_WIDTH,GRAPH_HEIGHT, e, .9)
getGraph(file,g,GRAPH_HEIGHT)
s = Search(g.getNode(0,0), g.getNode(GRAPH_WIDTH-1,GRAPH_HEIGHT-1), g)

for i in range(21):
    sys.stdout.write('\r')
    sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
    sys.stdout.flush()
    sleep(0.035)

s.printSearch()