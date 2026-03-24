'''
Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:

1.	Somar
2.	Multiplicar
3.	Maior
4.	Novos números
5.	Sair do programa

'''

n1=int(input('Digite um numero: '))
n2=int(input('Digite um numero: '))
n3=int(input('Digite um numero: '))

while True:
    menu = int(input('1. Somar'
                     '\n2. Multiplicar'
                     '\n3. Maior'
                     '\n4. Novos Números'
                     '\n5. Sair ------>'))

    if menu ==1:
        print(f'A soma é {n1+n2+n3}')
    elif menu ==2:
        print(f'A multiplicação é {n1*n2*n3}')
    elif menu ==3:
        if n1>n2 and n1 > n3:
            print(f'O maior é {n1}')
        elif n2>n3:
            print(f'O maior é {n2}')
        else:
            print(f'O maior é o {n3}')

    elif menu ==4:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite um numero: '))
        n3 = int(input('Digite um numero: '))
    elif menu ==5:
        break

    else:
        print('Informação Incorreta')
























