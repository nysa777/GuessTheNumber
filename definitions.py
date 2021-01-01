import random 
import time

def sleepforzsec(z):
	time.sleep(z)

def welcome(a,b,c):
	print("Welcome!")
	print("You have", a ,"chances to guess the Number beetween ", b, " and ", c )
	
def randomize(x,y):	
	randomVal = random.randint(x,y)
	#print(randomVal)
	return randomVal

def guess():
	guessVal = int(input("Enter your Guess value"))
	return guessVal

def end():
	print("Correct!")
	print("You win!")
	sleepforzsec(3);

def ask():
	print("Do want to play the 1. customized-option GuessTheNumber or 2. limited GuessTheNumber")
	return int(input("Type 1 or 2 :"))

def choosing(v):
	if v==1:
		print("Starting Customized-option GuessTheNumber")
		exec(open('customized-version.py').read())
		exit()
	elif v==2:
		print("Starting Limited GuessTheNumber")
		exec(open('limited-version.py').read())
		exit()
	else:
		print("Wrong Value Entered. Choose Again!")
		q=ask();
		choosing(q);
