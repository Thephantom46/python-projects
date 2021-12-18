print("Welcome to Quiz")

choice = input("Do you want to play? ")

if choice.lower() != "yes":
    print("goodbye")
    quit()

print("Let's play!")
score = 0

answer = input("What is the capital city of iceland?")
if answer.lower() == "reykjavic":
    print("Correct answer")
    score +=1
else:
    print(answer)
    print("Incorrect")

answer = input("What is the capital of Poland?")
if answer.lower() == "warsaw":
    print("Correct answer")
    score += 1
else:
    print("Incorrect")

answer = input("what is the capital of Mongolia?")
if answer.lower() == "ulan bator":
    print("Correct answer")
    score += 1
else:
    print("Incorrect")

answer = input("What is the capital of Hungary?")
if answer.lower() == "budapest":
    print("Correct answer")
    score += 1
else:
    print("Incorrect")

print("Your final score is " + str(score))






