from sys import argv
from Node import *
from Search import *
import math

GRAPH_WIDTH = 10
GRAPH_HEIGHT = 8

class Graph:
	def __init__(self, width, height, e, discount):
		self.width = width
		self.height = height
		self.E = float(e)
		self.discount = float(discount)
		self.data = []
		for i in range(0,height):
			self.data.append([])

	def addData(self, node, index):
		self.data[index].append(node)

	def getNode(self, x, y):
		if x < 0 or y < 0 or x >= GRAPH_WIDTH or y >= GRAPH_HEIGHT:
			return None
		else:
			for i in self.data:
				for node in i:
					if node.x == x and node.y == y:
						return node

	def setUtility(self):
		change = 100
		while change >= self.E * (1-self.discount)/self.discount:
			change = -100
			for i in range(0, self.width):
				for j in range(0, self.height):
					nodeMiddle = self.getNode(i,j)
					nodeNorth = self.getNode(i,j+1)
					nodeEast = self.getNode(i+1,j)
					nodeWest = self.getNode(i-1,j)
					nodeSouth = self.getNode(i,j-1)

					if nodeMiddle.util is not None and nodeMiddle.val is not 50:
						utilityNorth = None
						utilityEast = None
						utilityWest = None
						utilitySouth = None

						if nodeNorth is None or nodeNorth.util is None:
							utilityNorth = nodeMiddle.util
						else:
							utilityNorth = nodeNorth.util
						if nodeEast is None or nodeEast.util is None:
						    utilityEast = nodeMiddle.util
						else:
						    utilityEast = nodeEast.util
						if nodeWest is None or nodeWest.util is None:
						    utilityWest = nodeMiddle.util
						else:
						    utilityWest = nodeWest.util
						if nodeSouth is None or nodeSouth.util is None:
							utilitySouth = nodeMiddle.util
						else:
							utilitySouth = nodeSouth.util

						moveNorth = .8*utilityNorth + .1*utilityEast + .1*utilityWest
						moveEast = .8*utilityEast + .1*utilitySouth + .1*utilityNorth
						moveWest = .8*utilityWest + .1*utilityNorth + .1*utilitySouth
						moveSouth = .8*utilitySouth + .1*utilityWest + .1*utilityEast
						prevUtil = nodeMiddle.util
						nodeMiddle.util = max(moveNorth, moveEast, moveWest, moveSouth) + nodeMiddle.reward
						nodeMiddle.util = nodeMiddle.util*self.discount

						if abs(nodeMiddle.util - prevUtil) > change:
							change = abs(nodeMiddle.util - prevUtil)
            
def getGraph(file, graph, height):
	index = 0
	y = height-1
	for line in file:
		if line:
			x = 0
			lineSplit = line.split()
			for val in lineSplit:
				n = Node(val)
				n.setLoc(x,y)
				graph.addData(n, index)
				x += 1
			y -= 1
			index += 1


