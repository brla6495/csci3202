class NodeCh:
    def __init__(self, pTrueCTrue, pTrueCFalse, cancerNode, name):
        self.pTrueCTrue = pTrueCTrue
        self.pTrueCFalse = pTrueCFalse
        self.cancerNode = cancerNode
        self.name = name
        self.sortOrder = 2
    
    def prob(self, isTrue):
        pTrue = self.pTrueCTrue * self.cancerNode.prob(True) + self.pTrueCFalse * self.cancerNode.prob(False)
        prob = pTrue if isTrue else 1.0 - pTrue
        return prob
    
    def con(self, selfTrue, otherNode, isTrue):
        prob = 0.0
        if (otherNode == self):
            prob = 1.0 if selfTrue else 0.0
        elif (otherNode == self.cancerNode):
            p = self.pTrueCTrue if isTrue else self.pTrueCFalse
            prob = p if selfTrue else 1.0 - p
        else:
            c = self.cancerNode.con(True, otherNode, isTrue)
            prob = self.con(selfTrue, self.cancerNode, True) * c + self.con(selfTrue, self.cancerNode, False) * (1 - c)
        return prob
    
    def conD(self, selfTrue, node1, node2, isTrue1, isTrue2):
        prob = 0.0
        if (node1 == self or node2 == self):
            prob = 1.0 if selfTrue else 0.0
        elif (node1 == self.cancerNode and isinstance(node2, NodeP)):
            prob = self.con(selfTrue, self.cancerNode, isTrue1)
        elif (node2 == self.cancerNode and isinstance(node1, NodeP)):
            prob = self.con(selfTrue, self.cancerNode, isTrue2)
        elif (isinstance(node1, NodeP) and isinstance(node2, NodeP)):
            prob = node1.con(isTrue1, self, selfTrue) * node2.con(isTrue2, self, selfTrue)
            prob *= self.prob(selfTrue) / (node1.prob(isTrue1) * node2.prob(isTrue2))
        else:
            c = self.cancerNode.conD(True, node1, node2, isTrue1, isTrue2)
            prob = self.con(selfTrue, self.cancerNode, True) * c + self.con(selfTrue, self.cancerNode, False) * (1 - c)
        return prob
