# -*- coding: utf-8 -*-
import var as var
import random
def boss() :
    if var.vague == 5 and var.boss_spawn == False : # si le boss n'a pas spawn et que il s'agit de la vague est 5 (pour voir quel boss faire apparaître)
        var.tab_monstre.append([900,200,"billy",1,100,1000,95,60])  # [coordonnée x , coordonée y , nom du mob , vitesse de vase , vie, score, hitbox axe x, hitbox axe y]
        global img_billy 
        img_billy = loadImage("Billy.png")  # image du boss
        global img_boule
        img_boule = loadImage("boule.png") # image de ses projectiles
        var.boss_spawn = True # le boss a spawn

    
        
def boss_vague() :
    if var.vague == 5 : # si la vague est 5 (pour voir quel boss faire apparaître)
        vie_boss = 1
        for i in range(0,len(var.tab_monstre)): # pour chaque monstres
            if var.tab_monstre[i][2] == "billy" :  # si le monstre est le boss
                image(img_billy,var.tab_monstre[i][0], var.tab_monstre[i][1]) # déplacer l'image sur lui
                vie_boss = var.tab_monstre[i][4] # définir la variable de sa vie restante
                
                if random.randint(0,100) == 5 : # si le nombre aléatoire est 5
                    var.projectile_mob.append([var.tab_monstre[i][0]+5,var.tab_monstre[i][1]+10]) # faire apparaître un projectile
                    
                for projectile in var.projectile_mob : # pour chacun de ses projectiles
                    projectile[0] -= 3 # le déplacer
                    image(img_boule,projectile[0],projectile[1]) # déplacer l'image
                    if var.coords_perso[0] < projectile[0]+30 and var.coords_perso[0] > projectile[0]-30 and var.coords_perso[1] < projectile[1]+30 and var.coords_perso[1] > projectile[1]-30 : #vérifie si le joueur est en collision avec le projectile
                        var.vie -=1 # si oui supprime une vie 
                        var.projectile_mob.remove(projectile) # supprime le projectile
                
        if len(var.tab_monstre) == 0 and var.boss_spawn == True: # si il n'y a plus de monstres et que le boss a déjà spawn
            vie_boss =0 # mettre sa vie à 0
        for monstre in var.tab_monstre: 
            if monstre[2] == "billy" and millis()%5 == 0: # avancer billy plus lentement que les autres mobs
                monstre[0]-= int(monstre[3]) + var.mob_speed 
            elif monstre[2] != "billy": # ancer les autres monstres normal ( car je comptais en rajouter)
                monstre[0]-= int(monstre[3]) + var.mob_speed 
            if (monstre[0]<-50):  # si les monstres sont hors de l'écran
                var.tab_monstre.remove(monstre)
        # vie du boss
        fill(0,0,0)
        rect(149,59,502,7)
        fill(255,0,0)
        rect(150,60,vie_boss*5,5)
        if vie_boss == 0 : # si le boss est mort
            var.vague_boss.remove(5) # supprimer cette vague de boss
            var.boss_spawn = False
        
            
