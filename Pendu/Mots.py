#! /usr/bin/python
# -*- coding: utf-8 -*-
from random import randint

class Mots():

    fichier = "mots.txt"

    def __init__(self):
        self.mots = []
        self.nb=0
        self.mot_courant=""
        self.mot_masque=[]
        self.mots_fait = []
        with open(Mots.fichier,"r") as f:
            for mot_fichier in f.readlines():
                self.mots.append(mot_fichier.strip("\n"))
                self.nb += 1


    def donne_mot(self):
        """
        Cette méthone retourne un mot
        Args:

        Returns:
            (string) mot
        """
        mot_valide = False
        while not mot_valide:
            pos = randint(1,self.nb)
            if self.mots[pos] not in self.mots_fait:
                self.mots_fait.append(self.mots[pos])
                mot_valide = True
        self.mot_courant=self.mots[pos]
        self.mot_masque=list("_"*(len(self.mot_courant)-1))
        return self.mots[pos]

if __name__ == "__main__":
    mes_mots = Mots()
    mes_mots.donne_mot()
    print(mes_mots.mot_courant)
    print(" ".join(mes_mots.mot_masque))
