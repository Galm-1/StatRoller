# Ecrit ton programme ici ;-)
import random
statnames = ["Strength","Agility","Intelligence","Charisma","Wisdom"]
statlines = [0,0,0,0,0]
statranking = ["Great","Good","Average","Poor","Shameful"]
def rolling(i): #Main Rolling + Attribute
    stat = random.randint(1,10)
    statlines[i] = stat
def evaluation(i): #Evaluation
    if statlines[i] > 8:
        print("Your " + statnames[i] + " is " + str(statlines[i]) + ", it is : " + statranking[0])
    elif statlines[i] > 6:
        print("Your " + statnames[i] + " is " + str(statlines[i]) + ", it is : " + statranking[1])
    elif statlines[i] > 4:
        print("Your " + statnames[i] + " is " + str(statlines[i]) + ", it is : " + statranking[2])
    elif statlines[i] > 2:
        print("Your " + statnames[i] + " is " + str(statlines[i]) + ", it is : " + statranking[3])
    elif statlines[i] > 0:
        print("Your " + statnames[i] + " is " + str(statlines[i]) + ", it is : " + statranking[4])
while True :
    print("Hello Adventurer ! please roll your stats")
    print("Press 1 to roll, Press 5 to get your result")
    playerMove = int(input())
    if playerMove == 1:
        for i in range (len(statnames)):
            rolling(i)
            print("You are rolling for " + statnames[i] + ", You have " + str(4-i) + " stats left to roll")
    elif playerMove == 5:
        for i in range (len(statnames)):
            print("Your " + statnames[i] + " is " + str(statlines[i]))
        break
    else :
        print("Please insert 1 or 5")
print("The great sorceress Ela will evaluate your stat")
print("Please repeat after her the sacred words")
print("Ela : KEBAB !")
while True:
    playerMove = input()
    if playerMove == "KEBAB !":
        print("Great ! Prepare for Evaluation !")
        for i in range (len(statnames)):
            evaluation(i)
        break
    else :
        print("Fool ! Say the sacred words !")
print("Now you may go !")
