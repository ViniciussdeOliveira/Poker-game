# MIT License
# Copyright (c) 2024 Vinícius de Oliveira
# Github: https://github.com/ViniciussdeOliveira
# See LICENSE file for more information.

from .carta import Carta
import random

class Baralho:
    NAIPES = ['♠', '♥', '♦', '♣']
    VALORES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

    def __init__(self):
        self.cartas = [Carta(valor,naipe) for valor in Baralho.VALORES for naipe in Baralho.NAIPES]
        self.embaralhar()
    
    def embaralhar(self):
        random.shuffle(self.cartas)
    
    def dar_carta(self):
        return self.cartas.pop(0)