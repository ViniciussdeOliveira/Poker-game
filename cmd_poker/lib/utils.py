# MIT License
# Copyright (c) 2024 Vinícius de Oliveira
# Github: https://github.com/ViniciussdeOliveira
# See LICENSE file for more information.

import os
import platform

def limpar_tela():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def quantidade_jogadores():
    while True:
        try:
            qtd = int(input("Quantos jogadores deseja ter na mesa? (max.: 8) "))
            if 0 < qtd <= 8:
                return qtd
            else:
                print("Por favor, insira um número maior que 0 e menor ou igual a 8!")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def cadastrar_jogadores(qtd_jogadores):
    nomes = []
    qtd_nomes = 0
    while qtd_nomes < qtd_jogadores:
        nome = str(input(f"Jogador {qtd_nomes+1}: ")).strip()
        if nome:
            nomes.append(nome)
            qtd_nomes+=1

            if qtd_jogadores - qtd_nomes != 0:
                print(f"Restam {qtd_jogadores - qtd_nomes} vaga(s)!")
                opcao = str(input("Deseja adicionar outro jogador (S/N)? ")).strip().upper()
                if opcao == "N":
                    break
            else:
                print("Todos os lugares já foram ocupados!")
        else:
            print("Nome invalido!")
    
    qtd_bots = qtd_jogadores - qtd_nomes
    nomes.extend([f"BOT-{i+1}" for i in range(qtd_bots)])
    return nomes

def desenhar_poker():
    lines = [
        "###   ###  #  # #### ###",
        "#  # #   # # #  #    #  #",
        "###  #   # ##   ###  ###",
        "#    #   # # #  #    # #",
        "#     ###  #  # #### #  #"
    ]
    
    # Determine the width of the longest line
    max_length = max(len(line) for line in lines)
    
    # Print the top border
    print('=' * (max_length + 4))
    
    # Print each line with side borders
    for line in lines:
        print('+ ' + line + ' ' * (max_length - len(line)) + ' +')
    
    # Print the bottom border
    print('=' * (max_length + 4))
