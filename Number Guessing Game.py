# Number Guessing Game
#Number = 1,2,3,4,5.....100
print("Guess the Number between 1 to 100")

attempts = 0
import random
secret_num = random.randint(1,100)

while True:
    print("=====Game=====")
    print("let play the Game")
    print("==Start==")

    Guess_Number = int(input("\n Guess the Number: "))
    attempts= attempts+1

    if(Guess_Number>secret_num):
        print("Too High")
        
        print("Try Again")

    if(Guess_Number<secret_num):
        print("Too Low")
          
        print("Try Again")

    if(Guess_Number==secret_num):
        print("You Guessed It")
        
        print("You Guessed It in", attempts),print("Attempts")

            



