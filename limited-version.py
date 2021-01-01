#You have to guess the random value between 1 to 10 in 3 chances
import definitions as f

f.welcome(3,1,10);
r=f.randomize(1,10);

i=1
while i<=3:
	g=f.guess();

	if (r==g):
		f.end(); 
		break
	else:
		print("Wrong!")
		print(3-i,"chances left")
		if i==3:
			print("You lose. Better luck next time!")
			f.sleepforzsec(3);
	i+=1