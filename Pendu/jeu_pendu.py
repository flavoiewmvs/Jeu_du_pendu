#!/usr/bin/python
# -*- coding: utf-8 -*-

from Pendu import  Pendu
from Pendu import  Mots



if __name__ == "__main__":
    mon_pendu = Pendu()
    print(mon_pendu.lettres)
    mes_mots = Mots()
    print(mes_mots.donne_mot())