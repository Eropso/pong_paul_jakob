import pygame
from ball import Ball
from paddle import Paddle
from spillObjekt import SpillObjekt
pygame.init()
 

bredde, hoyde = 800, 600
hvit = (255, 255, 255)
FPS = 60

skjerm = pygame.display.set_mode(bredde, hoyde)
pygame.display.set_caption('Pong')
