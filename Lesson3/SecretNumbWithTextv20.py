# Imports and whatnot
import random
from os import path
import csv
from datetime import datetime

# Variables needing declaration
name = ""
age = ""
gender = ""
prefix = ""
command = ""
player_description = []


# Update the date function
def update_date():
    d = datetime.now()
    date_in_fun = d.strftime("%d.%m.%Y")
    return date_in_fun


# Find files or create them
if not path.exists("playdata.csv"):
    with open("playdata.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["name", "gender", "age", "date", "game #", "score"])


# Player description function
def player_description_update():
    global name
    name = input("Enter your name: ")
    if name == "":
        name = "Guest"

    global gender
    global prefix
    gender = input("Gender m/f: ").lower()
    if not (gender == "m" or gender == "f"):
        gender = "Nonstandard"
    if gender == "m":
        prefix = "Mr."

    elif gender == "f":
        prefix = "Ms."
    else:
        prefix = ""

    global age
    age = ""
    age_input = input("Enter your age: ")
    for i in age_input:
        if i.isdigit():
            age += i
    if age == "":
        age = "1"
    print(f"Hello {prefix}{name}, {age} years old.")


# Read and save to list csv for past games data
#  Get past data for game number and best score FUNCTION


def current_game_numb_fun():
    with open("playdata.csv", "r") as playdata:
        data = csv.reader(playdata)
        play_data = list(data)
    last_game_data = play_data[-1]
    try:
        x = int(last_game_data[4]) + 1
        return x
    except ValueError:
        x = 1
        return x
    

player_description_update()


# Functions and stuffs
def print_scoreboard():
    with open("playdata.csv", "r") as play_data2:
        reader = csv.reader(play_data2)
        for row in reader:
            print(row)


def play_game_fun():
    # Update date
    date = update_date()
    # Best score placeholder
    if path.exists("score.txt"):
        with open("score.txt", "r") as score_txt:
            try:
                best_score = int(score_txt.read())
            except ValueError:
                with open("score.txt", "w+") as score_txt2:
                    score_txt2.write("100")
                    score_txt2.seek(0)
                    best_score = int(score_txt2.read())
    else:
        with open("score.txt", "w+") as score_txt:
            score_txt.write("100")
            score_txt.seek(0)
            best_score = int(score_txt.read())
    # Current game
    current_game_numb = current_game_numb_fun()

    print(f"Welcome to Game number {current_game_numb} on {date}.")
    print(f"You must beat a score of {best_score}! Good luck!")
    secret = random.randint(1, 30)
    print(f"Secret number is: {secret}")
    attempt = 0
    print()
    while True:
        try:
            print(f"Attempt number: {attempt + 1}")
            guess = int(input("Guess a number between 1-30: "))
            attempt += 1

            if guess < 1 or guess > 30:
                print("Within 1 and 30, stay between ONE and THIRTY!")
                print("")
                continue
        except ValueError:
            print("Try to punch in an actual NUMBER!!!!!")
            print(f"This still counted an attempt!")
            attempt += 1
            print("")
        else:
            if guess < secret:
                if secret - guess < 5:
                    print("Just a bit more.")
                    print("")
                else:
                    print("Try a bigger number.")
                    print("")

            elif guess > secret:
                if guess - secret < 5:
                    print("Just a touch less.")
                    print("")
                else:
                    print("Try a smaller number.")
                    print("")
            # Game won
            elif guess == secret:
                if best_score > attempt:
                    with open("score.txt", "w") as score_txt1:
                        score_txt1.write(f"{attempt}")
                    print(f"Congratulations {prefix}{name}, you have the new HIGHSCORE with only {attempt} attempts!")

                elif attempt - best_score < 5:
                    print(f"Well done {prefix}{name}, it took you {attempt} attempts but you did make it. Huzzah!")

                else:
                    print(f"Meh {name}, took you {attempt} attempts... quite the overachiever...")
                break
    # Now to punch in the data
    with open("playdata.csv", "a") as csvdata:
        writer1 = csv.writer(csvdata)
        writer1.writerow([f"{name}", f"{gender}", f"{age}", f"{date}", f"{current_game_numb}", f"{attempt}"])

    # Aftermath choices
    print(f"Game number {current_game_numb} finished. ")
    print("")
    # End of game function


play_game_fun()
while True:
    commands = input("re = restart, sb = scoreboard, n = new player, q = quit: ")

    if commands == "q":
        break
    elif commands == "sb":
        print("")
        print_scoreboard()
        print("")
    elif commands == "re":
        print("")
        play_game_fun()
    elif commands == "n":
        print("")
        player_description_update()
        play_game_fun()
