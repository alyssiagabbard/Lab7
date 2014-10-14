#50 points
import random
rand = random.randint(0,50)
userInput1 = -1
while (userInput1 != rand):
    print "What do you think the number is?"
    userInput1 = int(raw_input())
    if userInput1 > rand:
        print "Your answer is too high!"
    elif userInput1 < rand:
        print "Your answer is too low!"
    elif userInput1 == rand:
        print "You go the right answer!"
        userInput1 = rand