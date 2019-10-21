# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:20:42 2019

@author: Alexandre
"""

import numpy as np
import random

class Grille:

    global N

    def __init__(self):
        """ On initialise tous les éléments que l'on va trouver dans la grille """
        self.__grille = np.zeros((N,N))
        self.__mur = []
        self.__positionSouris = (0,0)  
        self.__positionDecharge = []
        self.__positionEau = []
        self.__positionFromage = (random.randint(N), random.randin(N))

    def getMurs(self):
        """ Renvoie les positions des murs """
        return(self.__mur)

    def getPositionSouris(self):
        """ Renvoie la position de la souris """
        return(self.__positionSouris)

    def setPositionSouris(self,case):
        """ Déplacement de la souris vers la case "case" """
        self.__positionSouris = case

    def getPositionFromage(self):
        """ Renvoie la position de l'objectif """
        return(self.__positionFromage)

    def getPositionDecharge(self):
        """ Renvoie les positions des différentes décharges """
        return(self.__positionDecharge)

    def getPositionEau(self):
        """ Renvoie les positions des gouttes d'eau """
        return(self.__positionEau)


    def affichageGrille(self):
        """ Renvoie un affichage dans la console de la grille
        x : objectif
        s : souris
        * : mur
        '': case vide
        e : eau
        """






class MatriceStochastique:
