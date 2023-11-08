import random
import time

# INÍCIO DA CLASSE DEALER
class Dealer:
    def __init__(self, identificacao):
        self.cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # Cartas do Baralho
        self.identificacao = identificacao

    def distribuirCartas(self, jogador):
        carta = random.sample(self.cartas, 2)
        for i in carta:
            jogador.cartas_jogador.append(carta)
            self.cartas.remove(carta)
        print(f"\nCartas do Jogador: {jogador.cartas_jogador}")
        print(f"Soma: {sum(jogador.cartas_jogador)}")

    def compraCarta(self, jogador):
        carta = random.sample(self.cartas, 1)
        jogador.cartas_jogador.append(carta)
        self.cartas.remove(carta)
        print(f"\nCartas do Jogador: {jogador.cartas_jogador}")
        print(f"Soma: {sum(jogador.cartas_jogador)}")
        

# FIM DA CLASSE DEALER

nome_dealer = input("Insira a identificação do dealer: ")
dealer = Dealer(nome_dealer)


# INÍCIO DA CLASSE JOGADOR
class Jogador():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.pontos = 0
        self.cartas_jogador = []

    # def setCartas(self, cartas):
    #     self.__cartas_jogador = cartas

    # def getCartas(self):
    #     return self.__cartas_jogador
        
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
                    dealer.distribuirCartas(jogador)
                    jogadores.append(jogador)
                
                    compra = int(input("\n1 - comprar \n2 - parar \nO que gostaria de fazer? "))

                    while compra == 1:
                        dealer.compraCarta(jogador)
                    else:
                        print("O jogador parou")

                    

                else:
                    print("Você não possui idade suficiente para jogar!")
                    pass
                
        else:
            print("bye bye")
            exit()
    


jogar = Jogar()
jogar.iniciarJogo()
            

   
# FIM DA CLASSE JOGAR 