from spillObjekt import SpillObjekt
import random
bredde, hoyde = 800, 600

class Ball(SpillObjekt):
    def __init__(self, posisjon_x, posisjon_y, storrelse_x, storrelse_y, hastighet_x, hastighet_y):
        super().__init__(posisjon_x, posisjon_y, storrelse_x, storrelse_y)
        self._hastighet_x = hastighet_x
        self._hastighet_y = hastighet_y

    def oppdater(self):
        self.pos_x += self._hastighet_x
        self.pos_y += self._hastighet_y

    def kollisjon(self, paddle_venstre, paddle_hoyre):
        #kollisjon venstre paddle
        if (self.pos_x <= paddle_venstre.pos_x + paddle_venstre.size_x and
            self.pos_x + self.size_x >= paddle_venstre.pos_x and
            self.pos_y + self.size_y >= paddle_venstre.pos_y and
            self.pos_y <= paddle_venstre.pos_y + paddle_venstre.size_y):
            if self._hastighet_x > 0:
                self._hastighet_x += 0.2
            else:
                self._hastighet_x -= 0.2
            self._hastighet_x *= -1
            self._hastighet_y = random.randint(-5, 5)
            self.pos_x = paddle_venstre.pos_x + paddle_venstre.size_x

        #kollisjon høyre paddle
        if (self.pos_x + self.size_x >= paddle_hoyre.pos_x and
            self.pos_x <= paddle_hoyre.pos_x + paddle_hoyre.size_x and
            self.pos_y + self.size_y >= paddle_hoyre.pos_y and
            self.pos_y <= paddle_hoyre.pos_y + paddle_hoyre.size_y):
            if self._hastighet_x > 0:
                self._hastighet_x += 0.2
            else:
                self._hastighet_x -= 0.2
            self._hastighet_x *= -1
            self._hastighet_y = random.randint(-5, 5)
            self.pos_x = paddle_hoyre.pos_x - self.size_x

        # kollisjon topp, bunn
        if self.pos_y <= 0 or self.pos_y >= hoyde - self.size_y:
            self._hastighet_y *= -1

            
    def sjekk_score(self):
        # Ball går ut venstre (høyre scorer)
        if self.pos_x <= 0:
            self.pos_x = bredde/2 - self.size_x
            self.pos_y = hoyde/2 - self.size_y
            if self._hastighet_x > 0:
                self._hastighet_x = 7
            else:
                self._hastighet_x = -7
            self._hastighet_x *= -1
            return "hoyre"

        # Ball går ut høyre (venstre scorer)
        if self.pos_x >= bredde - self.size_x:
            self.pos_x = bredde/2 - self.size_x
            self.pos_y = hoyde/2 - self.size_y
            if self._hastighet_x > 0:
                self._hastighet_x = 7
            else:
                self._hastighet_x = -7
            self._hastighet_x *= -1
            return "venstre"
        
        return None
