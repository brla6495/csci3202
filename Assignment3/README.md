#To Run the File:
> python Assignment3TestFile.py

Follow the prompts. Options for worlds are World1.txt and World2.txt. Options for heuristic are manhattan and euclidean

#Heuristic Explaination:
The manhattan heuristic deals with horizontal and vertical movement. This leads to inefficiencies, since the shorter path can be found by finding the diagonal hypotenuse. Thus, I decided to use the euclidean distance formula as my second heuristic. It is adapted from the pythagorean theorem, taking the square root of the sum of the squares of each side. 

	sqrt(math.pow(x-x1,2) + math.pow(y-y1,2))
