# MIT License
# Copyright (c) 2024 Vinícius de Oliveira
# Github: https://github.com/ViniciussdeOliveira
# See LICENSE file for more information.

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []
        self.forca = None
    
    def receber_mao(self,carta):
        self.mao.append(carta)
    
    def mostrar_mao(self):
        return ' '.join(map(str, self.mao))
    
    def resetar_mao(self):
        self.mao = []