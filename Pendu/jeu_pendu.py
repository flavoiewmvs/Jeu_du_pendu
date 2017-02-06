#!/usr/bin/python
# -*- coding: utf-8 -*-

from Pendu import  Pendu
from Mots import  Mots



if __name__ == "__main__":
    mon_pendu = Pendu()
    mes_mots = Mots()
    mon_mot = mes_mots.donne_mot()
    mon_pendu = Pendu()
    print(mon_pendu.trouve_lettre("O", mon_mot))

    mon_pendu.prochain = 9
    mon_pendu.affiche()

    print(mon_pendu.trouve_lettre("Z", mon_mot))
    mon_pendu.prochain += 1
    mon_pendu.affiche()
    print(mon_mot)
