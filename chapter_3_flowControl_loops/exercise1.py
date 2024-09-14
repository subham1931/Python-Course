#make a variable like winning number and ssign any number to it 
#Ask user to guess a number.
#is user gusses is correct then print "YOU WIN !!!!"
#ifuser did not gussed correctlt then:
        #if user gussed lower than actual number then print "too low"
        #if user gussed higer than actual number then print "too high"
        
#solution
import random
wining_number = random.randint(1,9)
gussed_number = int(input("Gusse a number between 1 to 9"))

if gussed_number == wining_number :
    print("YOU WIN!!!")
elif gussed_number > wining_number:
    print("Too High")
elif gussed_number < wining_number:
    print("Too Low")
else:
    print("PLease enter a number between 1 tp 9")