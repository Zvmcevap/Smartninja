# Imports and whatnot
import random
from os import path
import csv
from datetime import datetime

# Variables needing declaration
age = ""
prefix = ""
date = datetime.now()
date = date.strftime("%d.%m.%Y")

# Secret number generation
secret = random.randint(1, 30)
print(f"The secret numb is: {secret}")

# Find files or create them
if not path.exists("playdata.csv"):
    with open("playdata.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["name", "gender", "age", "date", "game #", "score"])

# Player description
name = input("Enter your name: ")
if name == "":
    name = "Guest"

gender = input("Gender m/f: ").lower()
if not (gender == "m" or gender == "f"):
    gender = "Nonstandard"
if gender == "m":
    prefix = "Mr."
elif gender == "f":
    prefix = "Ms."

age_input = input("Enter your age: ")
for i in age_input:
    if i.isdigit():
        age += i
if age == "":
    age = 1
age = int(age)

# Read and save to list csv for past games data
with open("playdata.csv", "r") as playdata:
    data = csv.reader(playdata)
    play_data = list(data)

# Get past data for game number and best score
last_game_data = play_data[-1]
try:
    current_game_numb = int(last_game_data[4]) + 1
except:
    current_game_numb = 1

# Best score placeholder
if path.exists("score.txt"):
    with open("score.txt", "r") as score_txt:
        try:
            best_score = int(score_txt.read())
        except:
            pass
else:
    with open("score.txt", "w+") as score_txt:
        score_txt.write("100")
        score_txt.seek(0)
        best_score = int(score_txt.read())

print(f"Hello {prefix}{name}, {age} years old, today on {date}.")
print(f"Welcome to Game number {current_game_numb}, you must beat a score of {best_score}! Good luck! ")

# Start of play
attempt = 0
while True:
    try:
        print(f"Attempt number: {attempt + 1}")
        guess = int(input("Guess a number between 1-30: "))
        attempt += 1

        if guess < 1 or guess > 30:
            print("Within 1 and 30, stay between ONE and THIRTY!")
            continue
    except:
        print("Try to punch in an actual NUMBER!!!!!")
        print(f"This still counted an attempt!")
        attempt += 1
    else:
        if guess < secret:
            if secret - guess < 5:
                print("Just a bit more.")
            else:
                print("Try a bigger number.")

        elif guess > secret:
            if guess - secret < 5:
                print("Just a touch less.")
            else:
                print("Try a smaller number.")
        # Game won
        elif guess == secret:
            if best_score > attempt:
                with open("score.txt", "w") as score_txt:
                    score_txt.write(f"{attempt}")
                print(f"Congratulations {prefix}{name}, you have the new HIGHSCORE with only {attempt} attempts!")

            elif attempt - best_score < 5:
                print(f"Well done {prefix}{name}, it took you {attempt} attempts but you did make it. Huzzah!")

            else:
                print(f"Meh {name}, took you {attempt} attempts... quite the overachiever...")
            break
# Now to punch in the data
with open("playdata.csv", "a") as csvdata:
    writer = csv.writer(csvdata)
    writer.writerow([f"{name}", f"{gender}", f"{age}", f"{date}", f"{current_game_numb}", f"{attempt}"])
