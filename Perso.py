# -*- coding: utf-8 -*-
import var as var
import var_save as vars
from life import afficher_coeurs

def init_perso() :
    global img_perso
    img_perso = loadImage("Perso.png")
    global img_death
    img_death =loadImage("tombe.png")
    
def afficher_perso():
    if var.vie > 0 : #si joueur en vie = personnage
        image(img_perso,var.coords_perso[0],var.coords_perso[1])
    elif var.start : #sinon et si le jeu à commencé = tombe
        image(img_death,var.coords_perso[0],var.coords_perso[1])
    
def deplacer_perso():
    if var.coords_perso[1]<115 : # si le joueur touche la bannière
        var.up = False #il ne peut plus monter
    if var.coords_perso[1]>337 :  # si le joueur est en bas
        var.down = False # il ne peut plus descendre
        
        
    if (var.down) and var.vie > 0: # si le joueur est en vie et qu'il veut descendre 
        var.coords_perso[1] += 5 
    if (var.up) and var.vie > 0:  # si le joueur est en vie et qu'il veut monter 
        var.coords_perso[1] -= 5

def mort():
    for monstre in var.tab_monstre: # pour chaques montres en vies 
        monstre_coords_x = [monstre[0]+monstre[6],monstre[0]-monstre[6]] # definir la hitbox x
        monstre_coords_y = [monstre[1]+monstre[7]+45,monstre[1]-monstre[7]-45] # definir la hitbox y avec la taille du joueur
        if var.coords_perso[0] < monstre_coords_x[0] and var.coords_perso[0] > monstre_coords_x[1] and var.coords_perso[1] < monstre_coords_y[0] and var.coords_perso[1] > monstre_coords_y[1] : #vérifie si le joueur est en collision avec un monstre
            if monstre[2] == "billy" :
                var.vie -= 3 # tues le joueur si c'est un boss
            else :
                var.vie -= 1 # enlève une vie
                var.tab_monstre.remove(monstre) #tue le monstre
            if var.vie == 0 and var.score > vars.best_score : #si le joueur est mort et que il a fait son meilleur score
                fichier = open("var_save.py", "w") #ouvre le fichier var_save.py
                fichier.write("best_score = {}".format(var.score)) #remplace le meilleur score dedans pour qu'il soit sauvegardé même après que le jeu soit fermé
                fichier.close() # ferme le fichier
                var.best_score = var.score #enregistre le best_score dans la mémoire car sinon le best_score du jeu s'actualise pas 
