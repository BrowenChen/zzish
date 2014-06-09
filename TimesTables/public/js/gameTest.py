"""
Answer Checking
Takes in xCoor, yCoor, usrInput all in the current cursor


"""




def ansChecker(xCoor, yCoor, usrInput):

	answers = {}
	tmp = 0

	for y in range(0, 10):
		for x in range(0, 10):
			answers[x, y] = x*y

# Check usrInput with the answer grid

	print(answers[xCoor, yCoor])
	if (answers[xCoor, yCoor] == usrInput):
		print("Yay you got it right")
		return True
	else:
		print("no you got it wrong")
		return False
	ans = str(answers[xCoor, yCoor])
	print("Answer is " + ans)



"""
Finish function checkSolutions
Returns a score out of the dimensions
Loop through all answers and checks user input. 

"""


print("Testing with 5, 5, 25")
ansChecker(5, 5, 25)