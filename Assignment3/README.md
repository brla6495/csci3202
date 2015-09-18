#To Run the File:
> python Assignment3TestFile.py

Follow the prompts. Options for worlds are World1.txt and World2.txt. Options for heuristic are manhattan and euclidean

#Heuristic Explaination:
The manhattan heuristic deals with horizontal and vertical movement. This leads to inefficiencies, since the shorter path can be found by finding the diagonal hypotenuse. Thus, I decided to use the euclidean distance formula as my second heuristic. It is adapted from the pythagorean theorem, taking the square root of the sum of the squares of each side. 

	cost*(sqrt(math.pow(x-x1,2) + math.pow(y-y1,2)))

The euclidean heuristic was more efficient and produced a lower path cost than the manhattan, based on the given heuristic cost. 

	World1.txt~Manhattan:
	RESULTS:
	Total path cost: 156
	Total locations evaluated: 33
	Path locations: [(0, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 5), (3, 5),
	(4, 6), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7)]
	
	World1.txt~Euclidean:
	RESULTS:
	Total path cost: 130.0
	Total locations evaluated: 33
	Path locations: [(0, 0), (1, 0), (2, 0), (3, 1), (4, 2), (4, 3), (5, 4),
	(6, 4), (7, 5), (8, 5), (9, 6), (9, 7)]

	