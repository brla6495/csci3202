from Assignment3 import*

fileName = raw_input("Name of World File: ")
heuristic = raw_input("Name of Heuristic ('manhattan or euclidean'): ")
file = open(fileName, 'r')
g = Graph (10, 8)
makeGraph(file, g, 8)
settings = AStarSearch(g.getNode(0,0), g.getNode(9,7), g, heuristic)
settings.beginSearch()