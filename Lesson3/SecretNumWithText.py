import random
# Predefined variables to not break Python
best_score = ""
last_attempt = ""
only = ""
rev_last_attempt = ""

# Open text and check whats useful in it
with open("score.txt", "r") as score_file:
    lines = score_file.readlines()
    n = len(lines) - 1
    if n > 0:
        for i in lines[0]:
            if i.isdigit():
                best_score += i
        for i in reversed(lines[n]):
            if i == ":":
                break
            elif i.isdigit():
                rev_last_attempt += i
    else:
        n = 0
        lines = [None]

# Get the stats from the last game if any available
try:
    for i in reversed(rev_last_attempt):
        last_attempt += i
    last_attempt = int(last_attempt)
    print(f"Game {n + 1}! GO!")
except:
    last_attempt = ""

try:
    best_score = int(best_score)
except:
    best_score = 1000

# Secret number generation
secret = random.randint(1, 30)
print(f"Its: {secret}")
attempts = 0

# Fun play time (put in system to charge per attempt later)
while True:
    try:
        print(f"Attempt number: {attempts + 1}!")
        guess = int(input("Guess the secret number between 1-30: "))
        attempts += 1

        if guess > 30 or guess < 1:
            print("Please stay within 1 and 30. ")
            continue
    except:
        print("Please write a valid NUMBER! ")
        attempts += 1
        print(f"This still counted as an attempt number {attempts}! ")

    else:
        if guess < secret:
            print("Try a biggah numbah!")

        elif guess > secret:
            print("Try a smallah numbah!")

# Win state (and eventual credit card charges (WIN STATE HUZZAH!))
        else:
            last_attempt = attempts
            if attempts < 5:
                only = "only "
            if best_score > attempts:
                best_score = attempts

            lines[0] = f"Best score: {best_score} tries. \n"
            lines.append(f"Game number {n + 1}: {last_attempt} tries. \n")
            with open("score.txt", "w") as score_file:
                for x in lines:
                    score_file.write(x)

            print(f"Congratulations,youve guessed the secret number {secret}! ")
            print(f"And you {only}needed {attempts} attempts! ")
            break
