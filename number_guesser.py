import random

top = input("Type a number: ")

if top.isdigit():
    top = int(top)

    if top <= 0:
        print("please type a number larger than 0 next time")
        quit()
else:
    print("please print a number next time")
    quit()

r = random.randint(0, top)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == r:
        print("YOU GOT IT!!")
        break
    elif user_guess > r:
        print("Your guess was higher")
    else:
        print("Your guess was lower")

print("You got it", guesses, "guesses")
    