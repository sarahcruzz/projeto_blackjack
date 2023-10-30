import random
import time

# INÍCIO DA CLASSE DEALER
class Dealer:
    def __init__(self, identificacao):
        self.cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # Cartas do Baralho
        self.identificacao = identificacao
        self.cartas_dealer = []
        self.cartas_jogador = []

    def cartasIniciais(self):       
        distribuicao = random.sample(self.cartas, 2)
        for i in distribuicao:
            self.cartas_dealer.append(i)
            self.cartas.remove(i)
        print(f"Cartas do Dealer: {self.cartas_dealer}")
        print(f"Soma: {sum(self.cartas_dealer)}\n")

        distribuicao = random.sample(self.cartas, 2)
        for i in distribuicao:
            self.cartas_jogador.append(i)
            self.cartas.remove(i)
        print(f"Cartas do jogador: {self.cartas_jogador}")
        print(f"Soma: {sum(self.cartas_jogador)}\n")

            
    def distribuirMaisCartas(self):
        distribuicao = random.sample(self.cartas, 1)
        for i in distribuicao:
            self.cartas_jogador.append(i)
            self.cartas.remove(i)
        print(self.cartas_jogador)
        

# FIM DA CLASSE DEALER

nome_dealer = "Derek"
dealer = Dealer(nome_dealer)


# INÍCIO DA CLASSE JOGADOR
class Jogador(Dealer):
    def __init__(self, nome, idade, pontos, cartas_mao):
        self.nome = nome
        self.__idade = idade
        self.pontos = pontos
        self.cartas_mao = []

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade



# FIM DA CLASSE JOGADOR



# INÍCIO DA CLASSE jOGAR 
class Jogar():
    def iniciarJogo(self):
        print("="*43)
        print("\tBEM VINDO AO BLACKJACK ♠ !!")
        print("="*43)
        time.sleep(0.5)
        confirm = input("Gostaria de iniciar o jogo? (s/n): ")

        if confirm == "s":
            print(f"Identificação do Dealer: {dealer.identificacao}")

            dealer.cartasIniciais()
            
        else:
            print("bye bye")
            exit()

    
        

        
jogar = Jogar()
jogar.iniciarJogo()
            

   
            
       



# FIM DA CLASSE JOGAR 