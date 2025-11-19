from spillObjekt import SpillObjekt

class Paddle(SpillObjekt):
    def __init__(self, posisjon_x:int, posisjon_y:int, hastighet:int):
        super().__init__(posisjon_x, posisjon_y)
        self.hastighet = hastighet

        



