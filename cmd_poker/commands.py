import random
import os

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

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
    
    def __repr__(self):
        return f'{self.valor}{self.naipe}'

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

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []
    
    def receber_mao(self,carta):
            self.mao.append(carta)
    
    def mostrar_mao(self):
        return ' '.join(map(str, self.mao))

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
        descarte = self.deck.dar_carta()
        for _ in range(3):
            self.mesa.append(self.deck.dar_carta())
        print(' '.join(map(str, self.mesa)))
    
    def turn(self):
        descarte = self.deck.dar_carta()
        self.mesa.append(self.deck.dar_carta())
        print(' '.join(map(str, self.mesa)))

    def river(self):
        descarte = self.deck.dar_carta()
        self.mesa.append(self.deck.dar_carta())
        print(' '.join(map(str, self.mesa)))

def Jogar_Poker():
    opcao = "S"

    qtd_jogadores = quantidade_jogadores()
    print("Digite o nome dos jogadores (O restante será Bot)")
    nomes_jogadores = cadastrar_jogadores(qtd_jogadores)

    qtd_nomes_jogadores = 0
    for i in range(len(nomes_jogadores)):
        if "BOT" not in nomes_jogadores[i]:
            qtd_nomes_jogadores += 1

    while opcao != "N":
        x = Mesa(nomes_jogadores)
        x.distribuir_cartas()

        for i in range(qtd_nomes_jogadores):
            os.system("cls")
            lixo = input(f"Precione qualquer tecla para mostrar a mão do jogador {x.player[i].nome}.")
            x.mostar_mao_especifica(i)
            lixo = input(f"Precione qualquer tecla para continuar.")
            os.system("cls")
        
        print("Fase do Flop")
        x.flop()
        for i in range(qtd_nomes_jogadores):
            lixo = input(f"Precione qualquer tecla para mostrar a mão do jogador {x.player[i].nome}.")
            x.mostar_mao_especifica(i)
            print(f"Mesa Flop: {' '.join(map(str, x.mesa))}")
            lixo = input(f"Precione qualquer tecla para continuar.")
            os.system("cls")

        print("Fase do Turn")
        x.turn()
        for i in range(qtd_nomes_jogadores):
            lixo = input(f"Precione qualquer tecla para mostrar a mão do jogador {x.player[i].nome}.")
            x.mostar_mao_especifica(i)
            print(f"Mesa Turn: {' '.join(map(str, x.mesa))}")
            lixo = input(f"Precione qualquer tecla para continuar.")
            os.system("cls")

        print("Fase do River")
        x.river()
        for i in range(qtd_nomes_jogadores):
            lixo = input(f"Precione qualquer tecla para mostrar a mão do jogador {x.player[i].nome}.")
            x.mostar_mao_especifica(i)
            print(f"Mesa River: {' '.join(map(str, x.mesa))}")
            lixo = input(f"Precione qualquer tecla para continuar.")
            os.system("cls")
        
        x.mostar_mao_geral()
        print(f"Mesa Final: {' '.join(map(str, x.mesa))}")
        print("Vencedor: Em construção...")

        lixo = input(f"Precione qualquer tecla para continuar.")
        os.system("cls")

        opcao = input("Deseja jogar novamente com os mesmos jogadores (S/N)? ").strip().upper()
        

def main():
    Jogar_Poker()

if __name__ == "__main__":
    main()
