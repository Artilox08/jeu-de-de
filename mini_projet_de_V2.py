from turtle import*
from random import randint

def nombre_aleatoire(n): # Denevanne
    """
    Fonction renvoyant un entier aléatoire compris entre 1 et n.
    
    Argument d'entrée:
    n : nombre maximum du tirage aléatoire
        type : entier
        
    Sortie :
    nombre : nombre choisi alétoirement
        type : entier
    """
    ## Ecrivez ici le code de la fonction
    return randint(1,n)

def couleur_aleatoire(): # Denevanne
    """ Fonction renvoyant un tuple de 3 nombres entiers compris entre 0 et 255
    Ce tuple correspond à une couleur codée en RVB. Par exemple rouge (255,0,0),
    vert (0,255,0), bleu (0,0,255)
    
    Argument d'entrée:
    aucun
        
    Sortie :
    couleur : un tuple composé de trois entiers compris entre 0 et 255
        type : tuple
    """
    ## Ecrivez ici le code de la fonction
    a = nombre_aleatoire(255)
    b = nombre_aleatoire(255)
    c = nombre_aleatoire(255)
    return(a,b,c)

def comparer_chiffre(chiffre1, chiffre2, chiffre3): # Matt
    """ Fonction comparant trois chiffres décimaux et renvoyant le plus grand 
    nombre composé par ces trois chiffres
    
    Arguments d'entrée:
    chiffre1, chiffre2, chiffre3 : chiffre décimaux
        type : entier
        
    Sortie :
    résultat : un nombre décimal
        type : entier
    
    Exemples d'exécution
    --------------------
    >>> comparer_chiffre(1, 5, 3)
    531
    >>> comparer_chiffre(5, 1, 1)
    511
    >>> comparer_chiffre(1, 1, 1)
    111
    >>> comparer_chiffre(1, 3, 3)
    331
    """
    ## Ecrivez ici le code de la fonction

    combi1 = chiffre1 * 100 + chiffre2 * 10 + chiffre3
    combi2 = chiffre1 * 100 + chiffre3 * 10 + chiffre2
    combi3 = chiffre2 * 100 + chiffre1 * 10 + chiffre3
    combi4 = chiffre2 * 100 + chiffre3 * 10 + chiffre1
    combi5 = chiffre3 * 100 + chiffre1 * 10 + chiffre2
    combi6 = chiffre3 * 100 + chiffre2 * 10 + chiffre1



    if combi1 >= combi2 and combi1 >= combi3 and \
       combi1 >= combi4 and combi1 >= combi5 and \
       combi1 >= combi6:
        return combi1
    elif combi2 >= combi3 and combi2 >= combi4 and \
         combi2 >= combi5 and combi2 >= combi6:
        return combi2
    elif combi3 >= combi4 and combi3 >= combi5 and \
         combi3 >= combi6:
        return combi3
    elif combi4 >= combi5 and combi4 >= combi6:
        return combi4
    elif combi5 >= combi6:
        return combi5
    else:
        return combi6


def tracer_carre(x, y, longueur): # Denevanne
    """ Procédure tracant un carré dont la longueur d'un 
    coté est 'longueur'. Ce tracé s'effecue à partir des coordonnées x,y du 
    point inférieur gauche de ce carré."""
    ## Ecrivez ici le code de la fonction
    
    penup()
    goto(x,y)
    pendown()
    colormode(255)
    fillcolor(couleur_aleatoire())
    begin_fill()
    for i in range(4):
         forward(longueur)
         left(90)
    end_fill()


def tracer_point(x, y, longueur): # Denevanne
    """Procédure tracant un point aux coordonnés x,y. Ce point possède un 
    rayon égal à longueur/5."""
    ## Ecrivez ici le code de la fonction
    goto(x, y)
    dot(longueur/5, "black")


def afficher_message(x, y, texte): # Matt 
    """
    Procédure affichant le message 'texte' aux coordonnés x,y.
    """
    ## Ecrivez ici le code de la fonction
    goto(x, y)
    write(texte, align="center", font=("Georgia", 27, "normal"))

def afficher_un(x, y, longueur): # Matt
    """
    Procédure affichant le point milieu d'un dé, dont la longueur d'un 
    coté est 'longueur'. Ce tracé s'effecue à partir des coordonnées x,y du 
    point inférieur gauche de ce dé.
    """
    ## Ecrivez ici le code de la fonction
    penup()
    tracer_point(x+(longueur/2),y+(longueur/2), longueur)
       

def afficher_diagonale_1(x, y, longueur): # Denevanne
    """
    Procédure affichant les deux points de la diagonale 1 d'un dé, dont la longueur 
    d'un coté est 'longueur'. Ce tracé s'effecue à partir des coordonnées x,y du 
    point inférieur gauche de ce dé.
    """
    ## Ecrivez ici le code de la fonction
    penup()
    tracer_point(x+(3/4*longueur), y+(3/4*longueur), longueur)
    tracer_point(x+(1/4*longueur), y+(1/4*longueur), longueur)

