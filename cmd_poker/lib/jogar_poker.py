# MIT License
# Copyright (c) 2024 Vinícius de Oliveira
# Github: https://github.com/ViniciussdeOliveira
# See LICENSE file for more information.

from .utils import quantidade_jogadores, cadastrar_jogadores, limpar_tela
from .mesa import Mesa
from .regras import verificar, verificar_vencedor

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
        
        for jogador in mesa.player:
            maoGeral = jogador.mao + mesa.mesa
            valor = [value.valor for value in maoGeral]
            naipe = [suit.naipe for suit in maoGeral]
            jogador.forca = verificar(valor,naipe)

        vencedor = verificar_vencedor(mesa.player)
        
        mesa.mostar_mao_geral()
        print(f"Mesa Final: {' '.join(map(str, mesa.mesa))}")
        print("Vencedor: " + vencedor)

        input(f"Precione qualquer tecla para continuar.")
        limpar_tela()

        mesa.resetar_mesa()

        opcao = input("Pressione enter para continuar ou digite 'n' para sair ").strip().upper()
    
    print("Thanks for playing!")