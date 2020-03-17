
import  random

# Variables
secret = random.randint(1, 10)

won = "Congrats!!!! "
lost = "Loser! "

# Fun part

while True:
    guess = int(input("Guess the secret number: "))
    if guess == secret:
        print(won)
        break
    elif guess == secret - 1:
        print("Warmer...warmerr... ")
    elif guess == secret + 1:
        print("So freakin CLOSE! ")
    elif guess < secret:
        print(lost + "Try a bigger number. ")
    elif guess > secret:
        print(lost + "Try a smaller number.")
