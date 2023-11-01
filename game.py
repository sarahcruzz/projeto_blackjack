import random
import time

# INÍCIO DA CLASSE DEALER
class Dealer:
    def __init__(self, identificacao):
        self.cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # Cartas do Baralho
        self.identificacao = identificacao

    def cartasIniciais(self, jogador):       
        distribuicao = random.sample(self.cartas, 2)
        for i in distribuicao:
            jogador.setCartas(distribuicao)
            self.cartas.remove(i)
        print(f"Cartas do jogador: {jogador.getCartas()}")
        print(f"Soma: {sum(jogador.getCartas())}\n")
        jogador.pontos = sum(jogador.getCartas())

            
    def distribuirMaisCartas(self):
        distribuicao = random.sample(self.cartas, 1)
        for i in distribuicao:
            jogador.getCartas.append(i)
            self.cartas.remove(i)
        print(self.cartas_jogador)
        

# FIM DA CLASSE DEALER

nome_dealer = "Derek"
dealer = Dealer(nome_dealer)


# INÍCIO DA CLASSE JOGADOR
class Jogador():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.pontos = 0
        self.__cartas_jogador = []

    def setCartas(self, cartas):
        self.__cartas_jogador = cartas

    def getCartas(self):
        return self.__cartas_jogador
        
# FIM DA CLASSE JOGADOR
jogadores = []

# INÍCIO DA CLASSE jOGAR 
class Jogar():
    def iniciarJogo(self):
        print("="*43)
        print("\tBEM VINDO AO BLACKJACK ♠ !!")
        print("="*43)
        time.sleep(0.5)
        confirm = input("Gostaria de iniciar o jogo? (s/n): ")

        if confirm == "s":
            print(f"\nIdentificação do Dealer: {dealer.identificacao}")
            quant_jogadores = int(input("\nInforme a quantidade de jogadores: "))
            

            for i in range(quant_jogadores):
                nome_jogador = input(f"\nDigite o nome do {i+1} jogador: ")
                idade_jogador = int(input(f"Digite a idade do {i+1} jogador: "))

                if idade_jogador >= 18:
                    jogador = Jogador(nome_jogador, idade_jogador)
                    dealer.cartasIniciais(jogador)
                    jogadores.append(jogador)
                    print(f"Pontuação: {jogadores[i].pontos}, Nome: {jogadores[i].nome}")

                    compra = input("Gostaria de comprar mais uma carta? (H)it (S)tand ").upper
                    while compra == "H":
                        

                else:
                    print("Você não possui idade suficiente para jogar!")
                    pass
                
        else:
            print("bye bye")
            exit()
        
        def 


jogar = Jogar()
jogar.iniciarJogo()
            

   
# FIM DA CLASSE JOGAR 