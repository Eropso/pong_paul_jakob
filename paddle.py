import pygame
from spillObjekt import SpillObjekt

#arver fra spillobjekt og lager ny instansvariabel hastighet
class Paddle(SpillObjekt):
    def __init__(self, posisjon_x:int, posisjon_y:int, storrelse_x:int, storrelse_y:int, hastighet:int):
        super().__init__(posisjon_x, posisjon_y, storrelse_x, storrelse_y)
        self.hastighet = hastighet
    
    #ikke treffer top
    def bevege_opp(self):
        if self.pos_y > 0:
            self.pos_y -= self.hastighet

    #ikke treffer bottom
    def bevege_ned(self):
        if self.pos_y + self.size_y < 600:
            self.pos_y += self.hastighet




