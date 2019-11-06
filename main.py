# -*- coding: utf-8 -*-
import numpy as np

from Grille import *

if "__name__" == "__main__":
    # ================= BASIC TEST =================
    # On place des murs et de l'eau à des positions fixes.
    # Le fromage est dans la 0-ième case de la grille (en haut à gauche)
    # La souris est initialement dans le coin bas droit (en case 15)


    # Initialisation
    N = 4

    fromage = (0, 0)
    murs = [(1, 1), (1, 2), (2, 1)]
    # decharges = [(3, 1)]
    decharges = []
    gouttes_eau = [(3, 1)]
    # gouttesEau = []
    g = Grille(N)
    g.addMurs(murs)
    g.addDecharges(decharges)
    g.addGouttesEau(gouttes_eau)
    g.addFromage(fromage)

    # Entraînement
    g.train(10000) # 10 000 itérations

    # Test
    # rdm = np.random.randint(N**2)
    # position_initiale = (rdm//N, rdm%N)
    position_initiale = (3, 3)
    g.setPositionSouris(position_initiale)
    g.affichageGrille()
    g.play(position_initiale)

    # ================= RANDOM TEST =================
    # On choisit une grille de taille 20x20
    # Nombre d'éléments de chaque sorte : entre N/2 et 80% de N (pour une taille 4,on a donc entre 2 et 3 murs/décharges/eau)
    # Tous les éléments sont placés random
    # Entraînement sur 10 000 essais
    # Souris placée au hasard (pas sur un mur mais potentiellement sur une eau/décharge)


    N = 20
    nb_elements = int(0.8*N) # 80% de N
    nb_murs = np.random.randint(N//2, nb_elements)
    nb_decharges = np.random.randint(N//2, nb_elements)
    nb_gouttes_eau = np.random.randint(N//2, nb_elements)
    casesDisposPourAjoutEnvironnement = [(i, j) for i, j in np.ndindex((N, N))] # pour éviter qu'un même case ait plusieurs éléements d'environnement
    fromage = casesDisposPourAjoutEnvironnement.pop(np.random.randint(len(casesDisposPourAjoutEnvironnement)))
    murs = []
    decharges = []
    gouttes_eau = []
    for i in range(nb_murs):
        murs.append(casesDisposPourAjoutEnvironnement.pop(np.random.randint(len(casesDisposPourAjoutEnvironnement))))
    for i in range(nb_decharges):
        decharges.append(casesDisposPourAjoutEnvironnement.pop(np.random.randint(len(casesDisposPourAjoutEnvironnement))))
    for i in range(nb_gouttes_eau):
        gouttes_eau.append(casesDisposPourAjoutEnvironnement.pop(np.random.randint(len(casesDisposPourAjoutEnvironnement))))
    g = Grille(N)
    g.addMurs(murs)
    g.addDecharges(decharges)
    g.addGouttesEau(gouttes_eau)
    g.addFromage(fromage)

    # Entraînement
    g.train(10000) # 10 000 itérations

    # Test
    rdm = np.random.randint(N**2)
    while (rdm//N, rdm%N) in murs : # vérifions que position_initiale n'est pas un mur
        rdm = np.random.randint(N**2)
    position_initiale = (rdm//N, rdm%N)
    g.setPositionSouris(position_initiale)
    g.affichageGrille()
    g.play(position_initiale)


    # ================= COMPLEXITY TEST =================
    # Test de la complexité : on crée des grilles aléatoires et on observe le temps d'entraînement pour des tailles différentes
    import matplotlib.pyplot as plt

    temps = []

    for N in range(3, 100):
        # même code donc même fonctionnement que random test
        nb_elements = int(0.8*N) # 80% de N
        nb_murs = np.random.randint(N//2, nb_elements)
        nb_decharges = np.random.randint(N//2, nb_elements)
        nb_gouttes_eau = np.random.randint(N//2, nb_elements)
        casesDisposPourAjoutEnvironnement = [(i, j) for i, j in np.ndindex((N, N))] # pour éviter qu'un même case ait plusieurs éléements d'environnement
        fromage = casesDisposPourAjoutEnvironnement.pop(np.random.randint(len(casesDisposPourAjoutEnvironnement)))
        murs = []
        decharges = []
        gouttes_eau = []
        for i in range(nb_murs):
            murs.append(casesDisposPourAjoutEnvironnement.pop(np.random.randint(len(casesDisposPourAjoutEnvironnement))))
        for i in range(nb_decharges):
            decharges.append(casesDisposPourAjoutEnvironnement.pop(np.random.randint(len(casesDisposPourAjoutEnvironnement))))
        for i in range(nb_gouttes_eau):
            gouttes_eau.append(casesDisposPourAjoutEnvironnement.pop(np.random.randint(len(casesDisposPourAjoutEnvironnement))))
        g = Grille(N)
        g.addMurs(murs)
        g.addDecharges(decharges)
        g.addGouttesEau(gouttes_eau)
        g.addFromage(fromage)

        # Entraînement
        temps_entrainement = g.train(10000) # 10 000 itérations
        temps.append(temps_entrainement)

    # Traçons les résultats
    plt.figure()
    plt.plot(range(3, 100), temps, 'red', label='Méthode simple')

    plt.xlabel("Taille de la grille")
    plt.ylabel("Temps d'éxécution de l'entraînement")
    plt.savefig("Time.png")
    plt.show()

    # # ================= REWARD PARAMETERS INFLUENCE TEST =================
    # from Grille import * # on ré-importe les variables RWD_EAU, RWD_DECHARGE, RWD_FROMAGE
    # RWD_EAU, RWD_DECHARGE, RWD_FROMAGE = 50, 100, -50# on les modifie
    # N = 20
    #
    # def creer_une_grille():
    #     # on re-crée une grille random comme pour random test
    #     nb_elements = int(0.8*N) # 80% de N
    #     nb_murs = np.random.randint(N//2, nb_elements)
    #     nb_decharges = np.random.randint(N//2, nb_elements)
    #     nb_gouttes_eau = np.random.randint(N//2, nb_elements)
    #     casesDisposPourAjoutEnvironnement = [(i, j) for i, j in np.ndindex((N, N))] # pour éviter qu'un même case ait plusieurs éléements d'environnement
    #     fromage = casesDisposPourAjoutEnvironnement.pop(np.random.randint(len(casesDisposPourAjoutEnvironnement)))
    #     murs = []
    #     decharges = []
    #     gouttes_eau = []
    #     for i in range(nb_murs):
    #         murs.append(casesDisposPourAjoutEnvironnement.pop(np.random.randint(len(casesDisposPourAjoutEnvironnement))))
    #     for i in range(nb_decharges):
    #         decharges.append(casesDisposPourAjoutEnvironnement.pop(np.random.randint(len(casesDisposPourAjoutEnvironnement))))
    #     for i in range(nb_gouttes_eau):
    #         gouttes_eau.append(casesDisposPourAjoutEnvironnement.pop(np.random.randint(len(casesDisposPourAjoutEnvironnement))))
    #     g = Grille(N)
    #     g.addMurs(murs)
    #     g.addDecharges(decharges)
    #     g.addGouttesEau(gouttes_eau)
    #     g.addFromage(fromage)
    #
    #     # Entraînement
    #     g.train(10000) # 10 000 itérations
    #
    #     return g
    #
    # g = creer_une_grille()
    #
    # # Test
    # rdm = np.random.randint(N**2)
    # while (rdm//N, rdm%N) in murs : # vérifions que position_initiale n'est pas un mur
    #     rdm = np.random.randint(N**2)
    # position_initiale = (rdm//N, rdm%N)
    # g.setPositionSouris(position_initiale)
    # g.affichageGrille()
    # g.play(position_initiale)
