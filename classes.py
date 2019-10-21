# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:20:42 2019

@author: Alexandre
"""

import numpy as np
import random

class Grille :

    global N

    def __init__(self):
        """ On initialise tous les éléments que l'on va trouver dans la grille """
        self.__grille = np.zeros((N,N))
        self.__mur = []

        # Souris dans la grille
        positionInit = (0,0)
        self.__souris = Souris(positionInit)

        self.__positionDecharge = []
        self.__positionEau = []
        self.__positionFromage = (random.randint(0,N), random.randint(0,N))

    def getGrille(self):
        """ Renvoie la grille """
        return(self.__grille)

    def getMurs(self):
        """ Renvoie les positions des murs """
        return(self.__mur)

    def addMur(self,lst):
        """ Rajoute des murs aux emplacements case """
        for case in lst:
            self.getMurs().append(case)

    def getPositionFromage(self):
        """ Renvoie la position de l'objectif """
        return(self.__positionFromage)

    def getPositionDecharge(self):
        """ Renvoie les positions des différentes décharges """
        return(self.__positionDecharge)

    def getPositionEau(self):
        """ Renvoie les positions des gouttes d'eau """
        return(self.__positionEau)

    def addGouttesEau(self,lst):
        """ Rajoute des gouttes d'eau """
        for case in lst:
            self.getPositionEau().append(case)

    def affichageGrille(self):
        """ Renvoie un affichage dans la console de la grille
        o : objectif;   s : souris;
        # : mur;        '': case vide;
        e : eau;        x : décharge
        """

        grilleAffichage = np.reshape(np.array(['']*N**2), (N,N))

        for case in self.getGrille():
            if self.__souris.getPositionSouris() == case :
                grilleAffichage[case] = 's'
            elif case in self.getPositionEau():
                grilleAffichage[case] = 'e'
            elif case in self.getPositionDecharge():
                grilleAffichage[case] = 'x'
            elif case == self.getPositionFromage():
                grilleAffichage[case] = 'o'
            elif case in self.getMurs():
                grilleAffichage[case] = '#'

        print(grilleAffichage)


    def casesVoisinesDisponibles(self,case):
        """ Cette fonction contrôle quelles cases voisines peuvent être visitée par la souris """

        i, j = case
        voisins = [(i,j+1), (i,j-1), (i+1,j), (i-1,j)] # nord/sud/est/ouest

        for v in voisins:
            # On vérifie que la case est dans la grille
            a , b = v
            if a < 0 or a > N or b < 0 or b > N:
                voisins.remove(v)
            # On vérifie qu'il n'y a pas de mur
            if v in self.getMurs():
                voisins.remove(v)

        return(voisins)


class Souris :

    def __init__(self, positionInit=(0,0)):
        self.__position = positionInit

    def getPositionSouris(self):
        """ Renvoie la position de la souris """
        return self.__position

    def setPosition(self, case):
        """ Déplacement de la souris vers la case "case" """
        self.__position = case
        return self
