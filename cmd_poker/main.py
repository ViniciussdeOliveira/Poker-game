# MIT License
# Copyright (c) 2024 Vinícius de Oliveira
# Github: https://github.com/ViniciussdeOliveira
# See LICENSE file for more information.

from lib.jogar_poker import Jogar_Poker
from lib.utils import desenhar_poker

def main():
    desenhar_poker()
    Jogar_Poker()

if __name__ == "__main__":
    main()

""" TODO:
x Criar a funcao resetar mao em jogadores
x melhorar o reset do jogo em jogar-POKER()
x limpar o código
x separar as classes
x incluir a licença MIT
- fazer o readme
- mudar o qtd_nomes_jogadores para armazenar as posições em vez de quantos são
- começar a classe que analisa as maos para gerar o que ele tem
 """