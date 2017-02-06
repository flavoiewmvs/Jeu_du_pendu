#!/usr/bin/python
# -*- coding: utf-8 -*-



class Pendu():

    lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    fichier = "pendu.txt"
    fichier_seq = "pendu_seq.txt"

    def __init__(self):
        self.lettre_fait = []
        self.resultats_fait = []
        self.mes_lettres = Pendu.lettres
        self.pendu = []
        with open(Pendu.fichier,"r") as f:
            for ligne in f.readlines():
                self.pendu.append(list(ligne.strip("\n")))
        self.pendu_seq = []
        with open(Pendu.fichier_seq,"r") as f:
            for ligne in f.readlines():
                self.pendu_seq.append(list(ligne.strip("\n")))
        seq = []
        for ligne in self.pendu_seq:
            for item in ligne:
                seq.append(item)
        self.sequence = list(set(seq))
        self.sequence.sort()
        self.prochain = 0



    def trouve_lettre(self,lettre,mot):
        """
        Cette méthone retourne une liste de position d'une lettre contenu dans le mot a chercher
        Args:
            lettre: (string) Lettre a rechercher dans le mot a trouver

        Returns:
            (list int) liste de position trouvé
        """
        self.lettre_fait.append(lettre)
        return [i for i, c in enumerate(mot) if c == lettre]

    def affiche_prochain(self,prochain):
        ligne_courante = 0
        for ligne in self.pendu_seq:
            item_courant = 0
            for item in ligne:
                if item <= prochain:
                    print(self.pendu[ligne_courante][item_courant],end="")
                else:
                    print(" ",end="")
                item_courant += 1
            print()
            ligne_courante += 1

    def affiche(self):
        self.efface_ecran()
        print(self.lettres)
        print("-".join(self.lettre_fait))
        print()
        self.affiche_prochain(self.sequence[self.prochain])
        print()
        print()

    def efface_ecran(self):
        for i in range (1,40):
            print()



if __name__ == "__main__":
    mon_pendu = Pendu()
    print(mon_pendu.trouve_lettre("O","FLOCON"))
    mon_pendu.prochain=9
    mon_pendu.affiche()

    print(mon_pendu.trouve_lettre("Z", "FLOCON"))
    mon_pendu.prochain += 1
    mon_pendu.affiche()