def afficher_diagonale_2(x, y, longueur): # Denevanne
    """
    Procédure affichant les deux points de la diagonale 2 d'un dé, dont la longueur 
    d'un coté est 'longueur'. Ce tracé s'effecue à partir des coordonnées x,y du 
    point inférieur gauche de ce dé.
    """
    ## Ecrivez ici le code de la fonction
    penup()
    tracer_point(x+(1/4*longueur), y+(3/4*longueur), longueur)
    tracer_point(x+(3/4*longueur), y+(1/4*longueur), longueur)

def afficher_horizontale_milieu(x, y, longueur): # Matt
    """
    Procédure affichant les deux points de l'horizontale du milieu d'un dé, dont la longueur 
    d'un coté est 'longueur'. Ce tracé s'effecue à partir des coordonnées x,y du 
    point inférieur gauche de ce dé.
    """
    ## Ecrivez ici le code de la fonction
    penup()
    tracer_point(x+(1/4*longueur), y+(1/2*longueur), longueur)
    tracer_point(x+(3/4*longueur), y+(1/2*longueur), longueur)

def choisir_face_a_afficher(x, y, lance, longueur): # Matt
    """
    Procédure affichant la face d'un dé correpondant à "lance", dont la longueur 
    d'un coté est 'longueur'. Ce tracé s'effecue à partir des coordonnées x,y du 
    point inférieur gauche de ce dé.
    """
    ## Ecrivez ici le code de la fonction
    
    if lance == 1:
        tracer_carre(x, y, longueur)
        afficher_un(x, y, longueur)
        
    elif lance == 2:
        tracer_carre(x, y, longueur)
        afficher_diagonale_1(x, y, longueur)
        
    elif lance == 3:
        tracer_carre(x, y, longueur)
        afficher_un(x, y, longueur)
        afficher_diagonale_1(x, y, longueur)
        
    elif lance == 4:
        tracer_carre(x, y, longueur)
        afficher_diagonale_1(x, y, longueur)
        afficher_diagonale_2(x, y, longueur)
        
    elif lance == 5:
        tracer_carre(x, y, longueur)
        afficher_diagonale_1(x, y, longueur)
        afficher_diagonale_2(x, y, longueur)
        afficher_un(x, y, longueur)
        
    elif lance == 6:
        tracer_carre(x, y, longueur)
        afficher_diagonale_1(x, y, longueur)
        afficher_diagonale_2(x, y, longueur)
        afficher_horizontale_milieu(x, y, longueur)



def lancer_jeu(): # Ensemble
    """ Programme prinicipal de la gestion du jeu"""
    ## Ecrivez ici le code de la fonction
    penup()
    
    nom_j1 = textinput("Nom joueur 1", "Veuillez saisir le nom du joueur 1.")
    nom_j2 = textinput("Nom joueur 2", "Veuillez saisir le nom du joueur 2.")
    
    
    afficher_message(-200, 100, nom_j1)
    afficher_message(200, 100, nom_j2)
    
    chiffre_j1_1 = nombre_aleatoire(6) # 3 chiffres du joueurs 1 aléatoires
    chiffre_j1_2 = nombre_aleatoire(6)
    chiffre_j1_3 = nombre_aleatoire(6)
    
    score_j1 = comparer_chiffre(chiffre_j1_1, chiffre_j1_2, chiffre_j1_3) # Score du joueur 1

    
    choisir_face_a_afficher(-285, 20, chiffre_j1_1, 40) # dés du joueur 1
    choisir_face_a_afficher(-225, 20, chiffre_j1_2, 40)
    choisir_face_a_afficher(-165, 20, chiffre_j1_3, 40)
    
    afficher_message(-240, -70, "Score:") # Afficher "score:" pour le joueur 1
    afficher_message(-150, -70, score_j1) # Afficher le score du joueur 1
    
    
    
    chiffre_j2_1 = nombre_aleatoire(6) # 3 chiffres du joueurs 2 aléatoires
    chiffre_j2_2 = nombre_aleatoire(6)
    chiffre_j2_3 = nombre_aleatoire(6)
    
    score_j2 = comparer_chiffre(chiffre_j2_1, chiffre_j2_2, chiffre_j2_3) # Score du joueur 2
    
    
    choisir_face_a_afficher(115, 20, chiffre_j2_1, 40) # dés du joueur 2
    choisir_face_a_afficher(175, 20, chiffre_j2_2, 40)
    choisir_face_a_afficher(235, 20, chiffre_j2_3, 40)

    afficher_message(150, -70, "Score:") # Afficher "score:" pour le joueur 2
    afficher_message(240, -70, score_j2) # Afficher le score du joueur 2
    
    
    if score_j1 > score_j2:
        afficher_message(0, -150, nom_j1+" a gagné!")
    
    elif score_j2 > score_j1:
        afficher_message(0, -150, nom_j2+" a gagné!")


    reset = textinput("Rejouer?","Souhaitez vous rejouer? Tapez ""non"" pour fermer et ""oui"" pour rejouer.")
    
    if reset == "non" or reset == "Non" or reset == "NON":
        bye()
    elif reset == "oui" or reset == "Oui" or reset == "OUI":
        clear()
        lancer_jeu()
    


TurtleScreen._RUNNING = True
setup(width=1.0, height=1.0)
hideturtle()
speed("fastest")
up()
## testez ici vos fonctions
lancer_jeu()
