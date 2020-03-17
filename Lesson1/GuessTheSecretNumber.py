# Variables
secret = 7

won = "Congrats!!!!"
lost = "Loser!"

# Fun part

guess = int(input("Guess the secret number: "))

if guess == secret:
    print(won)
else:
    print(lost)
