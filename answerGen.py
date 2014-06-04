"""
answerGen.py
---------
Random answer generator for times tables. (Just to memorize simple times tables)
Goal is to create 'similar' wrong answers. 
Future implementation would be to generalize this feature for other tasks

"""

import random
import math 

def alg(arg1, arg2, operation):
	"""
	Input arg1 and arg2 are integer numbers

	Operation is a string of a function. "+", "-", "/", "*". We want it to be a function to take in the arguments
	"""


	#List of answers
	ans = []

	#set trueAnswer to be operation(arg1, arg2)
	#check to see what kind of operation it is and change it to that function 


	trueAns = operation(arg1, arg2)
	ans.append(trueAns)

	#Generate unique possible answers that are not the true answer. (Assuming only 4 answers)
	#Loop until there are four answers
	while len(ans) < 4:

		tempArg2 = operation(arg1,random.randrange(arg2 - 3, arg2 + 3))
		#Generate tempArg2's that are similar to arg2 to use to generate a new number

		#Check if generated sample is equal to trueAnswer
		if (tempArg2 != arg2):
			ans.append(tempArg2)

	return ans

