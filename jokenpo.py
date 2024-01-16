# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 14:56:27 2024

@author: kraus
"""      
   
def jokenpo():
    jogadas = ["Pedra", "Papel", "Tesoura"]

    jogada_1 = input("Jogador 1, qual é o seu movimento? ").strip().capitalize()
    jogada_2 = input("Jogador 2, qual é o seu movimento? ").strip().capitalize()

    if jogada_1 in jogadas and jogada_2 in jogadas:
        if jogada_1 == jogada_2:
            print("Deu empate!")
        elif (jogada_1 == "Pedra" and jogada_2 == "Tesoura") or \
             (jogada_1 == "Papel" and jogada_2 == "Pedra") or \
             (jogada_1 == "Tesoura" and jogada_2 == "Papel"):
            print("Jogador 1 ganhou!")
        else:
            print("Jogador 2 ganhou!")
    else:
        print("Jogue um movimento válido!")

if __name__ == "__main__":
    jokenpo()

        
            
        
    
    
    
  