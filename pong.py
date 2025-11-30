import pygame
from ball import Ball
from paddle import Paddle
pygame.init()
 
font = pygame.font.SysFont('Impact', 24)

bredde, hoyde = 800, 600
hvit = (255, 255, 255)
FPS = 60

skjerm = pygame.display.set_mode((bredde, hoyde))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

#lage objektene
ball = Ball(380, 280, 20, 20, 7, 7)
paddle_venstre = Paddle(50, 250, 20, 100, 10)
paddle_hoyre = Paddle(730, 250, 20, 100, 10)

restart = 'Trykk For Restart'
restart_cords = font.render(restart, True, (255,255,255))


class Spill:
    def __init__(self):
        self.aktiv = True
        self.poeng_hoyre = 0
        self.poeng_venstre = 0
    
    #spill løkken
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

            # Sjekker vinner spiller 1 (venstre)
            if self.poeng_venstre == 4:
                vinner1 = 'Spiller 1 Vinner'
                skjerm.blit(restart_cords, (bredde/2 - 85, hoyde/2 - 85))
                cords = font.render(vinner1, True, (255,255,255))
                skjerm.blit(cords, (bredde/2 - 80, 50))

                #stopper ballen
                ball._hastighet_x = 0
                ball._hastighet_y = 0

                #restart ved klikk
                if hendelse.type == pygame.MOUSEBUTTONDOWN:
                    ball._hastighet_x = 7
                    ball._hastighet_y = 7
                    self.poeng_hoyre = 0
                    self.poeng_venstre = 0

            # Sjekker vinner spiller 2 (høyre)
            elif self.poeng_hoyre == 4:
                vinner2 = 'Spiller 2 Vinner'
                skjerm.blit(restart_cords, (bredde/2 - 85, hoyde/2 - 85))
                cords = font.render(vinner2, True, (255,255,255))
                skjerm.blit(cords, (bredde/2 - 80, 50))

                #stopper ballen
                ball._hastighet_x = 0
                ball._hastighet_y = 0

                #restart ved klikk
                if hendelse.type == pygame.MOUSEBUTTONDOWN:
                    ball._hastighet_x = 7
                    ball._hastighet_y = 7
                    self.poeng_hoyre = 0
                    self.poeng_venstre = 0


            # Viser score
            poeng1 = f'{self.poeng_venstre}'
            cords = font.render(poeng1, True, (255,255,255))
            skjerm.blit(cords, (80, 20))

            poeng2 = f'{self.poeng_hoyre}'
            cords = font.render(poeng2, True, (255,255,255))
            skjerm.blit(cords, (bredde - 90, 20))

            # tegner spillobjektene oppå bakgrunn
            ball.tegn()
            paddle_venstre.tegn()
            paddle_hoyre.tegn()

            # oppdater skjerm
            pygame.display.flip()
            clock.tick(FPS)

Spill().loop()
