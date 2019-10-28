# -*- coding: utf-8 -*-
import numpy as np

from Grille import *

# Initialisation
N = 4

fromage = (0, 3)
murs = [(1, 1), (1, 2), (2, 1)]
# decharges = [(2, 2), (1, 3)]
decharges = []
# gouttesEau = [(3, 1), (2, 0)]
gouttesEau = []
g = Grille(N)
g.addMurs(murs)
g.addDecharges(decharges)
g.addGouttesEau(gouttesEau)
g.addFromage(fromage)
g.affichageGrille()

# Entraînement
g.train(10000) # 10 000 itérations

# Test
position_initiale = np.random.randint(0, N**2)
g.setPositionSouris(position_initiale)
g.play(position_initiale)
