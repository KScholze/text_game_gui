
from tkinter import *

fenster = Tk()
fenster.title("Dungeon")
fenster.geometry("500x760")

rahmen_spielfeld = Frame(fenster, relief = "sunken", borderwidth = 4)

labels = [
    [Label(
        rahmen_spielfeld,
        width = 6,
        height = 3,
        borderwidth = 1,
        relief = "solid"
    ) for i in range(10)] for j in range(10)]

for i in range(10):
    for j in range(10):
        labels[i][j].grid(row = j, column = i)

rahmen_eingabe = Frame(fenster)

label_entry = Label(rahmen_eingabe)
label_info = Label(rahmen_eingabe,
                    text =
                    '***** Steuerung *****\n'
                    '"w" : geradeaus gehen\n'
                    '"a" : nach links gehen\n'
                    '"s" : zurückgehen\n'
                    '"d" : nach rechts gehen\n'        
                    '"f" : kämpfen\n'
                    '"z" : Spiel beenden',
                    justify = "left"
                   )

entry = Entry(rahmen_eingabe, width = 15, borderwidth = 2)
button_eingabe = Button(rahmen_eingabe, text = "Ok")

rahmen_spielfeld.pack()
rahmen_eingabe.pack()

label_entry.pack()
entry.pack()
button_eingabe.pack()
label_info.pack()
