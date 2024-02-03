# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 21:34:46 2024

@author: kraus
"""

altura = int(input("Digite a altura do triângulo: " ))
largura_total = (altura * 2) - 1
altura += 1

for i in range(altura):
    espaco = (largura_total - (i * 2 - 1))//2
    print(" " * espaco  + "*" * (i * 2 - 1))