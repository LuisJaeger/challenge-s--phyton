import random
victories = 0
defeats = 0
ties = 0
while True:

    desition = input("Choose: rock, paper or scissors.")
    if desition == "exit":
        break
    AI_desition = random.choice(["rock", "paper", "scissors"])
    print(AI_desition)
    if desition == AI_desition:
        print("Tie")
        ties = ties + 1
    elif desition == "rock" and AI_desition == "paper":
        print("You have lost")
        defeats = defeats + 1
    elif desition == "rock" and AI_desition == "scissors":
        print("You have won")
        victories = victories + 1
    elif desition == "paper" and AI_desition == "rock":
        print("You have won")
        victories = victories + 1
    elif desition == "paper" and AI_desition == "scissors":
        print("You have lost")
        defeats = defeats + 1
    elif desition == "scissors" and AI_desition == "paper":
        print("You have won")
        victories = victories + 1
    elif desition == "scissors" and AI_desition == "rock":
        print("You have lost")
        defeats = defeats + 1
print(f"You have won {victories} time(s), you have lost {defeats} time(s) and you have tied {ties} time(s)")
