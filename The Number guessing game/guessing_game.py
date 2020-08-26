import random
from time import sleep

print("\t\t\t******************** WELCOME TO GUESSING GAME ***********************")
guess = random.randint(1, 100)
print("\n\t\t\t\t\tYOU HAVE ONLY 10 CHANCES...!")
print("\n\t\t\t\t\t\t.......READY")
print("\n\t\t\t\t\t\t\t3")
sleep(1)
print("\n\t\t\t\t\t\t\t2")
sleep(1)
print("\n\t\t\t\t\t\t\t1")
sleep(1)
print("\n\t\t\t\t\t...............GO............")
chance = 10
while True:
    number = int(input("\n\t\t\t\t\tPlease Guess the Number : "))
    chance -= 1
    if chance == 0:
        print("\n\t\t\t!!! YOU LOSE !!! You have Left 0 Chances To guess!!!!!!!!!!!!!")
        sleep(1)
        print("\n\t\t\t\t\t\tGAME OVER")
        sleep(5)
        exit()
    elif number == guess:
        print("\n\t\t*************************** CONGRATULATIONS *************************")
        sleep(1)
        print("\n\t\tYOU ARE THE WINNER", number, "is Right Guess and you took only", 10-chance, "guess")
        sleep(5)
        print("\n\t\t\t\t\t\tGOODBYE")
        sleep(5)
        exit()
    elif number > guess:
        print("\n\t\t\t\t\t!!!!!!SORRY WRONG GUESS!!!!!!")
        sleep(1)
        print("\n\t\t\tIt would be Smaller Number And you Left only", chance, "Chances!!!!")
    elif number < guess:
        print("\n\t\t\t\t\t!!!!!!SORRY WRONG GUESS!!!!!!")
        sleep(1)
        print("\n\t\t\tIt would be Bigger Number And you Left only", chance, "Chances!!!!")

