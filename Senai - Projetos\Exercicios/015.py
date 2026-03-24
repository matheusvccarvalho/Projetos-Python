#Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.

nome=input("Digite seu nome: ")
idade=int(input("Digite sua idade: "))
peso=float(input("Digite seu peso: "))
tatuagem =input("Tem alguma tatuagem ?")
saude= input("Tem algum problema de saúde? ")
alcool = input("Insere bebida alcoolica?  ")


if idade >18 and idade<69 and peso > 50 and tatuagem =='Não' and saude =='Não' and alcool == 'Não':
    print('Pode doar')
else:
    print('Não pode doar')