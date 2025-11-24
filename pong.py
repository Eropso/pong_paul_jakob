import pygame
from ball import Ball
from paddle import Paddle
pygame.init()
 
font = pygame.font.SysFont(None, 24)

bredde, hoyde = 800, 600
hvit = (255, 255, 255)
FPS = 60

skjerm = pygame.display.set_mode((bredde, hoyde))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

ball = Ball(380, 280, 20, 20, 7, 7)
paddle_venstre = Paddle(50, 250, 20, 100, 10)
paddle_hoyre = Paddle(730, 250, 20, 100, 10)

class Spill:
    def __init__(self):
        self.aktiv = True
        self.poeng_hoyre = 0
        self.poeng_venstre = 0
    
    def loop(self):
        while self.aktiv == True:
            for hendelse in pygame.event.get():
                if hendelse.type == pygame.QUIT:
                    self.aktiv = False

            ball.kollisjon(paddle_venstre, paddle_hoyre)
            ball.oppdater()

            # Sjekk om noen har scoret
            scorer = ball.sjekk_score()
            if scorer == "hoyre":
                self.poeng_hoyre += 1
            elif scorer == "venstre":
                self.poeng_venstre += 1


            taster = pygame.key.get_pressed()

            #Spiller venstre
            if taster[pygame.K_w]:
                paddle_venstre.bevege_opp()
            if taster[pygame.K_s]:
                paddle_venstre.bevege_ned()
            
            #Spiller høyre
            if taster[pygame.K_UP]:
                paddle_hoyre.bevege_opp()
            if taster[pygame.K_DOWN]:
                paddle_hoyre.bevege_ned()

            skjerm.fill((0, 0, 0))

            # Viser score
            poeng1 = f'{self.poeng_venstre}'
            cords = font.render(poeng1, True, (255,255,255))
            skjerm.blit(cords, (80, 20))

            poeng2 = f'{self.poeng_hoyre}'
            cords = font.render(poeng2, True, (255,255,255))
            skjerm.blit(cords, (bredde - 90, 20))

            # Kjører at ballen og paddles blir tegnet
            ball.tegn()
            paddle_venstre.tegn()
            paddle_hoyre.tegn()

            pygame.display.flip()
            clock.tick(FPS)

Spill().loop()
