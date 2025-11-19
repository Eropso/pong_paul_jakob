import pygame
from spillObjekt import SpillObjekt

class Paddle(SpillObjekt):
    def __init__(self, posisjon_x:int, posisjon_y:int, storrelse_x:int, storrelse_y:int, hastighet:int):
        super().__init__(posisjon_x, posisjon_y, storrelse_x, storrelse_y)
        self.hastighet = hastighet
    def bevege_opp(self):
        self.rect.y -= self.hastighet

    def bevege_ned(self):
        self.rect.y += self.hastighet

            



