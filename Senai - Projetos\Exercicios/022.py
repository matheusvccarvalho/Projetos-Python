'''
Escreva um programa que leia o Nome, idade e sexo de 4 pessoas. No final mostre:
 1. A média de idade do grupo,
 2. Qual é o homem mais velho,
 3. Quantas mulheres têm menos de 20 anos
'''

soma_idades=0
idade_homem_mais_velho=0
nome_homem_mais_velho=''
quantidade_mulheres_menor_20_anos = 0

for i in range(4):
    nome = input('Nome: ')
    idade=int(input('Idade: '))
    sexo= input('M/F: ').strip().upper()[0]

    #Media
    soma_idades=(soma_idades+idade)

    if sexo =='M' and idade>idade_homem_mais_velho:
     idade_homem_mais_velho = idade
     nome_homem_mais_velho=nome

    #Quantidade de mulheres com menos de 20 anos

    if sexo =='F' and idade<20:
     quantidade_mulheres_menor_20_anos = quantidade_mulheres_menor_20_anos+1

print(f'\nA média de idades é de: {soma_idades/4}'
      f'\nNome do Homem mais velho: {nome_homem_mais_velho}'
      f'\nQuantidade de mulheres com menos de 20 anos: {quantidade_mulheres_menor_20_anos}')








