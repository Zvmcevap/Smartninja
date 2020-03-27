from Lesson5 import geography_functions

player_list = []
noob = 0

# Difficulty templates /// country diff and game diff
cdifficulty = []
gdifficulty = []


# Works like a charm, difficulty available as list of countries by continent
easy = []
normal = []
hard = []
geography_functions.get_countries_info(easy, normal, hard)


# Start program player generation
player = geography_functions.Player()
player_list.append(player)
player_list = geography_functions.get_player_list()


while True:
    print(f"Logged in as:{player.name} ------- ID:{player.identity}\n\n")
    command = input("np= new player, p= play game, x= quit:, s= scoreboard: ").lower()
    if command == "x":
        break

    elif command == "np":
        player = geography_functions.Player()
        player.name = input("Enter your name: ").capitalize()
        player.new_id()
    elif command == "pp":
        print(player)
        print(player.name, player.games)

    elif command == "p":
        while True:
            print("\nSelect the difficulty of the countries available")
            print("Points per question: Easy 1x, Normal 1.5x, G.MM: 3x")
            command = input("e= easy, n= normal, g= geopolitical mastermind mode, b= back: ").lower()
            if command == "e":
                cdifficulty = easy
                cdiffstr = "Easy"
                print("You selected easy pool of countries.\n")
                gdifficulty = geography_functions.selecting_gdifficulty(noob)
                last_game = geography_functions.play_game(player, cdifficulty, gdifficulty, cdiffstr, 1)
                if player.games is not None:
                    player.games.append(last_game)
                else:
                    player.games = [last_game]
                geography_functions.add_player_to_json(player)
                break

            elif command == "n":
                cdifficulty = normal
                cdiffstr = "Normal"
                print("You selected normal pool of countries.\n")
                gdifficulty = geography_functions.selecting_gdifficulty(noob)
                last_game = geography_functions.play_game(player, cdifficulty, gdifficulty, cdiffstr, 1)
                if player.games is not None:
                    player.games.append(last_game)
                else:
                    player.games = [last_game]
                geography_functions.add_player_to_json(player)
                break

            elif command == "g":
                cdifficulty = hard
                cdiffstr = "GeoMM"
                print("You selected Geopolitical Mastermind.. humble...\n")
                gdifficulty = geography_functions.selecting_gdifficulty(noob)
                last_game = geography_functions.play_game(player, cdifficulty, gdifficulty, cdiffstr, 1)
                if player.games is not None:
                    player.games.append(last_game)
                else:
                    player.games = [last_game]
                geography_functions.add_player_to_json(player)
                break

            elif command == "b":
                break
            else:
                print("Try selecting again -.-")

    elif command == "s":
        print("SCOREBOARD! SCORREEEBOAAARRD!!!")

    elif command == "rules":
        print("Rules rule")
