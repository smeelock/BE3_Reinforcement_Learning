# -*- coding: utf-8 -*-
# =============================================================================
#                               Classe Grille
# =============================================================================
class Grille :
    # =============================================================================
    #                                __init__
    # =============================================================================
    def __init__(self, dimension, fromage=None, lstMurs=None, lstDecharges=None, lstGouttesEau=None):
        """ On initialise tous les éléments que l'on va trouver dans la grille """
        # self.__grille = np.zeros((self.__dim,self.__dim))
        self.__dim = dimension

        # Souris dans la grille
        # positionInit = (0,0)
        # self.__souris = Souris(positionInit)
        self.__positionSouris = (0,0)

        # Eléments de la grille
        self.__murs = lstMurs if lstMurs != None else []
        self.__decharges = lstDecharges if lstDecharges != None else []
        self.__gouttesEau = lstGouttesEau if lstGouttesEau != None else []
        self.__fromage = fromage if fromage != None else (np.random.randint(0,self.__dim, size=1), np.random.randint(0,self.__dim, size=1))

        # Matrice de récompenses
        self.__rewardMatrix = np.matrix(np.ones((self.__dim**2, self.__dim**2))) # matrice de n²*n² car on peut (potentiellement) aller de chaque case à chaque case,
                                            # ie n² états possibles vers n² autre états possibles
        self.__rewardMatrix *= -1 # matrice de -1 partout

            # Decharges
        for decharge in self.__decharges :
            antecedents = self.casesVoisinesDisponibles(decharge)
            # print("DEBUG: antecedents - {}".format(antecedents))
            for v in antecedents :
                old, new = self.fromTuple2caseNumber(v), self.fromTuple2caseNumber(decharge)
                self.__rewardMatrix[old, new] = 0

                # Gouttes d'eau
        for goutte in self.__gouttesEau :
            antecedents = self.casesVoisinesDisponibles(goutte)
            # print("DEBUG: antecedents - {}".format(antecedents))
            for v in antecedents :
                old, new = self.fromTuple2caseNumber(v), self.fromTuple2caseNumber(goutte)
                self.__rewardMatrix[old, new] = 50

                # Fromage
        antecedents = self.casesVoisinesDisponibles(self.__fromage)
        # print("DEBUG: antecedents - {}".format(antecedents))
        for v in antecedents :
            old, new = self.fromTuple2caseNumber(v), self.fromTuple2caseNumber(self.__fromage)
            self.__rewardMatrix[old, new] = 100
    # =============================================================================
    #                                  get...()
    # =============================================================================

    # def getGrille(self):
    #     """ Renvoie la grille """
    #     return(self.__grille)

    # def getPositionMurs(self):
    #     """ Renvoie les positions des murs """
    #     return(self.__murs)
    #
    # def getPositionFromage(self):
    #     """ Renvoie la position de l'objectif """
    #     return(self.__fromage)
    #
    # def getPositionDecharge(self):
    #     """ Renvoie les positions des différentes décharges """
    #     return(self.__decharges)
    #
    # def getPositionEau(self):
    #     """ Renvoie les positions des gouttes d'eau """
    #     return(self.__gouttesEau)

    # =============================================================================
    #                                  add...()
    # =============================================================================
    def addGouttesEau(self, lstCases):
        """ Rajoute des gouttes d'eau aux emplacements lstCases """
        for case in lstCases:
            self.__gouttesEau.append(case)
        self.__gouttesEau = set(self.__gouttesEau) # on enlève les doublons
        # DEBUG: print("DEBUG: Eau ajoutée à la grille !")

    def addMurs(self, lstCases):
        """ Rajoute des murs aux emplacements lstCases """
        for case in lstCases:
            self.__murs.append(case)
        self.__murs = set(self.__murs) # on enlève les doublons
        # DEBUG: print("DEBUG: Mur ajouté à la grille !")

    def addDecharges(self, lstCases):
        """ Rajoute des décharges aux emplacements lstCases """
        for case in lstCases:
            self.__decharges.append(case)
        self.__decharges = set(self.__decharges) # on enlève les doublons
        # DEBUG: print("DEBUG: Decharge ajoutée à la grille !")

    def addFromage(self, case):
        """ Rajoute le fromage à l'emplacement case """
        self.__fromage = case
        # DEBUG: print("DEBUG: Fromage ajoutée à la grille !")

    # =============================================================================
    #                                  affichage
    # =============================================================================
    def affichageGrille(self):
        """ Renvoie un affichage dans la console de la grille
        o : objectif;   s : souris;
        # : mur;        '': case vide;
        e : eau;        x : décharge
        """
        grilleAffichage = np.reshape(np.array(['']*self.__dim**2), (self.__dim,self.__dim)) # crée une grille de NxN remplie de ''

        # Souris
        grilleAffichage[self.__positionSouris] = 's'

        # Fromage
        grilleAffichage[self.__fromage] = 'o'

        # Murs
        for mur in self.__murs:
            grilleAffichage[mur] = '#'

        # Eau
        for eau in self.__gouttesEau:
            grilleAffichage[eau] = '-'

        # Décharge
        for decharge in self.__decharges:
            grilleAffichage[decharge] = 'x'

        # for case in self.getGrille():
        #     if self.__souris.getPositionSouris() == case :
        #         grilleAffichage[case] = 's'
        #     elif case in self.getPositionEau():
        #         grilleAffichage[case] = 'e'
        #     elif case in self.getPositionDecharge():
        #         grilleAffichage[case] = 'x'
        #     elif case == self.getPositionFromage():
        #         grilleAffichage[case] = 'o'
        #     elif case in self.getPositionMurs():
        #         grilleAffichage[case] = '#'

        # Affichage
        print("INFO: grille - \n{}".format(grilleAffichage))
        print("#"*20)

    # =============================================================================
    #                           Fonctions utiles au jeu
    # =============================================================================
    def casesVoisinesDisponibles(self, case):
        """ Contrôle quelles cases voisines peuvent être visitées par la souris """
        i, j = case
        voisins = []

        for v in [(i,j+1), (i,j-1), (i+1,j), (i-1,j)] : # nord/sud/est/ouest
            # On vérifie que la case est dans la grille et n'est pas un mur
            a, b = v
            if a >= 0 and a < self.__dim and b >= 0 and b < self.__dim and v not in self.__murs:
                voisins.append(v)

        return voisins

    def fromTuple2caseNumber(self, case):
        """ Transforme la position de la case (i, j) en son numéro """
        i,j = case
        return i*self.__dim+j
    # def faireBougerSourisRandom(self):
    #     """ Faire bouger la souris """
    #     voisinsSouris = self.casesVoisinesDisponibles(self.__souris.getPositionSouris())
    #     self.__souris.setPosition(voisinsSouris[random.randint(0, len(voisinsSouris))])
    #     self.__fileModifications.append() # TODO: ajouter dans la file ce qu'il faut modif

    # def majGrille(self):
    #     """ Mise à jour des informations de la grille """
    #     # Souris
