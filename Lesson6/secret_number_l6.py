from Lesson6 import snumb_functions as fun

highscore = 100
games_list = fun.get_scores_from_txt()
best2last = fun.get_ranking(games_list)
if len(best2last) != 0:
    highscore = best2last[0].score

player_list = []
player = fun.create_player()
player_list.append(player)

while True:
    print(f'Player: {player.name}')
    print("n= new player, p= play, x= exit")
    command = input("s= print score: ")
    if command == "x":
        break
    elif command == "p":
        game, highscore = fun.play_game(player, highscore)
        games_list.append(game)
        fun.add_score_to_txt(games_list)
    elif command == "s":
        best2last = fun.get_ranking(games_list)
        for g in best2last:
            print(f'Name: {g.player_name} --- Score: {g.score} --- Dote: {g.date}')
    elif command == "n":
        player = fun.create_player()
        player_list.append(player)
