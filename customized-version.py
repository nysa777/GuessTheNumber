#User will input the range(lower and upper bounds) and also the number of chances they want to guess the number
import definitions as f

u=int(input("Enter Lower bound"))
l=int(input("Enter Upper bound"))
n=int(input("How many chances would you prefer?"))

f.welcome(n,u,l);
r=f.randomize(u,l);

i=1
while i<=n:
	g=f.guess();

	if (g==r):
		f.end(); 
		break
	elif g>r:
		print("Wrong! It is smaller than that.")
		print(n-i,"chances left")
		if i==n:
			print("You lose. Better luck next time!")
			f.sleepforzsec(3);
	elif g<r:
		print("Wrong! It is greater than that.")
		print(n-i,"chances left")
		if i==n:
			print("You lose. Better luck next time!")
			f.sleepforzsec(3);
	i+=1