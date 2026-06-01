import random
number=random.randint(1000,10000)
guess=0
attempts=0
print("Guess a number between 1000 and 10000")
while guess !=number:
    try:
        guess=int(input("Enter your guess: "))
        attempts+=1
        if guess<1000 or guess>10000:
            print("Enter number between 1000 to 10000")
        elif guess<number:
            print("Too low")
        elif guess>number:
            print("Too High")
        else:
            print("Correct Number")
            print(f"Number of attempts: {attempts}")
    except ValueError:
        print("Invalid Input. Please enter a valid number.")