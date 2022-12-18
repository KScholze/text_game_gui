
from text_game.game_data import *
from text_game.game_gui import *
import random

# Spielfeld erzeugen (Länge, Breite, Schatz-Position X, Schatz-Position Y)
feld = Feld(10, 10, 9, 8)

# Player erzeugen (Position X, Position Y, hp, Waffe, Waffenstärke)
spieler = Spieler(1, 1, 100, "Knüppel", 10)
labels[spieler.x_pos - 1][10 - spieler.y_pos].configure(text = "x")
im_kampf = False

def eingabe_verarbeiten():
    label_entry.configure(text = "Was wirst du tun?")
    eingabe = entry.get()
    entry.delete(0, END)
    if im_kampf == True:
        kampf_verarbeiten(eingabe)
    # Player über das Spielfeld bewegen, solange Spielfeld-Ende nicht erreicht
    elif eingabe == "w" or eingabe == "s" or eingabe == "d" or eingabe == "a":
        bewegen(eingabe)
        # Spiel beenden, wenn abgebrochen werden soll
    elif eingabe == "z":
        exit()
    else:
        label_entry.configure(text = "Ungültige Eingabe")

button_eingabe.configure(command = eingabe_verarbeiten)

def bewegen(eingabe):
    # Player über das Spielfeld bewegen, solange Spielfeld-Ende nicht erreicht
    if eingabe == "w" and spieler.y_pos < feld.hoehe:
        labels[spieler.x_pos - 1][10 - spieler.y_pos].configure(text = "")
        spieler.y_pos += 1
    elif eingabe == "s" and spieler.y_pos > 1:
        labels[spieler.x_pos - 1][10 - spieler.y_pos].configure(text = "")
        spieler.y_pos -= 1
    elif eingabe == "d" and spieler.x_pos < feld.breite:
        labels[spieler.x_pos - 1][10 - spieler.y_pos].configure(text = "")
        spieler.x_pos += 1
    elif eingabe == "a" and spieler.x_pos > 1:
        labels[spieler.x_pos - 1][10 - spieler.y_pos].configure(text = "")
        spieler.x_pos -= 1
    else:
        label_entry.configure(text = "Du kommst hier nicht weiter.")
        return

    labels[spieler.x_pos - 1][10 - spieler.y_pos].configure(text = "x")

    if spieler.x_pos == feld.schatz_position_x and spieler.y_pos == feld.schatz_position_y:
        def schatz_gefunden():
            label_entry.configure(text = "Du hast den Schatz gefunden! Das Spiel ist vorbei...")
        label_entry.configure(text = "Du hast den Schatz gefunden!")
        button_eingabe.configure(command = schatz_gefunden)
    else:
        ereignis()

def spieler_lebt():
    global spieler
    if spieler.hp < 1:
        label_entry.configure(text = "Du hast den Kampf nicht überlebt!")
        del spieler
        def spieler_gestorben():
            label_entry.configure(text = "Du bist gestorben. Das Spiel ist vorbei...")
        button_eingabe.configure(command = spieler_gestorben)

gegner = Gegner("Gegner", 0, 0)
def kampf_verarbeiten(eingabe):
    global im_kampf
    global gegner
    if eingabe == "f":
        gegner.hp -= spieler.staerke
        if gegner.hp < 1:
            label_entry.configure(text = f"Du hast den {gegner.name} getötet!")
            del gegner
            im_kampf = False
        else:
            spieler.hp -= gegner.staerke
            label_entry.configure(
                text =
                "Dein Gegner ist noch nicht tot.\n"
                "Kämpfst du oder läufst du weg? (Wahrscheinlichkeit, fliehen zu können: 1/3)\n"
                'Gib "f" für kämpfen ein, etwas anderes für flüchten.\n'
                f"Deine aktuelle Gesundheit: {spieler.hp}"
            )
            spieler_lebt()
    else:
        ereignis_wahrscheinlichkeit = random.randint(1, 3)
        if ereignis_wahrscheinlichkeit == 1:
            label_entry.configure(text = "Deine Flucht war erfolgreich!")
            im_kampf = False
        else:
            spieler.hp -= gegner.staerke
            label_entry.configure(
                text=
                "Du wirst angegriffen!\n"
                "Dein Gegner ist noch nicht tot.\n"
                "Kämpfst du oder läufst du weg? (Wahrscheinlichkeit, fliehen zu können: 1/3)\n"
                'Gib "f" für kämpfen ein, etwas anderes für flüchten.\n'
                f"Deine aktuelle Gesundheit: {spieler.hp}"
            )
            spieler_lebt()

def ereignis():
    # Unterfunktion kaempfen() (Funktion in der Funktion ereignis())
    def kaempfen():
        global im_kampf
        im_kampf = True
        ereignis_wahrscheinlichkeit = random.randint(1, 3)

        global gegner
        # Gegner ist ein Goblin (Wahrscheinlichkeit 2/3)
        if ereignis_wahrscheinlichkeit == 1 or ereignis_wahrscheinlichkeit == 2:
            gegner = Goblin()
        # Gegner ist ein Zwerg (Wahrscheinlichkeit 1/3)
        else:
            gegner = Zwerg()

        label_entry.configure(
            text =
            f"Mist! Ein {gegner.name} stellt sich mir in den Weg!\n"
            "Kämpfst du oder läufst du weg? (Wahrscheinlichkeit, fliehen zu können: 1/3)\n"
            'Gib "f" für kämpfen ein, etwas anderes für flüchten.\n'
            f"Deine aktuelle Gesundheit: {spieler.hp}"
        )

    # Unterfunktion waffe_gefunden() (Funktion in der Funktion ereignis())
    def waffe_gefunden():
        waffen_index = random.randint(0, len(waffen) - 1)
        gefundene_waffe = list(waffen.keys())[waffen_index]
        label_text = f"Du hast eine neue Waffe gefunden.\nDie neue Waffe: {gefundene_waffe}"
        if spieler.staerke >= list(waffen.values())[waffen_index]:
            label_text += "\nSo ein Mist! Die Waffe ist schwächer als meine bisherige."
            label_entry.configure(text = label_text)
        else:
            label_text += "\nDie Waffe wird mir gute Dienste leisten..."
            label_entry.configure(text = label_text)
            spieler.waffe = gefundene_waffe
            spieler.staerke = list(waffen.values())[waffen_index]

    # zufällige Ereignisse steuern
    ereignis_wahrscheinlichkeit = random.randint(1, 10)

    # 1. Gegner taucht auf (Wahrscheinlichkeit 1/5)
    if ereignis_wahrscheinlichkeit <= 2:
        kaempfen()

    # 2. Waffe wird gefunden (Wahrscheinlichkeit 1/10)
    elif ereignis_wahrscheinlichkeit == 3:
        waffe_gefunden()
