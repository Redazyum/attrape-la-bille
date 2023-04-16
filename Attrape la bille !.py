########################################################################################################################
########## Programme réalisé par Nathalie-Hélène Lefort-Martin et Antoine Chevalier
########## Dans le cadre de l'enseignement de spécialité Numérique et Sciences Informatiques en Terminale
########## Finalisé le 05/06/2021
########################################################################################################################

########################################################################################################################
########## Importation des modules nécessaires au fonctionnement du jeu
########################################################################################################################

import pygame
import random
import os

########################################################################################################################
########## Définition des variables et création des objets pour le jeu
########################################################################################################################

# Initialisation des polices d'écritures
pygame.font.init()

# Initialisation de la fenêtre
tailleFenetre = longueur, hauteur = 950, 650
surf = pygame.display.set_mode(tailleFenetre)  # surface de taille 950x650
pygame.display.set_caption('Attrape la bille')

# Création de la demande de pseudo
vert = (40, 230, 120)
bleu = (40, 120, 230)
pseudo = ""
police= pygame.font.SysFont('Comic Sans MS,Arial', 30)
demandePseudo = police.render('Entrez votre pseudo : ', True, bleu)
demandePseudoRect = demandePseudo.get_rect(center=(longueur//2, hauteur//2))
entreeUtilisateur = police.render(pseudo, True, vert)
entreeUtilisateurRect = entreeUtilisateur.get_rect(midtop=demandePseudoRect.midbottom)

# Chargement du fond du menu
fondMenu = pygame.image.load(os.path.join('data', 'menu_illustration.png'))  # importation de l'imageillustration

# Chargement de la dernière image créée en jeu
derniereImage = pygame.image.load(os.path.join('data', 'derniere image.png'))
derniereImage = pygame.transform.scale(derniereImage, (360, 246))

# Définition de variables
boucleDemandePseudo = True
boucleMenu = False  # Création de la variable booléenne pour la boucle du Menu
boucleDecompte = 0  # Création du compteur pour la boucle de décompte (nulle pour ne pas lancer le décompte)
boucleJeu = 0  # Création du compteur pour la boucle de jeu (nulle pour ne pas lancer le jeu)
boucleImage = False # Création de la variable booléenne pour la boucle de l'affichage de l'image créée à la fin du jeu
boucleScoreboard = False # # Création de la variable booléenne pour la boucle du Scoreboard
couleurFond = 255, 255, 255  # Couleur du fond en jeu
vitessesNiveauFacile = [-7, -6, -5, 5, 6, 7]
listeCoordonneesCliquees = []  # Liste des coordonnées où la bille est cliquée
clock = pygame.time.Clock()  # Définition de la clock pour avoir la même vitesse sur tout les ordinateurs
nombreBillesCliquees = 0  # Définition du compteur de billes cliquées
chaineBillesCliquees = 0  # Définition du compteur de chaîne de billes cliquées

# Définition de la taille des bouton jouer, galerie
l_boutton_jouer = 105  # on definit la largeur du bouton jouer
h_boutton_jouer = 80  # on définit la hauteur du bouton jouer
l_boutton_galerie = 100  # on definit la largeur du bouton galerie
h_boutton_galerie = 70  # on définit la hauteur du bouton galerie

# Création des zone des boutons
boutton_jouer = pygame.Surface((l_boutton_jouer, h_boutton_jouer))  # on créer la zone du bouton jouer
boutton_galerie = pygame.Surface((l_boutton_galerie, h_boutton_galerie))  # on créer la zone du bouton galerie

# Création du bouton jouer
bouton_jouer_pos = boutton_jouer.get_rect()  # on recupère le rectangle pour creer le bouton
bouton_jouer_pos.center = (545, 465)  # on place le bouton selon (x,y) le centre du rectangle

# Création du bouton galerie
bouton_galerie_pos = boutton_galerie.get_rect()  # on recupère le rectangle pour creer le bouton
bouton_galerie_pos.center = (670, 140)  # on place le bouton selon (x,y) le centre du rectangle

# Création du bouton suivant
boutonSuivant = pygame.image.load(os.path.join('data', 'bouton_suivant.png'))
boutonSuivant = pygame.transform.scale(boutonSuivant, (100, 100))
boutonSuivantRect = boutonSuivant.get_rect()
boutonSuivantRect.bottomright = (950, 650)

# Création des objets pour le décompte
decompteUn = pygame.image.load(os.path.join('data', 'decompte', '1.png'))       #
decompteDeux = pygame.image.load(os.path.join('data', 'decompte', '2.png'))     # On importe les images du décompte
decompteTrois = pygame.image.load(os.path.join('data', 'decompte', '3.png'))    #
decompteUnRect = decompteUn.get_rect()          #
decompteDeuxRect = decompteDeux.get_rect()      # On créé un rectangle correspondant à chaques images
decompteTroisRect = decompteTrois.get_rect()    #
decompteUnRect.center = longueur//2, hauteur//2     #
decompteDeuxRect.center = longueur//2, hauteur//2   # On Définit le centre des rectangles au centre de la fenêtre
decompteTroisRect.center = longueur//2, hauteur//2  #

# Création de la bille
vitesse = [8, 8]
bille = pygame.image.load(os.path.join('data', 'bille.png'))
bille = pygame.transform.scale(bille, (100, 100))
billeRect = bille.get_rect()

# Création du compteur en jeu
compteur = pygame.font.SysFont('Comic Sans MS', 70)
secondes = 0

# Importation des tâches pour le rendu finale
tacheUn = pygame.image.load(os.path.join('data', 'taches', 'T_1.png'))
tacheDeux = pygame.image.load(os.path.join('data', 'taches', 'T_2.png'))
tacheTrois = pygame.image.load(os.path.join('data', 'taches', 'T_3.png'))
tacheQuatre = pygame.image.load(os.path.join('data', 'taches', 'T_4.png'))
tacheCinq = pygame.image.load(os.path.join('data', 'taches', 'T_5.png'))
tacheSix = pygame.image.load(os.path.join('data', 'taches', 'T_6.png'))
tacheSept = pygame.image.load(os.path.join('data', 'taches', 'T_7.png'))
tacheHuit = pygame.image.load(os.path.join('data', 'taches', 'T_8.png'))
tacheNeuf = pygame.image.load(os.path.join('data', 'taches', 'T_9.png'))
tacheDix = pygame.image.load(os.path.join('data', 'taches', 'T_10.png'))
listeTaches = [tacheUn, tacheDeux, tacheTrois, tacheQuatre,tacheCinq, tacheSix, tacheSept,tacheHuit, tacheNeuf, tacheDix]  # Création d'une liste d'objet

# Ouverture des fichiers score et meilleur joueur
scoreFichier = open(os.path.join('data', 'score.txt'), 'r')
scoreLu = scoreFichier.readlines() # Lit le fichier ligne par ligne
meilleurScore = int(scoreLu[0]) # Défini le meilleur score comme étant celuis inscrit dans le fichier
meilleurJoueurFichier = open(os.path.join('data', 'meilleur joueur.txt'))
pseudoLu = meilleurJoueurFichier.readlines()  # Lit le fichier ligne par ligne
meilleurJoueur = str(pseudoLu[0])
scoreFichier.close()
meilleurJoueurFichier.close()

# Création du tableau de score
meilleurScoreAffichage = police.render("Meilleur Score : {}".format(meilleurScore), True, (0, 0, 0))
meilleurScoreAffichageRect = meilleurScoreAffichage.get_rect(center=(longueur//2, hauteur//2))
meilleurJoueurAffichage = police.render("Meilleur joueur : {}".format(meilleurJoueur), True,(0, 0, 0))
meilleurJoueurAffichageRect = meilleurJoueurAffichage.get_rect(midbottom=meilleurScoreAffichageRect.midtop)

########################################################################################################################
########## Déroulement du jeu
########################################################################################################################

# Demande au joueur d'entrer un pseudo
while boucleDemandePseudo:

    # Vérification des événements pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Permet au joueur de quitter le jeu
            boucleDemandePseudo = False
            break

        elif event.type == pygame.KEYDOWN:  # Permet de quitter cette boucle et lance le menu en appuyant sur entrée
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                boucleDemandePseudo = False
                boucleMenu = True
                break
            elif event.key == pygame.K_BACKSPACE:  # Permet de supprimer des caractères avec retour arrière
                pseudo = pseudo[:-1]
            else:
                pseudo += event.unicode
            entreeUtilisateur = police.render(pseudo, True, vert)
            entreeUtilisateurRect = entreeUtilisateur.get_rect(midtop=demandePseudoRect.midbottom)  # Permet de toujours centrer le pseudo

    clock.tick(30)

    surf.fill(couleurFond)
    surf.blit(demandePseudo, demandePseudoRect)
    surf.blit(entreeUtilisateur, entreeUtilisateurRect)
    pygame.display.flip()

# Boucle pour le menu
while boucleMenu:

    # Vérification des événements pygame
    for event in pygame.event.get():  # Permet au joueur de quitter le jeu
        if event.type == pygame.QUIT:
            boucleMenu = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and bouton_jouer_pos.collidepoint(event.pos):
            # si la souris fait un clic gauche (1) sur le bouton à la position du rectangle
            boucleDecompte = 180  # On met le compteur pour la boucle de décompte avant le commencement du jeu à 180 pour qu'il dure 3 secondes (60 boucles par seconde)
            boucleJeu = 2400  # On met le compteur pour la boucle de jeu à 2400 pour qu'il dure 40 secondes (60 boucles par seconde)
            boucleImage = True  # On met la variable sur vraie pour faire le rendu à la fin du jeu
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and bouton_galerie_pos.collidepoint(event.pos):
            # si la souris fait un clic gauche (1) sur le bouton à la position du rectangle
            print("Bienvenue dans la galerie")  # alors on imprime la phrase suivante
            boucleMenu = False

    surf.blit(fondMenu, (0, 0))  # positionner l'image
    surf.blit(derniereImage, (30, 140))
    pygame.display.flip()

    # Boucle pour le décompte avant le jeu
    while boucleDecompte > 0:

        clock.tick(60)  # On effectue cette boucle 60 fois en une seconde

        # Vérification des événements pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Permet au joueur de quitter le jeu
                boucleDecompte = 0
                boucleJeu = 0
                boucleImage = False  # On met la variable sur faux parce que l'on quitte le jeu

        # Vérification du temps restant et affichage du décompte en conséquence
        if boucleDecompte > 120:
            surf.fill(couleurFond)
            surf.blit(decompteTrois, decompteTroisRect)
        elif 60 < boucleDecompte < 120:
            surf.fill(couleurFond)
            surf.blit(decompteDeux, decompteDeuxRect)
        elif 0 < boucleDecompte < 60:
            surf.fill(couleurFond)
            surf.blit(decompteUn, decompteUnRect)

        pygame.display.flip()
        boucleDecompte -= 1

    # Boucle du jeu
    while boucleJeu > 0:

        clock.tick(60)  # On effectue cette boucle 60 fois en une seconde

        secondes = boucleJeu // 60 + 1  # On calcul le nombre de secondes restantes
        surfaceCompteur = compteur.render(str(secondes), False, (0, 0, 0))  # On affiche le temps restant sur la surfaceCompteur

        # Vérification des événements pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Permet au joueur de quitter le jeu
                boucleJeu = 0
                boucleImage = False  # On met la variable sur faux parce que l'on quitte le jeu
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and billeRect.collidepoint(event.pos):  # Vérificationdu clique du joueur sur la bille
                listeCoordonneesCliquees.append((billeRect.x, billeRect.y))
                nombreBillesCliquees += 1
                billeRect.x, billeRect.y = random.randint(150, 800), random.randint(150, 500)  # Positionnement aléatoire de la nouvelle bille
                vitesse = [random.choice(vitessesNiveauFacile), random.choice(vitessesNiveauFacile)]  # Avec une vitesse aléatoirement choisie dans le niveau Facile

        # Vérification des coordonnées de la bille
        if billeRect.left < 0 or billeRect.right > longueur:
            vitesse[0] = -vitesse[0]  # Permet de créer un effet de rebond sur le bord
        if billeRect.top < 0 or billeRect.bottom > hauteur:
            vitesse[1] = -vitesse[1]  # Permet de créer un effet de rebond sur le bord

        billeRect = billeRect.move(vitesse)  # Définition des nouvelles coordonnées de la bille

        surf.fill(couleurFond)
        surf.blit(bille, billeRect)
        surf.blit(surfaceCompteur, (0,0))
        pygame.display.flip()
        boucleJeu -= 1

    # Réalisation de l'image
    if boucleImage and listeCoordonneesCliquees != []:
        surf.fill(couleurFond)
        for coord in listeCoordonneesCliquees:
            surf.blit(listeTaches[random.randint(0, 9)], coord)  # Ajoute des taches au hasard sur la surface aux coordonnées des cliques
            pygame.display.flip()
        pygame.image.save(surf, "derniere image.png")  # Sauvegarde de l'image réalisée dans le même dossier que le programme
        os.remove('data/derniere image.png')  # Suppression de l'ancienne image
        os.rename('derniere image.png', 'data/derniere image.png')  # Déplacement de la nouvelle image dans le dossier data
        derniereImage = pygame.image.load(os.path.join('data', 'derniere image.png'))
        derniereImage = pygame.transform.scale(derniereImage, (360, 246))

    elif boucleImage and listeCoordonneesCliquees != []:
        surf.fill(couleurFond)

    # Boucle pour l'affichage de l'image finale
    while boucleImage:

        clock.tick(60)  # On effectue cette boucle 60 fois en une seconde

        # Vérification des événements pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Permet au joueur de quitter le jeu
                boucleImage = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and boutonSuivantRect.collidepoint(event.pos):
                boucleImage = False
                boucleScoreboard = True

        surf.blit(boutonSuivant, boutonSuivantRect)
        pygame.display.flip()

    # Vérification du plus haut score:
    if nombreBillesCliquees > meilleurScore:
        scoreFichier = open(os.path.join('data', 'score.txt'), 'w')
        scoreFichier.write(str(nombreBillesCliquees))
        meilleurJoueurFichier = open(os.path.join('data', 'meilleur joueur.txt'), 'w')
        meilleurJoueurFichier.write(str(pseudo))
        meilleurScore = nombreBillesCliquees
        meilleurJoueur = pseudo
        scoreFichier.close()
        meilleurJoueurFichier.close()
        meilleurScoreAffichage = police.render("Meilleur Score : {}".format(meilleurScore), True, (0, 0, 0))        #
        meilleurScoreAffichageRect = meilleurScoreAffichage.get_rect(center=(longueur // 2, hauteur // 2))          # Changement du meilleur jouer et du meilleur score
        meilleurJoueurAffichage = police.render("Meilleur joueur : {}".format(meilleurJoueur), True, (0, 0, 0))     #
        meilleurJoueurAffichageRect = meilleurJoueurAffichage.get_rect(midbottom=meilleurScoreAffichageRect.midtop) #

    # Créaton de l'affichage du score du joueur
    scoreJoueurAffichage = police.render("Votre Score : {}".format(nombreBillesCliquees), True, (0, 0, 0))
    scoreJoueurAffichageRect = scoreJoueurAffichage.get_rect(midtop=meilleurScoreAffichageRect.midbottom)

    while boucleScoreboard:

        clock.tick(60)  # On effectue cette boucle 60 fois en une seconde

        # Vérification des événements pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Permet au joueur de quitter le jeu
                boucleScoreboard = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and boutonSuivantRect.collidepoint(event.pos):
                boucleScoreboard = False

        surf.blit(meilleurJoueurAffichage, meilleurJoueurAffichageRect)
        surf.blit(meilleurScoreAffichage, meilleurScoreAffichageRect)
        surf.blit(scoreJoueurAffichage, scoreJoueurAffichageRect)
        surf.blit(boutonSuivant, boutonSuivantRect)
        pygame.display.flip()

pygame.quit()
