from spillObjekt import SpillObjekt



class Ball(SpillObjekt):
    def __init__(self, posisjon_x, posisjon_y, storrelse_x, storrelse_y, hastighet_x, hastighet_y):
        super().__init__(posisjon_x, posisjon_y, storrelse_x, storrelse_y)
        self._hastigeht_x = hastighet_x
        self._hastighet_y = hastighet_y