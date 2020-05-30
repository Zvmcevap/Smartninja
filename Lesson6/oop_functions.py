import json

# Classes
class Player:
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

    def cm_to_meter(self):
        height_m = self.height_cm / 100
        return height_m


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


# Functions
def save_player(player_list):
    with open("basketball_players.json", "w") as bbp_file:
        list_json = []
        for p in player_list:
            list_json.append(vars(p))
        json.dump(list_json, bbp_file)


def load_players():
    player_list = []
    with open("basketball_players.json", "r") as read_file:
        bball_players = json.load(read_file)
        for x in bball_players:
            player_list.append(BasketballPlayer(**x))
    return player_list
