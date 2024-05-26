import random
import os

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
    
    def __repr__(self):
        return f'{self.valor}{self.naipe}'

class Baralho:
    naipe = ['♠', '♥', '♦', '♣']
    valor = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

    def __init__(self):
        self.cartas = [Carta(valor,naipe) for valor in Baralho.valor for naipe in Baralho.naipe]
    
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
# %%%%%%%%%%%%%%%%%%%%%%% VARIAVEIS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    nomes = []
    opcao = 's'
    QTD_nomes = 0

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%% PARTE DE CADASTRO DOS JOGADORES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    print("Quantos jogadores deseja ter na mesa ?") 
    print("(Obs.: Se 2 pessoas forem jogar e tiver 5 na mesa, o excedente será BOT)")
    QTD_jogadores = int(input("Quantidade: "))

    print("Digite o nome dos jogadores")
    while opcao.upper() != "N" and QTD_nomes < QTD_jogadores:
        nome = str(input(f"Jogador {QTD_nomes+1}: "))
        nomes.append(nome)
        QTD_nomes+=1

        if QTD_jogadores - QTD_nomes != 0:
            print(f"Restam {QTD_jogadores - QTD_nomes} vaga(s)!")
            opcao = str(input("Deseja adicionar outro jogador (S/N)?"))
        else:
            print("Todos os lugares já foram ocupados!")
    
    QTD_bots = QTD_jogadores - QTD_nomes
    for i in range(QTD_bots):
        bot = (f"BOT-{i+1}")
        nomes.append(str(bot))

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%% CRIACAO DA MESA %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    deck = Baralho()
    deck.embaralhar()
    player = [Jogador(str(name)) for name in nomes]
    for _ in range(2):
        for play in player:
            play.receber_mao(deck.cartas)
    for p in player:
        print(f"Nome: {p.nome} - MAO: {p.mostrar_mao()}")

if __name__ == "__main__":
    main()

# TODO: Features e upgrades
#    - Melhorar o código existente
#    - Criar a mesa (Reunir os jogadores e distribuir cartas para o jogo)
#    - Adicionar as regras de vitória
#    - Criar o jogar novamente
#    - Criar as fases de aposta
#    - fazer com que os bots também apostem (Pensar em uma lógica que permita uma boa esperiência para o usuário)
#    - Colocar um limitador para 8 pessoas
