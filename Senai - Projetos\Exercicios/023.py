#Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos

maior_peso = None
menor_peso=None

for i in range (7):
    peso=float(input('Peso: '))

    if maior_peso == None and menor_peso ==None:
        maior_peso = peso
        menor_peso=peso

    if peso > maior_peso:
       maior_peso=peso

    if menor_peso < peso:
        maior_peso = peso
print(f'O menor peso é {menor_peso}'
          f'\n O maior peso é {maior_peso}')
