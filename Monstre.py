# -*- coding: utf-8 -*-
import var as var
from Boss import *

def init_monstre():
    global img_monstre
    img_monstre = loadImage("Monstre.png")
    global img_slime
    img_slime = loadImage("slime.png")

def afficher_monstre():
    for i in range(0,len(var.tab_monstre)) :
        if var.tab_monstre[i][2] == "slime": # si le monstre est un slime
            image(img_slime,var.tab_monstre[i][0], var.tab_monstre[i][1]) 
        elif var.tab_monstre[i][2] == "gobelin" : # si le monstre est un gobelin
            image(img_monstre,var.tab_monstre[i][0], var.tab_monstre[i][1])
        
        
def deplacer_monstre():
    if not var.vague in var.vague_boss : # si c'est pas une vague de boss
        for monstre in var.tab_monstre:
            monstre[0]-= int(monstre[3]) + var.mob_speed #déplace le mob en fonction de sa caractéristique vitesse associée
            if (monstre[0]<-50): 
                var.tab_monstre.remove(monstre) # tues le monstre si il est trop à gauches
    else :
        boss_vague() # sinon lancer une vague de bosss

def spawn():
    if len(var.tab_monstre) == 0 and var.vie > 0 : # si tout les monstres de la vague sont tués et le joueur est en vie
        if var.vague not in var.vague_boss : #si ce n'est pas la vague d'un boss
            if var.nbr_monstre_total < 15 : # si il y a moins de 15 monstres  pour éviter d'avoir trop de monstres
                var.nbr_monstre_total += 1 # rajouter un monstre à la vague
            var.vague+=1 
            if var.mob_speed < 5 and var.vague%3 == 0 and var.vague not in var.vague_boss : # Augmente la rapidité des monstres jusqu'à un certain moment et une vague / 2
                var.mob_speed +=1  #augmente le speed
            for monstre in range(0,var.nbr_monstre_total) :
                taux =random.randint(0,10)
                if taux == 1 and var.vague > 5 and var.vague not in var.vague_boss: #  à partir de la vague 5, il y a 10% de chances qu'un monstre soit un slime
                    var.tab_monstre.append([int(random.randint(850,1700)),int(random.randint(100,350)),"slime",1,5,100,78,59]) # [coordonnée x , coordonée y , nom du mob , vitesse de vase , vie, score, hitbox axe x, hitbox axe y]
                elif var.vague not in var.vague_boss :
                    var.tab_monstre.append([int(random.randint(850,1700)),int(random.randint(100,350)),"gobelin",3,1,10,37,37]) # [coordonnée x , coordonée y , nom du mob , vitesse de vase , vie, score, hitbox axe x, hitbox axe y]
        else :
            boss() # sinon faire spawn le boss
            
def tuer_monstre() :
    for bullet in var.tab_bullets:
        for monstre in var.tab_monstre:
            monstre_coords_x = [monstre[0]+monstre[6],monstre[0]-monstre[6]] # définie les caractéristiques des monstres dans l'axe x de l'hitbox
            monstre_coords_y = [monstre[1]+monstre[7],monstre[1]-monstre[7]] # définie les caractéristiques des monstres dans l'axe y de l'hitbox
            if bullet[0] < monstre_coords_x[0] and bullet[0] > monstre_coords_x[1] and bullet[1] < monstre_coords_y[0] and bullet[1] > monstre_coords_y[1] : # vérifie collision balle avec le / les monstres
                try : #try = évite une erreur pour laquelle je n'avais pas trouvé de solution
                    var.tab_bullets.remove(bullet) # supprimer la balle
                    monstre[4] -= 1 # enlever 1 pv au monstre
                    if monstre[4] ==0 : # si le monstre a plus de vie
                        var.tab_monstre.remove(monstre) # le tuer (supprimer)
                        var.score += monstre[5] # rajouter le score associé au monstre
                except :
                    pass
    if var.vie <= 0 : #quand le joueur est mort les monstres et balles meurts
        var.tab_monstre = []
        var.tab_bullets = []
