import tkinter as tk
import string


lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
numb = list(string.digits)
pun = list(string.punctuation)
pun.append(" ")

symbols = [lower, upper, numb, pun]


class Gui:
    # Masta window and variables
    def __init__(self, master, sym):
        self.master = master
        # Center le screen
        screen_w, screen_h = master.winfo_screenwidth(), master.winfo_screenheight()
        w, h = 1000, 700
        pos_x, pos_y = (screen_w//2) - (w//2), (screen_h//2) - (h//2)
        self.master.geometry("%dx%d+%d+%d" % (w, h, pos_x, pos_y))
        self.master.title("Benigma und Buring Maschine")
        self.symbols = sym

        self.orgtext = ""
        self.enctext = ""
        self.shift = tk.IntVar()

        self.checkvar = tk.IntVar(value=1)
        # Frames
        self.frame_top = tk.Frame(self.master)
        self.frame_top.pack(fill=tk.BOTH, side=tk.TOP)
        self.frame_but = tk.Frame(self.master)
        self.frame_org = tk.LabelFrame(self.master, text="Original message", bg="grey")
        self.frame_sol = tk.LabelFrame(self.master, text="Coded message", bg="red")

        self.frame_top.pack(side=tk.TOP)
        self.frame_org.pack(side=tk.LEFT, expand=tk.TRUE, fill=tk.BOTH, padx=50, pady=40)
        self.frame_but.pack(side=tk.LEFT)
        self.frame_sol.pack(side=tk.RIGHT, expand=tk.TRUE, fill=tk.BOTH, padx=50, pady=40)

        # Shift scale
        self.scale_frame = tk.LabelFrame(self.frame_but, text="Set shift level", bg="grey")
        self.scale = tk.Scale(
            self.scale_frame,
            orient=tk.HORIZONTAL,
            length=152,
            from_=0,
            to_=25,
            variable=self.shift,
            command=lambda x: self.encode()
        )
        self.scale_frame.grid(row=2)
        self.scale.pack()

        # Text boxes
        self.naslov = tk.Label(
               self.frame_top,
               text="Benos Enigma and Turing Machine!",
               font=("", 20),
               pady=20,
               padx=10,
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
             command=lambda: self.encode(),
             width=20
             )
        self.checkbox = tk.Checkbutton(
            self.frame_but,
            text="Benigma",
            variable=self.checkvar,
            pady=20,
            command=lambda: self.update_check(),
            width=8,
            anchor="w"
        )
        self.butcode.grid(row=0)
        self.checkbox.grid(row=1)

    # Fun in functions
    def update_check(self):
        if self.checkvar.get() == 1:
            self.checkbox.configure(text="Benigma")
            self.butcode.configure(text="Encode the message\n------->", fg="red")
        else:
            self.butcode.configure(text="Decode the message\n<------", fg="black")
            self.checkbox.configure(text="Buring")

    def encode(self):
        benigma = self.checkvar.get()
        shift = self.shift.get()
        if benigma:
            text = self.inputtxtorg.get(1.0, tk.END)
            self.enctext = ""
        else:
            text = self.inputtxtsol.get(1.0, tk.END)
            self.orgtext = ""
            shift = -shift

        for letter in text:
            for s in self.symbols:
                if letter in s:
                    fpos = s.index(letter)
                    newpos = fpos + shift
                    if benigma:
                        while newpos >= len(s):
                            newpos -= len(s)
                        self.enctext += s[newpos]
                    else:
                        while newpos < 0:
                            newpos += len(s)
                        self.orgtext += s[newpos]
        if benigma:
            self.inputtxtsol.delete(1.0, tk.END)
            self.inputtxtsol.insert(tk.END, self.enctext)
        else:
            self.inputtxtorg.delete(1.0, tk.END)
            self.inputtxtorg.insert(tk.END, self.orgtext)


def main():
    root = tk.Tk()
    Gui(root, symbols)
    root.mainloop()


if __name__ == '__main__':
    main()
