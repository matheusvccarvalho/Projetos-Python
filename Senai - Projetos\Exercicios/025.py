'''
Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e continue
pedindo até que o usuário acerte o número.
E no final, retorne também a quantidade de tentativas necessárias.
'''

import random

tentativas=1

pc = random.randint(1,10)
j=int(input('Digite um numero de 1 a 10:  '))

while j != pc:
    j = int(input('Digite um numero de 1 a 10:  '))
    tentativas +=1

    print(f'Tentativas: {tentativas}')