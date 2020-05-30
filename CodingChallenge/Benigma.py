import tkinter as tk
import string


lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
numb = list(string.digits)
pun = list(string.punctuation)
pun.append(" ")

symbols = [lower, upper, numb, pun]


def complicate(wrd, sft):
    solution = ""
    for letter in wrd:
        for x in symbols:
            if letter in x:
                fpos = x.index(letter)
                newpos = fpos + sft
                if newpos > len(x):
                    newpos -= len(x)
                solution += x[newpos]
    return solution


def decomplicate(sol, sft):
    dec = ""
    for letter in sol:
        for x in symbols:
            if letter in x:
                fpos = x.index(letter)
                newpos = fpos - sft
                if newpos < 0:
                    newpos += len(x)
                dec += x[newpos]


class Gui:
    # Masta window and variables
    def __init__(self, master, sym):
        self.orgtext = ""
        self.enctext = ""
        self.shift = 0
        self.symbols = sym

        self.master = master
        self.master.geometry("1000x700")
        self.master.title("Benigma und Buring Maschine")

        # Frames
        self.frame_top = tk.Frame(self.master)
        self.frame_top.pack(fill=tk.BOTH, side=tk.TOP)
        self.frame_but = tk.Frame(self.master)
        self.frame_org = tk.LabelFrame(self.master, text="Original message.", bg="grey")
        self.frame_sol = tk.LabelFrame(self.master, text="Coded message.", bg="red")

        self.frame_top.pack(side=tk.TOP)
        self.frame_org.pack(side=tk.LEFT, expand=tk.TRUE, fill=tk.BOTH, padx=50, pady=40)
        self.frame_but.pack(side=tk.LEFT)
        self.frame_sol.pack(side=tk.RIGHT, expand=tk.TRUE, fill=tk.BOTH, padx=50, pady=40)

        # Shift scale
        self.scale_frame = tk.LabelFrame(self.frame_but, text="Set shift level", bg="grey")
        self.scale = tk.Scale(
            self.scale_frame,
            orient=tk.HORIZONTAL,
            from_=0,
            to_=25,
            variable=tk.IntVar
        )
        self.scale_frame.grid(row=2)
        self.scale.pack()

        # Text boxes
        self.naslov = tk.Label(
                               self.frame_top,
                               text="Benos Enigma and Turing Machine!",
                               font=("", 20),
                               pady=20,
                               padx=10
                               )
        self.naslov.pack()
        self.inputtxtorg = tk.Text(self.frame_org, width=20, height=20)
        self.inputtxtorg.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.inputtxtsol = tk.Text(self.frame_sol, width=20, height=20)
        self.inputtxtsol.pack(expand=tk.TRUE, fill=tk.BOTH)

        # Buttons
        self.butcode = tk.Button(
                                 self.frame_but,
                                 text="Encode the message\n------->",
                                 fg="red",
                                 command=lambda: self.encode()
                                 )
        self.butdecode = tk.Button(self.frame_but,
                                   text="Decode the message\n<-------",
                                   command=lambda: self.decode()
                                   )
        self.butcode.grid(row=0)
        self.butdecode.grid(row=1)

    # Fun in functions
    def get_shift(self):
        self.shift = self.scale.get()

    def encode(self):
        self.shift = self.scale.get()
        self.enctext = ""
        self.orgtext = self.inputtxtorg.get(1.0, tk.END)
        for letter in self.orgtext:
            for s in self.symbols:
                if letter in s:
                    fpos = s.index(letter)
                    newpos = fpos + self.shift
                    while newpos >= len(s):
                        newpos -= len(s)
                    self.enctext += s[newpos]
        self.inputtxtsol.delete(1.0, tk.END)
        self.inputtxtsol.insert(tk.END, self.enctext)

    def decode(self, event=None):
        self.shift = self.scale.get()
        self.orgtext = ""
        self.enctext = self.inputtxtsol.get(1.0, tk.END)
        for letter in self.enctext:
            for s in self.symbols:
                if letter in s:
                    fpos = s.index(letter)
                    newpos = fpos - self.shift
                    while newpos < 0:
                        newpos += len(s)
                    self.orgtext += s[newpos]
        self.inputtxtorg.delete(1.0, tk.END)
        self.inputtxtorg.insert(tk.END, self.orgtext)


def main():
    root = tk.Tk()
    Gui(root, symbols)
    root.mainloop()


if __name__ == '__main__':
    main()
