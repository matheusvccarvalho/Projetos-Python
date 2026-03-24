'''
Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder.
Ao final deve mostrar a quantidade de vitórias
'''

import random

vitorias =0

while True:
    pc=random.randint(1,10)
    n=int(input('N: '))
    j=input('Par ou Impar [P/I]: ').strip().upper()[0]

    if (((pc+n) %2 ==0) and j=='P') or (((pc+n) %2 !=0) and j =='I'):
            print(f'Venceu - Soma: {pc + n}')
            vitorias +=1
    else:
        print(f'Perdeu - Soma: {pc + n}')
        print(f'Ganhou {vitorias} vezes')

        break