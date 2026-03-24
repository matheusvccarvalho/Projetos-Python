'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:

Qual é o total gasto na compra
Quantos produtos custam mais de R$1000,00
Qual é o produto mais barato

'''

soma = 0
quant_prod_maior_1000 = 0

preco_mais_barato=None
nome_mais_barato= ''

while True:
    produto = input('Produto [Sair para parar]: ')
    if produto =='Sair':
        break

    preco = float(input('Preço: '))

    if preco_mais_barato == None:
        preco_mais_barato=preco
        nome_mais_barato = produto

    if preco < preco_mais_barato:
        preco_mais_barato = preco
        nome_mais_barato = produto

    soma +=preco

    if preco>1000:
        quant_prod_maior_1000 +=1

print(f'A soma é {soma}'
      f'\nProduto mais barato: {nome_mais_barato}'
      f'\nQuantidade de produtos que custam mais de 1000: {quant_prod_maior_1000}')
