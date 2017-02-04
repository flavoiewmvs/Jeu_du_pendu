#!/usr/bin/python
# -*- coding: utf-8 -*-



class Pendu():

    lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    fichier = "pendu.txt"

    def __init__(self):
        self.mots_fait = []
        self.resultats_fait = []
        self.mot = "PROGRAMMATION"
        self.mes_lettres = Pendu.lettres
        self.pendu = []
        with open(Pendu.fichier,"r") as f:
            for ligne in f.readlines():
                self.pendu.append(list(ligne.strip("\n")))



    def trouve_lettre(self,lettre):
        """
        Cette méthone retourne une liste de position d'une lettre contenu dans le mot a chercher
        Args:
            lettre: (string) Lettre a rechercher dans le mot a trouver

        Returns:
            (list int) liste de position trouvé
        """
        return [i for i, c in enumerate(self.mot) if c == lettre]




if __name__ == "__main__":
    mon_pendu = Pendu()
    print(mon_pendu.lettres)
    print(mon_pendu.mot)
    print(mon_pendu.trouve_lettre("O"))