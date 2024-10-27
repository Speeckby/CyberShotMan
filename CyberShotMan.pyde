from Perso import *
from Bullet import *
from Monstre import *
from life import *
import var as var
from interface import *
import var_save as vars



def setup():
    size (800, 400) # définition de la taille de la fenêtre de l'application
    imageMode(CENTER) # on affichera les images en précisant les coords du centre
    init_perso() 
    init_bullets()
    init_monstre()
    init_vie()
    var.best_score = vars.best_score # importe le meilleur score
def draw():
    desert = loadImage("desert.png") # background
    background(desert)
    imageMode(CENTER)
    #score + interface (hud)
    interface() #affiche l'interface du jeu 
    afficher_coeurs() #affiche les coeurs
    
    #perso
    afficher_perso() #affiche le personnage
    deplacer_perso() #permet le déplacement du personnage
    mort() #permet la mort et la perte de vie du personnage 
    
    #balle
    afficher_bullets() #affiche les balles
    deplacer_bullets() #déplace les balles
    
    #monstre 
    spawn() # permet le spawn de mobs
    afficher_monstre() #affiche les mobs
    deplacer_monstre() # déplace les mobs
    tuer_monstre() #permet de tuer les monstres
# configuration des touches

def keyPressed() :
    if key == "z" or key == "Z": var.up = True
    if key == "s" or key == "S": var.down = True
    if key == " " : 
        tirer(var.coords_perso)

def keyReleased():
    if (key == "z" or key == "Z"): var.up = False
    if (key == "s" or key == "S"): var.down = False
