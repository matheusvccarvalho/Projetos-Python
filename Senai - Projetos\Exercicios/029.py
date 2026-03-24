'''
Crie um programa que leia vários números inteiros. O programa só vai parar quando o usuário digitar 0000.
No final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)
'''

soma = 0
contagem = 0

while True:
    n = input('Numero: ')

    if n == '0000':
        break
    soma +=int(n)
    contagem +=1

print(f'A soma é {soma} com {contagem} números')