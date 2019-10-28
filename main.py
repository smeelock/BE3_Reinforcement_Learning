# -*- coding: utf-8 -*-
import numpy as np

from Grille import *

# ================= BASIC TEST =================
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
