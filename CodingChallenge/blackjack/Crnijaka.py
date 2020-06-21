import tkinter as tk
from PIL import Image, ImageTk
import glob
import random


deck = []
card_images = []
name = ""
value = ""
colour = ""

for file in glob.glob("cardjpegs/*.jpg"):
    pic = Image.open(file)
    pic_name = file[10:-4]
    card_images.append({pic_name: pic})


class Card:
    def __init__(self, pctr, clr, nm, vl):
        self.colour = clr
        self.name = nm
        self.picture = pctr
        self.value = vl


for c in card_images:
    for x in c:
        picture = c[x]
        if "D" in x:
            colour = "Diamonds"
        elif "H" in x:
            colour = "Hearts"
        elif "S" in x:
            colour = "Spades"
        elif "C" in x:
            colour = "Clubs"

        if 11 > int(x[:-1]) > 1:
            name = x[:-1]
            value = int(name)
        elif int(x[:-1]) == 1:
            name = "Ace"
            value = 1
        elif int(x[:-1]) == 11:
            name = "Jack"
            value = 10
        elif int(x[:-1]) == 12:
            name = "Queen"
            value = 10
        elif int(x[:-1]) == 13:
            name = "King"
            value = 10
        deck.append(Card(picture, colour, name, value))

deck.sort(key=lambda s: s.value)

for x in deck:
    print(f"{x.name} of {x.colour} with a value of {x.value}")

print(len(deck))


class Gui:
    def __init__(self, master):
        self.master = master
        screen_w, screen_h = master.winfo_screenwidth(), master.winfo_screenheight()
        self.master.geometry("{}x{}+{}+{}".format(screen_w, screen_h, 1, 1))

        self.frame = tk.Frame(self.master)
        self.frame.grid(row=0, column=0, rowspan=3)
        self.label = tk.Label(self.frame)


def main():
    root = tk.Tk()
    Gui(root)
    root.mainloop()


# if __name__ == '__main__':
#    main()
