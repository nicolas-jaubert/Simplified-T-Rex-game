import pygame
import random
import time



win = pygame.display.set_mode((750,250))
pygame.display.set_caption("T-Rex game")
horloge = pygame.time.Clock()

fond = pygame.image.load(('image/bg.png'))
T_Rex = pygame.image.load(('image/T-rex.png'))
T_Rex2 = pygame.image.load(('image/T-rex2.png'))
T_Rex3 = pygame.image.load(('image/T-rex3.png'))
T_Rex_bas = pygame.image.load(('image/T-rex_bas.png'))
T_Rex_bas2 = pygame.image.load(('image/T-rex_bas2.png'))
T_Rex_bas3 = pygame.image.load(('image/T-rex_bas3.png'))

pterosauria = pygame.image.load(('image/volant.png'))
pterosauria2 = pygame.image.load(('image/volant2.png'))

C1 = pygame.image.load(('image/cactus1.png'))
C2 = pygame.image.load(('image/cactus2.png'))
C3 = pygame.image.load(('image/cactus3.png'))
C4 = pygame.image.load(('image/cactus4.png'))
C5 = pygame.image.load(('image/cactus5.png'))
C6 = pygame.image.load(('image/cactus6.png'))


img_sol = pygame.image.load(('image/sol.png'))
#police des texte lorsque le joueur a perdu.
font2 = pygame.font.SysFont('Georgia', 50, True)
font3 = pygame.font.SysFont('Garamond', 16, True)


# liste de valeurs, la commande random.choice permet d'en prendre une au hasard.
cactus_liste=[1,2,3,4,5,6]
appa_volant =[850,1300,1750]

