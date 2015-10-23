class NodeCa:
    def __init__(self, pollutionNode, smokerNode):
        self.pollutionNode = pollutionNode
        self.smokerNode = smokerNode
        self.probTable = [(False, True, 0.05), (False, False, 0.02), (True, True, 0.03), (True, False, 0.001)]
        self.name = "Cancer"
        self.sortOrder = 0
    
    def prob(self, isTrue):
        pTrue = 0.0
        for p, s, val in self.probTable:
            pTrue += val * self.pollutionNode.prob(p) * self.smokerNode.prob(s)
        prob = pTrue if isTrue else 1.0 - pTrue
        return prob
    
    def con(self, selfTrue, otherNode, isTrue):
        prob = 0.0
        if (otherNode == self):
            prob = 1.0 if selfTrue else 0.0
        elif (otherNode == self.pollutionNode):
            for p, s, val in self.probTable:
                if (p == isTrue):
                    prob += val * self.smokerNode.prob(s)
            prob = prob if selfTrue else 1.0 - prob
        elif (otherNode == self.smokerNode):
            for p, s, val in self.probTable:
                if (s == isTrue):
                    prob += val * self.pollutionNode.prob(p)
            prob = prob if selfTrue else 1.0 - prob
        else:
            prob = otherNode.con(isTrue, self, selfTrue) * self.prob(selfTrue) / otherNode.prob(isTrue)
        return prob
    
    def conD(self, selfTrue, node1, node2, isTrue1, isTrue2):
        prob = 0.0
        if (node1 == self or node2 == self):
            prob = 1.0 if selfTrue else 0.0
        elif (node1 == self.pollutionNode and node2 == self.smokerNode):
            for p, s, val in self.probTable:
                if (p == isTrue1 and s == isTrue2):
                    prob += val
            prob = prob if selfTrue else 1.0 - prob
        elif (node2 == self.pollutionNode and node1 == self.smokerNode):
            for p, s, val in self.probTable:
                if (p == isTrue2 and s == isTrue1):
                    prob += val
            prob = prob if selfTrue else 1.0 - prob
        else:
            prob = node1.con(isTrue1, self, selfTrue) * node2.conD(isTrue2, self, node1, selfTrue, isTrue1)
            prob *= self.prob(selfTrue) / (node1.prob(isTrue1) * node2.con(isTrue2, node1, isTrue1))
        return prob
