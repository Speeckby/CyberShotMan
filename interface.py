# -*- coding: utf-8 -*-
import var as var
import var_save as vars

def interface():
    if not var.start and var.vie == 0: #interface quand le jeu a pas commencé
        # bouton
         fill("#1AA7EC") # couleur
         stroke(255,255,0)
         strokeWeight(5)
         rect(300,180, 200, 50)
         textSize(30)
         fill(255,255,0) # couleur
         text("JOUER",355,215)
         if mousePressed and (mouseButton == LEFT) and mouseX < 500 and mouseX > 300 and mouseY < 230 and mouseY > 180 : #si il y a un clic dans le rectangle du bouton
             var.vie = 3
             var.start = True
             var.vie = 3
    if var.start and var.vie > 0 : #jeu en cours
        fill("#1AA7EC") #couleur
        stroke(0,0,0) #couleur bordure
        strokeWeight(1) #taille bordure
        rect(-1,0, 801, 50) #rectangle en haut de l'écran pour afficher les stats en directs (vie, score ...)
        
        #score +best
        fill(255,255,0) # couleur
        textSize(30) #taille du texte 
        text("Score : {}".format(var.score),10,35)# affiche le score
        text("Record : {}".format(var.best_score),200,35)# affiche le best score
        
        # vague
        fill(255,255,0) # couleur
        textSize(30) #taille du texte 
        text("Vague : {}".format(var.vague),450,35)# affiche la vague
    if var.start and var.vie <= 0 : #interface après la mort
        fill("#1AA7EC")
        stroke(255,255,0)
        strokeWeight(1)
        rect(300,0, 501, 250)
        
        #score
        fill(255,255,0) # couleur
        textSize(30) #taille du texte 
        text("Score : {}".format(var.score),310,35)
        text("Meilleur Score : {}".format(var.best_score),310,75)
        
        
        
        #bouton rejouer
        fill("#1AA7EC") # couleur
        stroke(255,255,0)
        strokeWeight(4)
        rect(450,180, 200, 50)
        textSize(30)
        fill(255,255,0)
        text("REJOUER",490,215)
        if mousePressed and (mouseButton == LEFT) and mouseX < 650 and mouseX > 450 and mouseY < 230 and mouseY > 180 : #si il y a un clic dans le rectangle du bouton
            var.vie = 3
            var.nbr_monstre_total = 4 
            var.score = 0
            var.mob_speed = 0
            var.vague = 0
        
