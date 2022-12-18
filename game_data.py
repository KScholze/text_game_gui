
class Feld():
    def __init__(self, b, h, x, y):
        self.breite = b
        self.hoehe = h
        self.schatz_position_x = x
        self.schatz_position_y = y

    @property
    def breite(self):
        return self.__breite
    @breite.setter
    def breite(self, b):
        self.__breite = b

    @property
    def hoehe(self):
        return self.__hoehe
    @hoehe.setter
    def hoehe(self, h):
        self.__hoehe = h

    @property
    def schatz_position_x(self):
        return self.__schatz_position_x
    @schatz_position_x.setter
    def schatz_position_x(self, x):
        self.__schatz_position_x = x

    @property
    def schatz_position_y(self):
        return self.__schatz_position_y
    @schatz_position_y.setter
    def schatz_position_y(self, y):
        self.__schatz_position_y = y

class Spieler():
    def __init__(self, x, y, h, w, s):
        self.x_pos = x
        self.y_pos = y
        self.hp = h
        self.waffe = w
        self.staerke = s

    @property
    def x_pos(self):
        return self.__x_pos
    @x_pos.setter
    def x_pos(self, x):
        self.__x_pos = x

    @property
    def y_pos(self):
        return self.__y_pos
    @y_pos.setter
    def y_pos(self, y):
        self.__y_pos = y

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, h):
        self.__hp = h

    @property
    def waffe(self):
        return self.__waffe
    @waffe.setter
    def waffe(self, w):
        self.__waffe = w

    @property
    def staerke(self):
        return self.__staerke
    @staerke.setter
    def staerke(self, s):
        self.__staerke = s

class Gegner():
    def __init__(self, n, h, s):
        self.name = n
        self.hp = h
        self.staerke = s

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, n):
        self.__name = n

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, h):
        self.__hp = h

    @property
    def staerke(self):
        return self.__staerke
    @staerke.setter
    def staerke(self, s):
        self.__staerke = s

class Goblin(Gegner):
    def __init__(self):
        super().__init__("Goblin", 20, 10)

class Zwerg(Gegner):
    def __init__(self):
        super().__init__("Zwerg", 30, 20)

waffen = {"Baseballschläger" : 12, "Eisenstange" : 15, "Schwert" : 20}
