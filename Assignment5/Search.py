class Search:
    
	def __init__(self, start, goal, graph):
		self.path = []
		self.utils = []
		self.start = start
		self.goal = goal
		self.graph = graph
        
	def getPath(self):
		self.graph.setUtility()
		self.path.append(self.start)
		self.utils.append(self.start.util)
		current = self.start
		while current is not self.goal:
			nodeNorth = self.graph.getNode(current.x, current.y+1)
			nodeEast = self.graph.getNode(current.x+1, current.y)
			nodeWest = self.graph.getNode(current.x-1, current.y)
			nodeSouth = self.graph.getNode(current.x, current.y-1)
			utilityNorth = None
			utilityEast = None
			utilityWest = None
			utilitySouth = None
			if nodeNorth == None:
				utilityNorth = float('-inf')
			else:
				utilityNorth = nodeNorth.util
			if nodeSouth == None:
				utilitySouth = float('-inf')
			else:
				utilitySouth = nodeSouth.util
			if nodeWest == None:
				utilityWest = float('-inf')
			else:
				utilityWest = nodeWest.util
			if nodeEast == None:
				utilityEast = float('-inf')
			else:
				utilityEast = nodeEast.util
			if utilityNorth == max(utilityNorth, utilitySouth, utilityWest, utilityEast):
				current = nodeNorth
			elif utilityEast == max(utilityNorth, utilitySouth, utilityWest, utilityEast):
				current = nodeEast
			elif utilityWest == max(utilityNorth, utilitySouth, utilityWest, utilityEast):
				current = nodeWest
			elif utilitySouth == max(utilityNorth, utilitySouth, utilityWest, utilityEast):
				current = nodeSouth

			self.path.append(current)
			self.utils.append(current.util)

	def printSearch(self):
		self.getPath()
		print " Done."
		print ""
		print "-----------------------------------------"                      
		print "Path and Utility Values: "
		print ""
		print "Format: [(x,y), utility]"
		print ""                        
		for item1, item2 in zip(self.path, self.utils):
			print "[(%d,%d)" %(item1.x,item1.y) + ", %.2f]" %item2,
		print ""            
		print "\n-----------------------------------------"