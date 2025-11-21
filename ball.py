from spillObjekt import SpillObjekt

bredde, hoyde = 800, 600

class Ball(SpillObjekt):
    def __init__(self, posisjon_x, posisjon_y, storrelse_x, storrelse_y, hastighet_x, hastighet_y):
        super().__init__(posisjon_x, posisjon_y, storrelse_x, storrelse_y)
        self._hastighet_x = hastighet_x
        self._hastighet_y = hastighet_y

    def oppdater(self):
        self.pos_x += self._hastighet_x
        self.pos_y += self._hastighet_y

    def kollisjon(self):
        if self.pos_x <= 0 or self.pos_x >= bredde - 20:
            self._hastighet_x *= -1

        if self.pos_y <= 0 or self.pos_y >= hoyde - 20:
            self._hastighet_y *= -1
