from Lesson6 import oop_functions as fun


lebron = fun.BasketballPlayer(first_name="LeBron", last_name="James", height_cm=203, weight_kg=113, points=27.7, rebounds=7.4, assists=7.2)
kev_dur = fun.BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2, rebounds=7.1, assists=4)
bball_players = [lebron, kev_dur]

messi = fun.FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575, yellow_cards=67, red_cards=0)
ronaldo = fun.FootballPlayer(first_name="Cristiano", last_name="Ronaldo", height_cm=184, weight_kg=79, goals=586, yellow_cards=95, red_cards=11)
fball_players = [messi, ronaldo]

custom_player = fun.BasketballPlayer(first_name=input("Enter first name: "), last_name=input("Enter last name: "), height_cm=int(input("Enter Height: ")), weight_kg=int(input("Enter weight: ")), assists=float(input("Assists: ")), points=float(input("Points: ")), rebounds=float(input("Rebounds: ")))

bball_players.append(custom_player)

fun.save_player(bball_players)
test_list = fun.load_players()



for p in test_list:
    print(p.first_name, p.last_name, p.weight_to_lbs())
