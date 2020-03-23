# Imports and whatnot
import random
from os import path
import csv
from datetime import datetime

# Variables needing declaration
# name = ""
# age = ""
# gender = ""
# prefix = ""
command = ""
player_info = {"name": "", "gender": "", "prefix": "", "age": 1, "date": [], "play#": [], "score": []}


# Update the date function
def update_date():
    d = datetime.now()
    date_in_fun = d.strftime("%d.%m.%Y %H:%M")
    return date_in_fun


# Find files or create them
if not path.exists("playdata.csv"):
    with open("playdata.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["name", "gender", "age", "date", "game #", "score"])


# Player description function
def player_description_update(x):
    name = input("Enter your name: ")
    if name == "":
        name = "Guest"

    gender = input("Gender m/f: ").lower()
    if not (gender == "m" or gender == "f"):
        gender = "x"
    if gender == "m" or "male":
        prefix = "Mr."

    elif gender == "f" or "female":
        prefix = "Ms."
    else:
        prefix = ""

    age = ""
    age_input = input("Enter your age: ")
    for i in age_input:
        if i.isdigit():
            age += i
    if age == "":
        age = "1"
    print(f"Hello {prefix}{name}, {age} years old.")
    x.update({"name": name, "gender": gender, "age": age, "prefix": prefix})


# Read and save to list csv for past games data
#  Get past data for game number and best score FUNCTION
def clear_scoreboard():
    with open("playdata.csv", "w", newline="") as csvfile2:
        writer2 = csv.writer(csvfile2)
        writer2.writerow(["name", "gender", "age", "date", "game #", "score"])


def current_game_numb_fun():
    with open("playdata.csv", "r") as playdata:
        data = csv.reader(playdata)
        play_data = list(data)
        if len(play_data) > 1:
            last_game_data = play_data[-1]
            x = int(last_game_data[4]) + 1
            return x
        else:
            x = 1
            return x


def last_player():
    with open("playdata.csv", "r") as playdata:
        data = csv.DictReader(playdata)
        data_list = []
        for row in data:
            data_list.append(row)
        if len(data_list) > 0:
            player = dict(data_list[-1])
            if player["gender"] == "m":
                player["prefix"] = "Mr."
            elif player["gender"] == "f":
                player["prefix"] = "Ms."
            else:
                player["prefix"] = ""

            print(f'Logged in as {player["name"]}, last game was on {player["date"]} with a score of {player["score"]}')
            print(f"")
            return player
        else:
            print("No player recorder, please log in.")
            print("")
            player = {"name": "", "gender": "", "prefix": "", "age": 1, "date": [], "play#": [], "score": []}
            return player


# Scoreboard functions and stuffs
# Best score placeholder
def best_score_fun():
    with open("playdata.csv", "r") as play_data:
        reader = csv.DictReader(play_data)
        data_list = []
        for row in reader:
            data_list.append(dict(row))
        if len(data_list) > 0:
            data_sorted = sorted(data_list, key=lambda x: x["score"])
            best_player = data_sorted[0]
            return int(best_player["score"])
        else:
            return 1000


def print_scoreboard():
    with open("playdata.csv", "r") as play_data2:
        reader = csv.reader(play_data2)
        for row in reader:
            print(row)


def sort_key(x):
    if x[5].isdigit:
        return x[5]


def print_besttolast():
    with open("playdata.csv", "r") as play_data2:
        reader = csv.reader(play_data2)
        besttolast = list(reader)
        besttolast[1:] = sorted(besttolast[1:], key=sort_key)
        for row in besttolast:
            print(row)


def play_game_fun():
    # Update date
    date = update_date()
    # Best score placeholder
    best_score = best_score_fun()
    # Current game
    current_game_numb = current_game_numb_fun()

    print(f"Welcome to Game number {current_game_numb} on {date}.")
    print(f"You must beat a score of {best_score}! Good luck!")
    secret = random.randint(1, 30)
    attempt = 0
    print()
    while True:
        try:
            print(f"Attempt number: {attempt + 1}")
            guess = int(input("Guess a number between 1-30: "))
            attempt += 1
            if guess == 999:
                print(f"{secret}")

            elif guess < 1 or guess > 30:
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
                if best_score >= attempt:
                    with open("score.txt", "w") as score_txt1:
                        score_txt1.write(f"{attempt}")
                    print(f'Congratulations {player_info["prefix"]}{player_info["name"]},')
                    print(f'you have the new HIGHSCORE with only {attempt} attempts!')

                elif attempt - best_score < 5:
                    print(f'Well done {player_info["prefix"]}{player_info["name"]}, ')
                    print(f'it took you {attempt} attempts but you did make it. Huzzah!')
                else:
                    print(f'Meh {player_info["name"]}, took you {attempt} attempts... quite the overachiever...')
                break
    # Now to punch in the data
    with open("playdata.csv", "a", newline="") as csvdata:
        writer1 = csv.writer(csvdata)
        writer1.writerow([f'{player_info["name"]}', f'{player_info["gender"]}', f'{player_info["age"]}', f'{date}', f'{current_game_numb}', f'{attempt}'])

    # Aftermath choices
    print(f"Game number {current_game_numb} finished. ")
    print("")
    # End of game function


# Start of the program!
best_score = best_score_fun()
print("WELCOME TO GUESS THE SECRET NUMBER!")
print("")
print(f"The current highscore is {best_score}! Good luck!!!")
player_info = last_player()
if player_info["name"] == "":
    player_description_update(player_info)


while True:
    print("n= new player, p= play game, sb = scoreboard, win = best2last")
    commands = input("d= delete scoreboard, q= quit: ")

    if commands == "q":
        break
    elif commands == "sb":
        print("")
        print_scoreboard()
        print("")
    elif commands == "p":
        print("")
        play_game_fun()
    elif commands == "n":
        print("")
        player_description_update(player_info)
        play_game_fun()
    elif commands == "win":
        print_besttolast()
    elif commands == "d":
        clear_scoreboard()
