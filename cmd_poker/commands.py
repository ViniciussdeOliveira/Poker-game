import random

def quantidade_jogadores():
    while True:
        try:
            qtd = int(input("Quantos jogadores deseja ter na mesa? (max.: 8) "))
            if qtd > 0 and qtd < 9:
                return qtd
            else:
                print("Por favor, insira um número maior que 0.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def criar_bots(qtd_bots):
    return [f"BOT-{i+1}" for i in range(qtd_bots)]

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
                opcao = str(input("Deseja adicionar outro jogador (S/N)?")).strip().upper()
                if opcao == "N":
                    break
            else:
                print("Todos os lugares já foram ocupados!")
        else:
            print("Nome invalido!")
    
    qtd_bots = qtd_jogadores - qtd_nomes
    nomes.extend(criar_bots(qtd_bots))
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
    
    def embaralhar(self):
        random.shuffle(self.cartas)

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []
    
    def receber_mao(self,carta):
            self.mao.append(carta.pop(0))
    
    def mostrar_mao(self):
        return ' '.join(map(str, self.mao))

def main():
# %%%%%%%%%%%%%%%%%%%%%%% CADASTRO DOS JOGADORES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    qtd_jogadores = quantidade_jogadores()
    print("Digite o nome dos jogadores (O restante será Bot)")
    nomes_jogadores = cadastrar_jogadores(qtd_jogadores)

# %%%%%%%%%%%%%%%%%%%%%%%%% Teste  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    deck = Baralho()
    deck.embaralhar()
    print(deck.cartas)
    player = [Jogador(str(name)) for name in nomes_jogadores]
    for _ in range(2):
        for play in player:
            play.receber_mao(deck.cartas)
    for p in player:
        print(f"Nome: {p.nome} - MAO: {p.mostrar_mao()}")
    print(deck.cartas)

if __name__ == "__main__":
    main()