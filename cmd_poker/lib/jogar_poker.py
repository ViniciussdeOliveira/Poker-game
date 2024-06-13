# MIT License
# Copyright (c) 2024 Vinícius de Oliveira
# Github: https://github.com/ViniciussdeOliveira
# See LICENSE file for more information.

from .utils import quantidade_jogadores, cadastrar_jogadores, limpar_tela
from .mesa import Mesa

def Jogar_Poker():
    opcao = "S"

    qtd_jogadores = quantidade_jogadores()
    print("Digite o nome dos jogadores (O restante será Bot)")
    nomes_jogadores = cadastrar_jogadores(qtd_jogadores)

    qtd_nomes_jogadores = 0
    for i in range(len(nomes_jogadores)):
        if "BOT" not in nomes_jogadores[i]:
            qtd_nomes_jogadores += 1

    mesa = Mesa(nomes_jogadores)

    while opcao != "N":
        mesa.distribuir_cartas()

        for i in range(qtd_nomes_jogadores):
            limpar_tela()
            input(f"Precione qualquer tecla para mostrar a mão do jogador {mesa.player[i].nome}.")
            mesa.mostar_mao_especifica(i)
            input(f"Precione qualquer tecla para continuar.")
            limpar_tela()
        
        print("Fase do Flop")
        mesa.flop()
        for i in range(qtd_nomes_jogadores):
            input(f"Precione qualquer tecla para mostrar a mão do jogador {mesa.player[i].nome}.")
            mesa.mostar_mao_especifica(i)
            print(f"Mesa Flop: {' '.join(map(str, mesa.mesa))}")
            input(f"Precione qualquer tecla para continuar.")
            limpar_tela()

        print("Fase do Turn")
        mesa.turn()
        for i in range(qtd_nomes_jogadores):
            input(f"Precione qualquer tecla para mostrar a mão do jogador {mesa.player[i].nome}.")
            mesa.mostar_mao_especifica(i)
            print(f"Mesa Turn: {' '.join(map(str, mesa.mesa))}")
            input(f"Precione qualquer tecla para continuar.")
            limpar_tela()

        print("Fase do River")
        mesa.river()
        for i in range(qtd_nomes_jogadores):
            input(f"Precione qualquer tecla para mostrar a mão do jogador {mesa.player[i].nome}.")
            mesa.mostar_mao_especifica(i)
            print(f"Mesa River: {' '.join(map(str, mesa.mesa))}")
            input(f"Precione qualquer tecla para continuar.")
            limpar_tela()
        
        mesa.mostar_mao_geral()
        print(f"Mesa Final: {' '.join(map(str, mesa.mesa))}")
        print("Vencedor: Em construção...")

        input(f"Precione qualquer tecla para continuar.")
        limpar_tela()

        mesa.resetar_mesa()

        opcao = input("Deseja jogar novamente com os mesmos jogadores (S/N)? ").strip().upper()
    
    print("Thanks for playing!")