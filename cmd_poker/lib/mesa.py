# MIT License
# Copyright (c) 2024 Vinícius de Oliveira
# Github: https://github.com/ViniciussdeOliveira
# See LICENSE file for more information.

from .jogador import Jogador
from .baralho import Baralho

class Mesa:
    def __init__(self,nomes_jogadores):                
        self.player = [Jogador(name) for name in nomes_jogadores]
        self.deck = Baralho()
        self.mesa = []
    
    def distribuir_cartas(self):
        for _ in range(2):
            for jogador in self.player:
                jogador.receber_mao(self.deck.dar_carta())
    
    def mostar_mao_geral(self):
        for jogador in self.player:
            print(f"Nome: {jogador.nome} - MAO: {jogador.mostrar_mao()}")
    
    def mostar_mao_especifica(self,numero):
        print(f"MAO: {self.player[numero].mostrar_mao()}")
    
    def flop(self):
        self.deck.dar_carta() #descarte
        for _ in range(3):
            self.mesa.append(self.deck.dar_carta())
        print(' '.join(map(str, self.mesa)))
    
    def turn(self):
        self.deck.dar_carta() #descarte
        self.mesa.append(self.deck.dar_carta())
        print(' '.join(map(str, self.mesa)))

    def river(self):
        self.deck.dar_carta() #descarte
        self.mesa.append(self.deck.dar_carta())
        print(' '.join(map(str, self.mesa)))
    
    def resetar_mesa(self):
        self.deck = Baralho()
        self.mesa = []
        for jogador in self.player:
            jogador.resetar_mao()
