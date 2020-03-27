# import json
# import csv
import random
from datetime import datetime
from Lesson5 import geography_functions

list1 = []
for x in range(5):
    d = datetime.now()
    date = d.strftime("%d.%m.%Y %H:%M  %f")
    unit = {"score": random.randint(1, 10), "date": date}
    list1.append(unit)


class Player:
    def __init__(self, name="Guest", bestscore=0, games=None):
        self.name = name
        self.bestscore = bestscore
        if games is None:
            self.games = games

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
            for g in sorted(self.games, key=lambda dt: datetime.strptime(dt["date"], "%d.%m.%Y %H:%M  %f")):
                print(g)
        else:
            print("No Games on Record")


def up_score(diffmulti, combo):
    combo_x = 1
    if combo > 4:
        combo_x = 2
    elif combo > 9:
        combo_x = 5
    elif combo > 14:
        combo_x = 15
    score_delta = 10 * diffmulti * combo_x
    return score_delta, combo_x
country = {}
country["CapitalName"] = "Ljubljana"
tips = 5
list2 = ["", "a", "b", "b", "l", "k", "j", "l"]





def practice(lst, ctry, tps):
    word_hint = ""
    for letter in ctry["CapitalName"].lower():
        if letter in lst:
            word_hint += letter
        elif letter == " ":
            word_hint += "  "
        else:
            word_hint += " _ "
    print(word_hint.capitalize())
    tps -= 1
    return tps

tips = practice(list2, country, tips)

print(f'tips: {tips}')


