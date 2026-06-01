import random

choices=["rock","paper","scissor"]
comp=random.choice(choices)
user=input("Enter rock,paper or scissor?").lower()
print("Computer chose:",comp)
if user==comp:
    print("Draw")
elif(user=="rock" and comp=="scissor")or (user=="paper" and comp=="rock") or (user=="scissor" and comp=="paper"):
    print("You win!!")
else:
    print("You Lose!!")