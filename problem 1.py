import random
number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100:"))
while guess != number:
   
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")

    guess = int(input("Guess a number between 1 and 100:"))

if guess == number:
    print("Correct")