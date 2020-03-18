import random

best_score = ""
last_attempt = ""

# Text document stuff

with open("score.txt", "r") as score_file:
    lines = score_file.readlines()
    n = len(lines) - 1
    if n > 0:
        for i in lines[0]:
            if i.isdigit():
                best_score += i
        for i in lines[n]:
            if i.isdigit():
                last_attempt += i

try:
    last_attempt = int(last_attempt)
except:
    last_attempt = ""

try:
    best_score = int(best_score)
except:
    best_score = 1000

secret = random.randint(1, 30)
print(secret)
attempts = 0

while True:
    try:
        guess = int(input("Guess the secret number between 1-30: "))
        attempts += 1
        print(attempts)

        if guess > 30 or guess < 1:
            print("Please stay within 1 and 30. ")
            continue
    except:
        print("Please write a NUMBER between 1-30: ")
        attempts += 1
        print(f"This still counted as an attempt number {attempts}! ")

    else:
        if guess < secret:
            print("Try a biggah numbah!")

        elif guess > secret:
            print("Try a smallah numbah!")

        else:
            last_attempt = attempts
            if best_score > attempts:
                best_score = attempts
            with open("score.txt", "w") as score_file:
                score_file.write(f"Best score: {best_score}\n")
                score_file.write(f"Last score: {last_attempt}\n")

            print(f"Congratulations,youve guessed the secret number {secret}! ")
            print(f"And you only needed {attempts} attempts! ")
            break
