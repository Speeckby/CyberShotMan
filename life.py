# -*- coding: utf-8 -*-
import var as var
def init_vie() :
    global img_coeur
    img_coeur = loadImage("coeur.png")
    global img_hit
    img_hit = loadImage("hit.png")
    
def afficher_coeurs():
    if var.vie == 3 and var.start : # afficher 3 coeurs
        image(img_coeur,690,20)
        image(img_coeur,730,20)
        image(img_coeur,770,20)
    elif var.vie == 2 and var.start: # afficher 2 coeurs
        image(img_hit,690,20)
        image(img_coeur,730,20)
        image(img_coeur,770,20)
    elif var.vie == 1 and var.start: # afficher 1 coeurs
        image(img_hit,690,20)
        image(img_hit,730,20)
        image(img_coeur,770,20)
    elif var.start :
        image(img_hit,690,20)
        image(img_hit,730,20)
        image(img_hit,770,20)
