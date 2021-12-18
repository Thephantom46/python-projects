import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_pick = input("Please select rock/paper/scissors or type q to quit or press i to view scores: ").lower()
    if user_pick == "q":
        print("Goodbye")
        quit()

    elif user_pick == "i":
        print("You won", user_wins, "times")
        print("The computer won", computer_wins, "times")
        continue

    elif user_pick not in options:
        print("Invalid input")
        continue

    r = random.randint(0,2)
    # rock:0, paper:1, scissors:2
    computer_pick = options[r]
    print("Computer's choice is ", computer_pick)

    if user_pick == "rock" and computer_pick == "scissors":
        print("YOU WIN")
        user_wins += 1

    elif user_pick == "paper" and computer_pick == "rock":
        print("YOU WIN")
        user_wins += 1

    elif user_pick == "scissors" and computer_pick == "paper":
        print("YOU WIN")
        user_wins += 1

    elif user_pick == "rock" and computer_pick == "rock":
        print("DRAW")

    elif user_pick == "paper" and computer_pick == "paper":
        print("DRAW")

    elif user_pick == "scissors" and computer_pick == "scissors":
        print("DRAW")

    else:
        print("YOU LOST")
        computer_wins += 1

print("Goodbye")    
