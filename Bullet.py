# -*- coding: utf-8 -*-
import var as var

def init_bullets():
    global img_bullets
    img_bullets = loadImage("Bullet.png")

def afficher_bullets():
    for i in range(0,len(var.tab_bullets)) : # pour chaque balles
        image(img_bullets,var.tab_bullets[i][0], var.tab_bullets[i][1])

def tirer(tab_dimensions):
    if len(var.tab_bullets) < 5 and var.vie > 0: # limite le nombre de balle a 5 quand le joueur est en vie 
        var.tab_bullets.append([tab_dimensions[0]+35,tab_dimensions[1]]) # fait apparaitre la balle sur le pistolet
        
def deplacer_bullets():
    for bullets in var.tab_bullets:
        bullets[0]+=5 # vitesse des balles 
        if (bullets[0]>800): 
            var.tab_bullets.remove(bullets) # supprime les balles hors de l'écran
