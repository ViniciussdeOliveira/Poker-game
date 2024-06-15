# MIT License
# Copyright (c) 2024 Vinícius de Oliveira
# Github: https://github.com/ViniciussdeOliveira
# See LICENSE file for more information.

def verificar_conjuntos(valores):
    temp = {}
    for i in valores:
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1
    
    if 4 in temp.values():
        return "Quadra"
    elif 3 in temp.values():
        if 3 in temp.values() and 2 in temp.values():
            return "Full House"
        return "Trinca"
    elif list(temp.values()).count(2) == 2:
        return "Dois pares"
    elif 2 in temp.values():
        return "Par"
    else:
        return "Carta mais alta"

def verificar_sequencia(dicionario, valores):
    for i in range(len(valores)-4):
        if dicionario[valores[i]] + 4 == dicionario[valores[i+4]]:
            return True
    return False

def verifica_flush(naipe):
    temp = {}
    for naipes in naipe:
        if naipes in temp:
            temp[naipes] += 1
        else:
            temp[naipes] = 1
    
    if any(count >= 5 for count in temp.values()):
        return True
    else:
        return False

def verificar(mao_rodada,naipe):
    royal = ['T','J','Q','K','A']
    dicionario_valores = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}
    mao_ordenada = sorted(mao_rodada, key=lambda carta: dicionario_valores[carta])
    
    filtrado = sorted(set(mao_ordenada), key=lambda val: dicionario_valores[val])
    flush_verifica = verifica_flush(naipe)

    if flush_verifica:
        if all(element in mao_ordenada for element in royal) == True:
            return "Royal flush"
        elif verificar_sequencia(dicionario_valores, filtrado):
            return "Straight flush"
        return "Flush"  
    else:
        if verificar_sequencia(dicionario_valores, filtrado):
            return "Straight"
        return verificar_conjuntos(mao_ordenada)
    
def verificar_vencedor(jogadores):
    dicionario_forca = {'Carta mais alta': 1, 'Par': 2, 'Dois pares': 3, 'Trinca': 4, 'Straight': 5, 'Flush': 6, 'Full House': 7, 'Quadra': 8, 'Straight Flush': 9, 'Royal Flush': 10}
    dicionario_valores = {'A': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}
    maior_forca = 0
    vencedor = []

    for jogador in jogadores:
        if dicionario_forca[jogador.forca] > maior_forca:
            maior_forca = dicionario_forca[jogador.forca]
            vencedor = [jogador]
        elif dicionario_forca[jogador.forca] == maior_forca:
            vencedor.append(jogador)
    
    if len(vencedor) == 1:
        return vencedor[0].nome
    else:
        maior_valor = 0
        nome_vencedor = ""
        for jogador in vencedor:
            valor = [value.valor for value in jogador.mao]
            valores_mao = [dicionario_valores[k] for k in valor]
            valor_mais_alto = max(valores_mao)
            if valor_mais_alto > maior_valor:
                maior_valor = valor_mais_alto
                nome_vencedor = jogador.nome
            elif valor_mais_alto == maior_valor:
                for i in range(len(jogador.mao)):
                    if valores_mao[i] == maior_valor:
                        continue
                    elif valores_mao[i] > maior_valor:
                        maior_valor = valores_mao[i]
                        nome_vencedor = jogador.nome
                        break
                    else:
                        break
        
        return nome_vencedor