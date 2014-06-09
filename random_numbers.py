import random

class MyClass:

	staticList = []
	staticNum = []
	transList = []
m = MyClass()

inputList = input('Enter a list: ')
print(inputList)


def randomNum():

	list = []


	for i in range (100):
		list.append([str(random.randrange(0, 10)) + str(random.randrange(0, 10))])
	m.staticNum = list
	print(list)


def printOut():
	print("hello world")

def randomWord():
	words = open('/Users/owenchen/Desktop/WordNet-3.0/dict/noun.exc').read().splitlines()
	newList = []
	# print(words)
	# print(random.randrange(0, len(words)))
	# print(words[random.randrange(0, len(words))])
	for i in range(30):
		newList.append(words[random.randrange(0, len(words))])

	print(newList)
	m.staticList = newList

def translateNumber(newList):
	wordList = []
	translatedList = []
	translation = {1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D', 5 : 'E',
				   6 : 'S', 7 : 'G', 8 : 'H', 9 : 'N', 0 : 'O'}


	for item in newList:
		translatedList.append([item[0], (translation[int(item[0][0][0])] + translation[int(item[0][1][0])])])
		
	m.transList = translatedList

randomNum()
translateNumber(m.staticNum)
print(" ")
print(m.transList)