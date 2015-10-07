class Node:
	def __init__(self, val):
		self.val = int(val)
		self.x = 0
		self.y = 0
		self.parent = None
		if self.val is 0:
			self.reward = 0
			self.util = 0
		elif self.val is 1:
			self.reward = -1
			self.util = -1
		elif self.val is 2:
			self.reward = None
			self.util = None
		elif self.val is 3:
			self.reward = -2
			self.util = -2
		elif self.val is 4:
			self.reward = 1
			self.util = 1
		elif self.val is 50:
			self.reward = 50
			self.util = 50

	def setLoc(self, x ,y):
		self.x = x
		self.y = y
