"""
Multiple choice table in an app. 
2x12, each array input numbers


Answer:
	 1 2 3 4    Ans.
	 _ _ _ _
1	|_|_|_|_|	1 2 3 4
2	|_|_|_|_|   2 4 6 8
3	|_|_|_|_|   3 6 9 12
4	|_|_|_|_|   4 8 12 16
5	|_|_|_|_|   5 10 15 20
6	|_|_|_|_|   6 12 18 24


User

	 1 2 3 4    
	 _ _ _ _
1	|_|_|_|_|	
2	|_|_|_|_|   
3	|_|_|_|_|   
4	|_|_|_|_|   
5	|_|_|_|_|   
6	|_|_|_|_|   


Marked Grid - Checks if current cell is marked or not

	 1 2 3 4    
	 _ _ _ _
1	|_|_|_|_|	
2	|_|_|_|_|   
3	|_|_|_|_|   
4	|_|_|_|_|   
5	|_|_|_|_|   
6	|_|_|_|_|   


cellCurCursor = (x,y) of where the current cursor is on the cell. 
	Cursor has options to move(LRUP) or click()

	click() action 
		Check if current cell has been previously selected
		If MarkedGrid (cellCurCursor(x,y) ) == false:
		(Continue with algorithm)
			prompt user for input 
			Listen for user input
			Check if input is equal to the answer grid
			Mark right or wrong in that current grid
			Mark in MarkedGrid that cellCurCursor(x, y) is marked
			Maybe draw in a picture on that cell grid for the User grid to show that it is marked

		If the markedGrid of (cellCurCursor(x,y)) is == true, we cannot use that cell 

	move(direction) action
		4 case switches
		Left - do those actions
		Right -
		Up -
		Down - 


	
"""

#Create a grid 2x2

#Each cell is clickable
#Initialize all the cells to 0

#If clicked, prompt user for an input
	#Store user input into an int variable
	#Check that variable to answer Grid
	# If correct, say correct
		# else say wrong

