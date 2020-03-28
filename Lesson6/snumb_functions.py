import json
import random
from datetime import datetime
from os import path


# Player and Game classes
class Player:
    def __init__(self, name="Guest", bestscore=100, games=None):
        self.name = name
        self.bestscore = bestscore
        self.games = games

    def get_best2last(self):
        if self.games is not None:
            best2last = sorted(self.games, key=lambda x: x.score)
            if len(best2last) > 0:
                return best2last
            else:
                print("No games on record.")
        else:
            print("No games on record.")

    def newest2oldest(self):
        if self.games is not None:
            new2old = sorted(self.games, key=lambda x: x.date.datetime.strptime("%d.%m.%Y %H:%M"))
            return new2old
        else:
            print("No games on record")


class Game:
    def __init__(self, player_name, score, date):
        self.player_name = player_name
        self.score = score
        self.date = date


# Functions and stuff
def create_player():
    name = input("Enter your name: ")
    player = Player(name=name)
    return player


def get_ranking(games_list):
    best2last = sorted(games_list, key=lambda x: x.score)
    return best2last


def add_score_to_txt(player_list):
    with open("score.txt", "w", encoding="utf-8") as write_file:
        list_json = []
        for p in player_list:
            list_json.append(vars(p))
        json.dump(list_json, write_file)


def get_scores_from_txt():
    games_list = []
    if path.exists("score.txt"):
        try:
            with open("score.txt", "r") as file:
                reader = json.load(file)
                for x in reader:
                    games_list.append(Game(**x))
                return games_list
        except:
            print("No score on record.")
            return games_list
    else:
        print("No score on record.")
        return games_list


# Play Game
def play_game(player, hs):
    secret = random.randint(1, 30)
    highscore = hs
    attempt = 0
    print(f"Welcome to Guess the Secret Number.")
    print(f"You must beat a score of {highscore}! Good luck!")
    while True:
        try:
            print(f"\nAttempt number: {attempt + 1}")
            guess = int(input("Guess a number between 1-30: "))
            attempt += 1
            if guess == 999:
                print(f"{secret}")

            elif guess < 1 or guess > 30:
                print("Within 1 and 30, stay between ONE and THIRTY!")
                attempt += 1
                continue
        except ValueError:
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

            elif guess == secret:
                date = datetime.now()
                date = date.strftime("%d.%m.%Y %H:%M")
                # Record game
                game = Game(player.name, attempt, date)
                if attempt <= highscore:
                    highscore = attempt
                    print(f"Congratulations {player.name} you set the new highscore: {highscore}")

                else:
                    print(f"Congratulations {player.name}, you beat the game in {attempt} attempts.")

                return game, highscore
