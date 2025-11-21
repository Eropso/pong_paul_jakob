import pygame
from ball import Ball
from paddle import Paddle
from spillObjekt import SpillObjekt
pygame.init()
 

bredde, hoyde = 800, 600
hvit = (255, 255, 255)
FPS = 60

skjerm = pygame.display.set_mode((bredde, hoyde))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

ball = Ball(380, 280, 20, 20, 5, 5)
paddle_venstre = Paddle(50, 250, 20, 100, 5)
paddle_hoyre = Paddle(730, 250, 20, 100, 5)

class Spill:
    def __init__(self):
        self.aktiv = True
    
    def loop(self):
        while self.aktiv == True:
            for hendelse in pygame.event.get():
                if hendelse.type == pygame.QUIT:
                    self.aktiv = False

            ball.oppdater()

            skjerm.fill((0, 0, 0))

            ball.tegn()
            paddle_venstre.tegn()
            paddle_hoyre.tegn()

            pygame.display.flip()
            clock.tick(FPS)

Spill().loop()
