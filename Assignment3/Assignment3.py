import math

class Node:

	def __init__(self, val):
		self.val = int(val) # node value
		self.parent = None # No parent by default
		self.x = 0 # default x coordinate on grid
		self.y = 0  # default y coordinate on grid
		self.g = 0 # cost from start to current node
		self.h = 0 # heuristic cost
		self.cost = 0 # total cost

	def setLocation(self, x, y): # sets coordinates for node on grid
		self.x = x
		self.y = y
		
class Graph:

	def __init__(self, width, height):
		self.width = width # sets x length of graph
		self.height = height # sets y length of graph
		self.data = [] # empty list
		for i in range(0, height): # fills list up to height 
			self.data.append([])            
    
	def getNode(self, x, y): # check every node in grid, return node with same x and y coords
		for nodes in self.data: 
			for node in nodes:
				if node.x == x and node.y == y:
					return node

	def surroundingNodes(self, node): 
		adjacent=[]
		x = node.x
		y = node.y
		up = self.getNode(x,y+1) # node up
		down = self.getNode(x,y-1) # node down
		left = self.getNode(x-1, y) # node left
		right = self.getNode(x+1,y) # node right
		diagonalUL = self.getNode(x-1,y+1) # node diagonally up->left
		diagonalUR = self.getNode(x+1,y+1) # node diagonally up->right
		diagonalDL = self.getNode(x-1,y-1) # node diagonally down->left
		diagonalDR = self.getNode(x+1,y-1) # node diagonally down->right
 		extraCost = 10       
        
		for currentNode in [diagonalDL, down, diagonalDR, right, diagonalUR, up, diagonalUL, left]: #check surrounding nodes, apply cost
			if currentNode is not None and currentNode.val is not 2:
				totalCost = 0
				if currentNode in [diagonalDL, diagonalDR, diagonalUL, diagonalUR]:
					totalCost = 14
				else:
					totalCost = 10
				if currentNode.val is 1:
					totalCost = totalCost + extraCost
				adjacent.append([currentNode,totalCost])
		return adjacent

def makeGraph(file, g, height): #parse input file and make a graph out of it
	index = 0 
	y = height-1
	for line in file:
		x = 0
		gridSpaceIDs = str.split(line)
		for values in gridSpaceIDs:
			newNode = Node(values)
			newNode.setLocation(x,y)
			g.data[index].append(newNode)
			x = x+1
		y = y-1
		index = index + 1
            
class AStarSearch:
	
	def __init__(self, start, end, g, heuristicChoice): # default values
		self.path = []
		self.start = start
		self.end = end
		self.g = g
		self.heuristicFunction = heuristicChoice        
		self.locationsEvaluated = 1 

	def heuristic(self, node): # Choice of heuristic
		if self.heuristicFunction == "manhattan":
			return self.manhattan(node)
		elif self.heuristicFunction == "euclidean":
			return self.euclidean(node)

	def manhattan(self, node): # manhattan heuristic based on horizonal and vertical movements
		return (abs(self.end.x - node.x) + abs(self.end.y - node.y))*10
        
	def euclidean(self, node): # euclidian heuristic based on the pythagorean theorem
		return math.sqrt(math.pow((node.x - self.end.x),2) + math.pow((node.y - self.end.y),2))*14        
		
	def update(self, node, parent, move_cost): # update values for the node
		node.parent = parent
		node.g = move_cost + parent.g
		node.h = self.heuristic(node)
		node.cost = node.g + node.h
	
	def beginSearch(self): # find nodes, add their surrounding nodes, and look for lowest cost path
		open = [self.start]
		closedList = []
		while len(open) > 0:
			node = min(open, key=lambda n:n.cost)
			open.remove(node)
			if node is not self.end:
				closedList.append(node)
				for (adjacent, moveCost) in self.g.surroundingNodes(node):
					if adjacent not in closedList:
						if adjacent in open:
							if adjacent.g > (node.g + moveCost):
								self.update(adjacent, node, moveCost)
						else:
							self.update(adjacent, node, moveCost)
							open.append(adjacent)
							self.locationsEvaluated = self.locationsEvaluated + 1
			else:
				self.printResults()	
				break
		
	def printResults(self): # print cost, locations, and path
		path = self.getPath(self.end)
		print ""
		print "RESULTS:"
		print ""
		print ("Total path cost: " + str(self.end.cost))
		print ""                
		print ("Total locations evaluated: " + str(self.locationsEvaluated))
		print ""
		print ("Path locations: " + str(path))
		print ""
		
	def getPath(self, node):
		path = []
		index = node
		while index:
			path.append((index.x, index.y))
			index = index.parent
		return path[::-1] 	

               