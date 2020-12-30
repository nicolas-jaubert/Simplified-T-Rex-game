import pygame

pygame.init()

import time
import random

# on importe les valeurs de base, les images, puis les classes.
from parametres import *
from classes import *


def rejoueOuQuitte():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYUP:
            continue
        return event.key
    return None

def perdu():

    texte2 = font2.render("GAME OVER", 1, (0,0,0))
    texte3 = font3.render("Appuyer sur une touche du clavier pour rejouer",1,(0,0,0))
    win.blit(texte3, (200, 130))
    win.blit(texte2, (200, 70))

    pygame.display.update()
    #on laisse quelques secondes au joueur, pour que ça ne recommence pas directement.
    time.sleep(3)

    while rejoueOuQuitte()== None :
        horloge.tick()


    principale()

def principale():
    score=0

    def dessinefenetre():
        win.blit(fond, (0,0))
        texte = font1.render(str(score), 1, (0,0,0))
        win.blit(texte, (715, 10))
        decor.draw(win)
        obst1.draw(win)
        obst2.draw(win)
        obst3.draw(win)
        dino.draw(win)


        pygame.display.update()

    #police pour le score.
    font1 = pygame.font.SysFont('Helvetica', 20, True)
    dino = player(50, 200)
    obst1 = cactus(2000,188)
    obst2 = cactus2(2450,188)
    obst3 = pterosaure(18875,170)
    decor = sol(0,231)
    fonctionne = True
    scoredebit=3
    score_seuil = 200
    ecart = 0

    while fonctionne:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fonctionne = False

        keys = pygame.key.get_pressed()

        if dino.saute == False:
            dino.vit_y=-8
        #lorsque le joueurs appuie sur flèche du haut.
            if keys[pygame.K_UP] and dino.y==200:
                if dino.bas == False:
                    dino.saute = True
        else:
            if dino.sautCompte >=0:
                dino.vit_y= dino.sautCompte *2.1
                dino.sautCompte -= 1
            else:
                dino.saute = False
                dino.sautCompte = 10

        #lorsque le joueur appuie sur flèche du bas.
        if keys[pygame.K_DOWN]:
            dino.bas = True
            dino.vit_y += -15

        else:
            dino.bas = False


        dino.y -= dino.vit_y

        # on défini un sol en 200.
        if dino.y>200:
            dino.y=200

        decor.x -= decor.vit
        obst1.x -= obst1.vit
        obst2.x -= obst2.vit
        obst3.x -= obst3.vit
        #réapparition des obstacles et du sol.
        if decor.x < -3000:
            decor.x = 0

        if obst1.x<-50:
            obst1.valeur = random.choice(cactus_liste)
            obst1.x=850-ecart

        if obst2.x<-50:
            obst2.valeur = random.choice(cactus_liste)
            obst2.x=850-ecart

        if obst3.x<-50:
            obst3.x=random.choice(appa_volant)-ecart

        # les collisions avec les obtacles (5 et 8 sont des valeurs pour que les hitboxes soient plus tolérentes).
        if   dino.x+dino.l>obst1.x+8 and dino.x<obst1.x+obst1.l-8:
            if dino.y+dino.h>188+obst1.difh+5:
                perdu()


        if   dino.x+dino.l>obst2.x+8 and dino.x<obst2.x+obst2.l-8:
            if dino.y+dino.h>188+obst2.difh+5 :
                perdu()



        if dino.x+dino.l>obst3.x+10 and  dino.x<obst3.x+obst3.l-10:
                if dino.y+dino.dif_h<obst3.y+obst3.h and dino.y+dino.h>obst3.y+5:
                        perdu()

        #gestion du score
        if scoredebit>0:
            scoredebit-=1
        else:
            scoredebit+=3
            score+=1
        #Le jeu s'accélère au fur et à mesure que le score augmente, jusqu'à un certain point.
        if score>score_seuil and score <40000:
            decor.vit +=0.2
            obst1.vit +=0.2
            obst2.vit +=0.2
            obst3.vit +=0.2
            ecart += 5
            score_seuil +=200




        dessinefenetre()
        horloge.tick(60)

principale()
pygame.quit()
quit()