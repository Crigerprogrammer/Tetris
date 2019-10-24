#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random

class Forma(object):
    formaNinguna = 0
    formaI = 1
    formaL = 2
    formaJ = 3
    formaT = 4
    formaO = 5
    formaS = 6
    formaZ = 7

    #Tupla con las coordenadas de las formas del juego tetris
    coordinadas = (
        ((0, 0), (0, 0), (0, 0), (0, 0)), #Las coordenadas de la formaNinguna
        ((0, -1), (0, 0), (0, 1), (0, 2)), #Las coordenadas de la formaI
        ((0, -1), (0, 0), (0, 1), (1, 1)), #Las coordenadas de la formaL
        ((0, -1), (0, 0), (0, 1), (-1, 1)), #Las coordenas de la formaJ
        ((0, -1), (0, 0), (0, 1), (1, 0)), #Las coordenadas de la formaT
        ((0, 0), (0, -1), (1, 0), (1, -1)), #Las coordenadas de la forma O
        ((0, 0), (0, -1), (-1, 0), (1, -1)), #Las coordenadas de la forma S
        ((0, 0), (0, -1), (1, 0), (-1, -1)) #Las coordenadas de la forma Z
    )

    #Funcion principal
    def __init__(self, forma=0):
        self.forma = forma  #Se instancia la forma
    
    

