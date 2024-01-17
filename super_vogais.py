# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 15:46:28 2024

@author: kraus
"""
def super_vogais():
    vogais =['a','e','i','o','u']
    palavra = input("Digite a palavra que vai sofrer a alteração: ")
    
    palavra_nova = [letra.upper() if letra.lower() in vogais else letra for letra in palavra]
    resultado = ''.join(palavra_nova)
    print(resultado)

super_vogais()
    