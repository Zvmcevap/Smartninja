import random
import csv
from os import path
from datetime import datetime
import json


# CSV and JSON and Data specific functions /// csv might be obsolete (it is) ///
def print_csv(file):
    if path.exists(file):
        with open(file, "r") as csv_file:
            reader = csv.reader(csv_file)
            for x in reader:
                print(x)
    else:
        print("File does not exist! Making one!")
        with open(file, "w") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Name", "ID", "BestScore", "Games"])


def add_to_csv(file, player):
    if path.exists(file):
        with open(file, "a", newline="") as csv_file:
            fields = ["Name", "ID", "BestScore", "Games"]
            writer = csv.DictWriter(csv_file, fieldnames=fields)
            writer.writerow(player)
    else:
        with open(file, "w", newline="") as csv_file:
            fields = ["Name", "ID", "BestScore", "Games"]
            writer = csv.DictWriter(csv_file, fieldnames=fields)
            writer.writeheader()
            writer.writerow(player)


# My man JSON
def get_countries_info(easy, normal, hard):
    with open("country-capitals.json", "r") as file:
        data = json.load(file)
        for country in data:
            if country["CapitalName"] == "N/A" or country["CountryCode"] == "NULL":
                pass
            elif country["ContinentName"] == "Europe" or country["ContinentName"] == "North America":
                easy.append(country)
                normal.append(country)
                hard.append(country)
            elif country["ContinentName"] == "Asia" or country["ContinentName"] == "South America":
                normal.append(country)
                hard.append(country)
            else:
                hard.append(country)


# Game specific funcitons // Meet of the problem //
def get_the_country(data):
    country = random.choice(data)
    return country


def update_difficulty_multiplier(cd, gd):
    multiplier = 1
    if cd == "easy":
        multiplier *= 1
    elif cd == "normal":
        multiplier *= 2
    elif cd == "hard":
        multiplier *= 5
    if gd == "easy":
        multiplier *= 0.5
    elif gd == "normal":
        multiplier *= 1
    elif gd == "hard":
        multiplier *= 3
    return multiplier


def update_tips(gd):
    utips = 0
    if gd == "easy":
        utips = 3
    elif gd == "normal":
        utips = 2
    elif gd == "hard":
        utips = 1
    return utips


def up_score(diffmulti, combo):
    new_score = 10 * diffmulti * combo
    return new_score


def combo_x(combo):
    multi = 1
    if combo > 14:
        multi = 15
    elif combo > 9:
        multi = 5
    elif combo > 4:
        multi = 2
    return multi


def calculate_tips(guess, country, score, tips):
    if len(guess) <= 1:
        if guess == "":
            if score - 5 <= 0:
                print("You will loose if you go below 0 points, tip DENIED! Har har!")
                return tips, score
            else:
                tips -= 1
                score -= 5
        else:
            if score - 10 <= 0:
                print("You will loose if you go below 0 points, tip DENIED! Har har!")
                return tips, score
            else:
                tips -= 1
                score -= 10
        return tips, score
    if guess == "dunce":
        if score - 20 <= 0:
            print("You will loose if you go below 0 points, tip DENIED! Har har!")
            return tips, score
        else:
            score -= 10
            tips -= 1
            print(country["CountryName"])
            return tips, score
    else:
        print("Cant follow instructions, tip wasted!")
        tips -= 1
        return tips, score


def print_tip(tips_jar, country):
    word_hint = ""
    for letter in country["CapitalName"].lower():
        if letter in tips_jar:
            word_hint += letter
        elif letter == " ":
            word_hint += "  "
        else:
            word_hint += " _ "
    print(word_hint)


