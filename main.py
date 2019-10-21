# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:07:10 2019

@author: Alexandre
"""

import classes

# Initialisation

N = 4

g = Grille()
g.addMur([(1,1), (2,4)])
g.addGouttesEau([(2,3), (2,6)])
g.affichageGrille()


print(g.casesVoisinesDisponibles((0,0)))

mat = MatriceProbabilite(g)
print(mat.initProbabilite())
