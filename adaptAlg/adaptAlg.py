"""
adaptAlg.py
---------
Owen Chen
---------
Adaptive Algorithm module for learning analytics. Machine learning concepts to maximize learning retention
efficency

Algorithm:
1. Split into smallest possible items. 
2. E-Factor of 2.5 initialized to all variables. 
3. OF Matrix and E-Factor categories. Algorithm:
        OF(1,EF) = 4
        for n > 1 OF(n, EF) := EF

        Where OF(n, EF) - optimal factor for n-th repitition  and EF 
4. OF Matrix to determine inter-repetition intervals. 
        I(n, EF) = OF( n, EF) * I(n-1, EF)
        ... Code Online
5. Assess quality of repetition responses in 0-5 scale
6. Modify E-factor According to formula
7. After each rep, modify relevant entry of OF matrix. 
8. if quality respobse is lower than 3 start repetition for the item from the beginning with no E-factor change
9. Repeat all items under four in quality assement.

"""

import json

class Game():
	user = None

	def __init__(self, name):
		self.user = User(name)

	def begin(self):
		print("Spaced Repitition Algorithm \n" + 
			"Scale of 1 - 5, rate your comfort level\n" +
			"(0) - No clue\n" + 
			"(1) - Slight recognition\n" +
			"(2) - Almost had it! \n" +
			"(3) - Slight recognition\n" +
			"(4) - Got it, but not perfect \n" +
			"(5) - Mastery \n")

		curUser = self.getUser()
		repAlgorithm(curUser)


	#Get User Object____
	def getUser(self):
		print("Name of user is ")
		print(self.user.getName())
		return self.user
		
	#Repition Algorithm for User____
	def repAlgorithm(self, user):
		print("Starting algorithm")





		return 0

	def updateEF():
		return 0


		



class User:

	name = None
	cardFile = None
	#The start date of the current instantiation of game
	day = 0
	EFFactorData = {}

	



	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

	#Import a file. 
	def uploadCardFile(self):


	def getCardCount(self):
		return 0

	def addCard(self):
		return 0







game = Game("Owen")
print("Starting new game object name game with User Owen")