def play_game(player, cdifficulty, gdifficulty, cdiffstr, highscore):
    print(f'Player: {player.name} ID: {player.identity}')
    print(f'Difficulty: {cdiffstr} -- {gdifficulty}\n')
    print(f"Current High Score: {highscore}\n")
    diff_x = update_difficulty_multiplier(cdiffstr, gdifficulty)
    tips = update_tips(gdifficulty)
    question_number = 0
    score = 100
    combo_counter = 0
    attempts = 5
    guess = ""
    while True:
        if attempts == 0 or score == 0 or guess == "quit":
            date = datetime.now()
            date = date.strftime("%d.%m.%Y  %H:%M")
            game = {
                "score": score,
                "difficulty": f"{cdiffstr}, {gdifficulty}",
                "date": date
            }
            print(f"Youve made it to question {question_number}, with a score of {score}. Yay you.. GAME OVER!!!")
            return game
        country = get_the_country(cdifficulty)
        question_number += 1
        tip_jar = []
        if gdifficulty == "easy":
            if "" not in tip_jar:
                tip_jar.append("")
        while True:
            print(f"\nScore:{score}\n  + {10 * diff_x}")
            print(f"Question number: {question_number} ---- Lives: {attempts} Tips: {tips}")
            print(f"Combo: {combo_counter} ----- {combo_x(combo_counter)}X multiplier.")
            if gdifficulty == "hard" and "dunce" not in tip_jar:
                print(f'What is the capital of {country["CountryCode"]}?\n')
            else:
                print(f'What is the capital of {country["CountryName"]}?\n')
            if len(tip_jar) > 0:
                print_tip(tip_jar, country)
            print(f'Debug cheat: {country["CapitalName"]}')
            print('\nType "tip" to use tip, "pass" to skip an answer (uses Life, -50 points)')
            guess = input('What say you?: ').lower()
            if guess == "quit":
                break
            if guess == "tip":
                if tips > 0:
                    if gdifficulty == "hard":
                        print("Type dunce to reveal the name of the Country (-10 points)")
                    print("Type a letter to reveal it (-10 points), Enter to reveal number of letters (-5 points)")
                    guess = input("Or type back if you've changed your mind: ").lower()
                    if guess == "dunce":
                        if score - 10 <= 0:
                            print("You will loose if you go below 0 points, tip DENIED! Har har!")
                        else:
                            tips, score = calculate_tips(guess, country, score, tips)
                    if guess.lower() != "back":
                        tip_jar.append(guess)
                        tips, score = calculate_tips(guess, country, score, tips)
                else:
                    print("You have used up all your tips! Sorry!")
            elif guess == "pass":
                if attempts > 1 and score - 50 > 0:
                    print("Question skipped.")
                    combo_counter = 0
                    attempts -= 1
                    score -= 50
                    break
                else:
                    print("Too few points or lives to skip, it would kill you! DENIED!")
            elif guess == country["CapitalName"].lower():
                print(f"Congratulations! The capital is {country['CapitalName']}!")
                print(f"+ {up_score(diff_x, combo_x(combo_counter))} points!!!")
                score += up_score(diff_x, combo_x(combo_counter))
                combo_counter += 1
                break
            else:
                attempts -= 1
                combo_counter = 0
                if attempts == 0:
                    break
                else:
                    print(f"Sorry, try again. Youve lost a life!")


def selecting_gdifficulty(noob):
    while True:
        print("\nSelect the difficulty of the game.")
        print("e= easy,you get 3 tips at start and number of letters in the answer but only half points.")
        print("n= normal, you get 2 tips at start and a normal amount of points.")
        print("g= geography god mode, no tips and you only get country code instead of name, 3x points though!")
        command = input("e= easy, n= normal, g= godmode, b= back: ").lower()
        if command == "e":
            gdifficulty = "easy"
            print(gdifficulty)
            return gdifficulty
        elif command == "n":
            gdifficulty = "normal"
            print(gdifficulty)
            return gdifficulty
        elif command == "g":
            gdifficulty = "hard"
            print(gdifficulty)
            return gdifficulty
        elif command == "b":
            break
        else:
            noob += 1
            if noob < 3:
                print("Try again...")
            else:
                noob = 0
                print("Type in 'e', go for easy, trust me ;)")


# Player Class --------- making a big divide with comment ----------
class Player:
    def __init__(self, name="Guest", identity=random.randint(10000, 99999), bestscore=0, games=None):
        self.name = name
        self.identity = identity
        self.bestscore = bestscore
        if games is None:
            self.games = []

    def new_id(self):
        self.identity = random.randint(10000, 99999)

    def update_bestscore(self):
        if self.games is not None:
            best2last = sorted(self.games, key=lambda s: s["score"], reverse=True)
            bestgame = best2last[0]
            self.bestscore = bestgame["score"]
        else:
            print("No Games on Record")

    def get_best2last(self):
        if self.games is not None:
            for g in sorted(self.games, key=lambda s: s["score"], reverse=True):
                print(g)
        else:
            print("No Games on Record")

    def get_games_by_date(self):
        if self.games is not None:
            for g in sorted(self.games, key=lambda dt: datetime.strptime(dt["date"], "%d.%m.%Y %H:%M")):
                print(g)
        else:
            print("No Games on Record")


# lets send players to jason
def add_player_to_json(player):
    with open("players.json" "a") as players_file:
        players_file.write(json.dump(player, players_file))


def get_player_list():
    if path.exists("players.json"):
        with open("players.json", "r") as file:
            data = json.load(file)
            return data
