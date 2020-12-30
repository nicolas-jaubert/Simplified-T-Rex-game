import pygame
import time
import random

from parametres import *



class cactus (object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vit = 8 # vitesse de défilement des cactus.
        self.valeur = random.choice(cactus_liste)
        self.l = 0 #longueur des différents cactus.
        self.difh=0 # différence de hauteur en fonction des différents cactus.

    def draw(self,win):
        # en fonction de la valeur choisi on lui donne un des 6 cactus avce ces paramètres.
        if self.valeur == 1:
            self.l = 30
            self.difh= 2
            win.blit(C1, (self.x,self.y))
        elif self.valeur == 2:
            self.l = 20
            self.difh= 16
            win.blit(C2, (self.x,self.y))
        elif self.valeur == 3:
            self.l = 61
            self.difh = 2
            win.blit(C3, (self.x,self.y))
        elif self.valeur == 4:
            self.l = 42
            self.difh= 16
            win.blit(C4, (self.x,self.y))
        elif self.valeur == 5:
            self.l = 63
            self.difh= 16
            win.blit(C5, (self.x,self.y))
        elif self.valeur == 6:
            self.l = 92
            self.difh = 2
            win.blit(C6, (self.x,self.y))
#exactement pareil que la class cactus.
class cactus2 (object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vit = 8
        self.valeur = random.choice(cactus_liste)
        self.l = 30
        self.difh=0

    def draw(self,win):
        if self.valeur == 1:
            self.l = 30
            self.difh= 2
            win.blit(C1, (self.x,self.y))
        elif self.valeur == 2:
            self.l = 20
            self.difh= 16
            win.blit(C2, (self.x,self.y))
        elif self.valeur == 3:
            self.l = 61
            self.difh = 2
            win.blit(C3, (self.x,self.y))
        elif self.valeur == 4:
            self.l = 42
            self.difh= 16
            win.blit(C4, (self.x,self.y))
        elif self.valeur == 5:
            self.l = 63
            self.difh= 16
            win.blit(C5, (self.x,self.y))
        elif self.valeur == 6:
            self.l = 92
            self.difh = 2
            win.blit(C6, (self.x,self.y))


class pterosaure(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vit= 8 # sa vitesse.
        self.img = 8 # pour son animation.
        self.h = 45 #sa hauteur.
        self.l = 47 # sa largeur.

    def draw(self, win):

        if self.img  >4:#pendant 3 frames on dessine l'image 1.
            win.blit(pterosauria, (self.x,self.y))
            self.img -=1
        elif self.img >0:# puis pendant 4 frames la deuxième.
            win.blit(pterosauria2, (self.x,self.y))
            self.img -=1
        elif self.img ==0:# à nouveau la 1ère pendant une frame.
            win.blit(pterosauria, (self.x,self.y))
            self.img +=8



class sol(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vit = 8 # sa vitesse.


    def draw(self,win):
        win.blit(img_sol, (self.x,self.y))


class player(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.saute = False
        self.bas = False
        self.sautCompte = 10 # pendant combien de frames le dinosaure saute.
        self.img = 8
        self.img_bas=9
        self.h = 44
        self.l = 40
        self.dif_h = 0 # la différence de hauteur lorsqu'il se baisse.
        self.vit_y = 0


    def draw(self, win):
            #quand il se baisse.
            if self.bas:
                self.h = 29
                self.l = 58
                self.dif_h = 19
                if self.img_bas >6: #même principe que pour le ptérosaure.
                    win.blit(T_Rex_bas, (self.x,self.y))
                    self.img_bas-=1
                elif self.img_bas>3:
                    win.blit(T_Rex_bas2, (self.x,self.y))
                    self.img_bas-=1
                elif self.img_bas>0:
                    win.blit(T_Rex_bas3, (self.x,self.y))
                    self.img_bas-=1
                elif self.img_bas==0:
                    win.blit(T_Rex_bas, (self.x,self.y))
                    self.img_bas+=9
            #quand il saute.
            elif self.saute:
                self.dif_h = 0
                self.h = 44
                self.l = 40
                win.blit(T_Rex, (self.x,self.y))
            else: #quand il ne fait aucune des deux actions (quand il court).
                self.h = 44
                self.l = 40
                self.dif_h = 0

                if self.img >4:
                    win.blit(T_Rex2, (self.x,self.y))
                    self.img-=1
                elif self.img>0:
                    win.blit(T_Rex3, (self.x,self.y))
                    self.img-=1
                elif self.img==0:
                    win.blit(T_Rex2, (self.x,self.y))
                    self.img+=8