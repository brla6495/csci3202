#!/usr/bin/env python
import argparse
import re
from NodeP import*
from NodeCh import*
from NodeCa import*

def calcCon(nodes, b):
    if len(nodes) == 1:
        return nodes[0].prob(b[0])
    elif len(nodes) == 2:
        return nodes[1].con(b[1], nodes[0], b[0])
    elif len(nodes) == 3:
        return nodes[2].conD(b[2], nodes[0], nodes[1], b[0], b[1])
    elif len(nodes) == 4:
        if isinstance(nodes[0], NodeCa):
            return nodes[3].con(b[3], nodes[0], b[0])
        else:
            p = nodes[2].con(b[2], nodes[3], b[3])
            p *= nodes[1].conD(b[1], nodes[2], nodes[3], b[2], b[3])
            p *= nodes[0].conD(b[0], nodes[2], nodes[3], b[2], b[3])
            p *= nodes[3].prob(b[3]) / comProb(nodes[:3], b[:3])
            return p
    elif len(nodes) == 5:
        return nodes[4].con(b[4], nodes[0], b[0])
    return 0.0

def comProb(nodes, b, printString = False):
    p = 1.0
    sol = "P( "
    for j in range(0, len(nodes)):
        p *= calcCon(nodes[:j+1], b[:j+1])
        sol += nodes[j].name + "=" + str(b[j]) + " "
    if (printString):
        print sol + ") = " + str(p)
    return p

def makeTable(nodes, truths):
    nodes, truths = zip(*sorted(zip(nodes, truths), key=lambda (n, b): n.sortOrder))
    for i in range(0, 2 ** len(nodes)):
        b = [bool(int(x)) for x in bin(i)[2:]]
        for a in range(0, len(nodes) - len(b)):
            b.insert(0, False)
        if (all((x == y or y == None) for x, y in zip(b, truths))):
            comProb(nodes, b, True)

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-g", type=str, default=None, required=False)
    argparser.add_argument("-j", type=str, default=None, required=False)
    argparser.add_argument("-m", type=str, default=None, required=False)
    argparser.add_argument("-pP", type=float, default=0.9, required=False)
    argparser.add_argument("-pS", type=float, default=0.3, required=False)
    args = argparser.parse_args()
    
    smokerNode = NodeP(args.pS, "Is a smoker?")
    pollutionNode = NodeP(args.pP, "Had pollution exposure?")
    cancerNode = NodeCa(pollutionNode, smokerNode)
    xrayNode = NodeCh(0.9, 0.2, cancerNode, "Had XRay Exposure?")
    dNode = NodeCh(0.65, 0.3, cancerNode, "Has Dyspnoea?")
    
    smokerNode.cancerNode = cancerNode
    pollutionNode.cancerNode = cancerNode
    
    nodes = {'S' : smokerNode, 'P' : pollutionNode, 'C' : cancerNode, 'X': xrayNode, 'D' : dNode}
    if (args.g != None):
        match = re.match(r'(~?)(\w{1}):(\w{1})(\w?)', args.g)
        aNode = nodes.get(match.group(2).capitalize())
        isTrue = True if match.group(1) == "" else False
        if match.group(4) != "":
            bNode1 = nodes.get(match.group(3).capitalize())
            bNode2 = nodes.get(match.group(4).capitalize())
            p = aNode.conD(isTrue, bNode1, bNode2, True, True)
            print "Bel(", aNode.name, "=", isTrue, "|", bNode1.name, "= True,", bNode2.name, "= True ) =", p
        else:
            bNode = nodes.get(match.group(3).capitalize())
            print "Bel(", aNode.name, "=", isTrue, "|", bNode.name, "= True) =", aNode.con(isTrue, bNode, True)
    elif (args.j != None):
        match = re.match(r'(~?)(\w{1})(~?)(\w?)(~?)(\w?)(~?)(\w?)(~?)(\w?)', args.j)
        if match:
            b = []
            n = []
            for i in range(1, 10, 2):
                if (match.group(i+1) != ""):
                    if (match.group(i+1).islower()):
                        bi = True if match.group(i) == "" else False
                    else:
                        bi = None
                    b.append(bi)
                    n.append(nodes.get(match.group(i+1).capitalize()))
            makeTable(n, b)
        else:
            print "No match"
        
    elif (args.m != None):
        node = nodes.get(args.m)
        print "Bel(", node.name, "= True) =", node.prob(True)