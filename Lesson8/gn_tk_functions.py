import json
from os import path
import tkinter


class Player:
    def __init__(self, name="Guest", games=None, bestscore=0):
        self.name = name
        self.games = games
        self.bestscore = bestscore

    def get_bestscore(self):
        best2last = []
        if self.games is not None:
            if len(self.games) > 0:
                best2last = sorted(self.games, key=lambda g: g["Score"])
                return best2last[0]["Score"]
            else:
                return 0
        else:
            return 0


def load_players():
    player_list = []
    if path.exists("players.json"):
        with open("players.json" "r") as file:
            players_lst_dct = json.load(file)
            if len(players_lst_dct) > 0:
                for player in players_lst_dct:
                    player_list.append(Player(**player))
            return player_list
    else:
        return player_list


def save_players(player_list):
    player_lst_dct = []
    for player in player_list:
        player_lst_dct.append(vars(player))
    if len(player_lst_dct) > 0:
        with open("players.json", "w") as file:
            json.dump(player_lst_dct, file)


def new_player_window():
    player = ""
    def set_player(event=None):
        player = ent_name.get()
        return player

    def print_player():
        print(player)

    window = tkinter.Toplevel()
    lbl_enter_name = tkinter.Label(master=window, text="Enter your name: ")
    lbl_enter_name.grid(row=0, column=0, columnspan=2)
    ent_name = tkinter.Entry(master=window, width=30)
    ent_name.focus_set()
#    ent_name.bind("<Return>", r)
    ent_name.grid(row=1, column=0)
    btn_enter = tkinter.Button(window, command=set_player)
    btn_enter.grid(row=1, column=1)
    btn_print = tkinter.Button(master=window, command=print_player)
    btn_print.grid(row=1, column=2)
    player = ent_name.get()
    return
