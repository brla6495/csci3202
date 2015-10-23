class NodeP:
    def __init__(self, pTrue, name):
        self.pTrue = pTrue
        self.name = name
        self.cancerNode = None
        self.sortOrder = 1
    
    def prob(self, isTrue):
        prob = self.pTrue if isTrue else 1.0 - self.pTrue
        return prob
        
    def con(self, selfTrue, otherNode, isTrue):
        prob = 0.0
        if (otherNode == self):
            prob = 1.0 if selfTrue else 0.0
        elif (isinstance(otherNode, NodeP)):
            prob = self.prob(selfTrue)
        elif (otherNode == self.cancerNode):
            prob = otherNode.con(isTrue, self, selfTrue) * self.prob(selfTrue) / otherNode.prob(isTrue)
        else:
            c = self.cancerNode.con(True, self, selfTrue)
            prob = otherNode.con(isTrue, self.cancerNode, True) * c + otherNode.con(isTrue, self.cancerNode, False) * (1 - c)
            prob *= self.prob(selfTrue) / otherNode.prob(isTrue)
        return prob
    
    def conD(self, selfTrue, node1, node2, isTrue1, isTrue2):
        prob = 0.0
        if (node1 == self or node2 == self):
            prob = 1.0 if selfTrue else 0.0
        elif (node1 == self.cancerNode and isinstance(node2, NodeP)):
            prob = self.cancerNode.conD(isTrue1, self, node2, selfTrue, isTrue2) * self.prob(selfTrue)
            prob /= self.cancerNode.con(isTrue1, node2, isTrue2)
        elif (isinstance(node1, NodeP) and node2 == self.cancerNode):
            prob = self.cancerNode.conD(isTrue2, self, node1, selfTrue, isTrue1) * self.prob(selfTrue)
            prob /= self.cancerNode.con(isTrue2, node1, isTrue1)
        elif (isinstance(node1, NodeCh) and isinstance(node2, NodeP)):
            prob = self.con(selfTrue, node1, isTrue1)
        elif (isinstance(node1, NodeP) and isinstance(node2, NodeCh)):
            prob = self.con(selfTrue, node2, isTrue2)
        elif (isinstance(node1, NodeCh) and node2 == self.cancerNode):
            prob = node2.con(isTrue2, self, selfTrue) * node1.conD(isTrue1, node2, self, isTrue2, selfTrue)
            prob *= self.prob(selfTrue) / (node1.prob(isTrue1) * node2.con(isTrue2, node1, isTrue1))
        elif (isinstance(node2, NodeCh) and node1 == self.cancerNode):
            prob = node1.con(isTrue1, self, selfTrue) * node2.conD(isTrue2, node1, self, isTrue1, selfTrue)
            prob *= self.prob(selfTrue) / (node2.prob(isTrue2) * node1.con(isTrue1, node2, isTrue2))
        else:
            prob = node1.con(isTrue1, self, selfTrue) * node2.conD(isTrue2, node1, self, isTrue1, selfTrue)
            prob *= self.prob(selfTrue) / (node1.prob(isTrue1) * node2.con(isTrue2, node1, isTrue1))
        return prob