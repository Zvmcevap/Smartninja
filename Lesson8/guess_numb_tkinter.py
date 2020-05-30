import tkinter
from Lesson8 import gn_tk_functions as fun


# Variables
player_list = []
games_list = []
player = fun.Player()
highscore = 0

# The window
window = tkinter.Tk()
window.geometry("700x500")
frame_top = tkinter.Frame(window, relief=tkinter.GROOVE, borderwidth=5, background="#006600")
frame_mid = tkinter.Frame(window)
frame_name_hs = tkinter.Frame(window, width=100)
# Text and stuff
lbl_title = tkinter.Label(
    text="Guess the secret number game!",
    font=("", 20),
    bg="#CCFFCC",
    width=30,
    height=2,
    master=frame_top
)
lbl_title.pack()
frame_top.pack(fill=tkinter.BOTH, side=tkinter.TOP)


# Name and highscore
lbl_player_name = tkinter.Label(frame_name_hs, text=f"Nombre: {player.name}")
lbl_highscore = tkinter.Label(frame_name_hs, text=f"Highscore: {highscore}")
lbl_player_name.grid(row=0, column=1)
lbl_highscore.grid(row=0, column=3)

frame_name_hs.columnconfigure(0, weight=1)
frame_name_hs.columnconfigure(4, weight=1)
frame_name_hs.columnconfigure(2, weight=1)
frame_name_hs.rowconfigure(0, weight=1)
frame_name_hs.pack(fill=tkinter.BOTH, ipady=20)

# Main Menu Buttons
# Play Button
btn_play = tkinter.Button(master=frame_mid, text="PLAY", command=None, width=20)

# New Player Button
btn_new_player = tkinter.Button(master=frame_mid, text="NEW PLAYER", width=20, command=fun.new_player_window)

btn_scoreboard = tkinter.Button(master=frame_mid, text="SCOREBOARD", width=20)
btn_quit = tkinter.Button(master=frame_mid, text="QUIT", width=20, command=window.quit)

btn_play.grid(row=1)
btn_new_player.grid(row=2)
btn_scoreboard.grid(row=3)
btn_quit.grid(row=4)

frame_mid.grid_rowconfigure(0, weight=1)
frame_mid.grid_rowconfigure(5, weight=1)
frame_mid.pack(side=tkinter.BOTTOM, fill=tkinter.Y, expand=1)









'''
# Play the game

ent_guess = tkinter.Entry(master=frame_mid, width=20)
ent_guess.insert(0, "Enter the number")
ent_guess.pack(side=tkinter.LEFT)

secret = random.randint(1, 30)


def delete_entry_pg(event=None):
    if ent_guess.get() == "Enter the number":
        ent_guess.delete(0, tkinter.END)
    print(event)


def check_guess(event=None):
    guess = int(ent_guess.get())
    result_text = ""
    if guess == secret:
        result_text = "Correct"

    elif guess < secret:
        result_text = "Try a bigger number!"

    elif guess > secret:
        result_text = "Try a smaller number!"

    messagebox.showinfo("Result:", result_text)
    print(type(event))

# Pressing Enter in the Entry box
ent_guess.bind("<Return>", check_guess)
ent_guess.bind("<Button-1>", delete_entry_pg)

# Submit button
submit = tkinter.Button(text="Submit", command=check_guess, master=frame_mid)
submit.pack(side=tkinter.RIGHT)
frame_mid.pack(side=tkinter.BOTTOM, expand=True)
'''
# Keep the window open
window.mainloop()
