#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo (sem considerar os espaços)
#Quantas letras tem o primeiro nome


#Solicita o nome completo ao usuário.(Uso do strip para garantir que não haja espaço antes, nem após a escrita do nome.)
nome_completo=input("Digite seu nome..:").strip()

#Exibe o nome completo com letras maiúsculas
print(nome_completo.upper())

#Exibe o nome completo com letras minúsculas
print(nome_completo.lower())

#Criando variaveis para armazenar quantas letras tem o nome completo, e outra para contar quantos espaços existem.
#Depois, criamos uma variavel total para exibir a subtração de letras e espaços.

total_letras=len(nome_completo)
total_espacos=nome_completo.count(" ")

total=total_letras-total_espacos
print(total)

#Quantas letras tem o primeiro nome


primeiro_espaco=nome_completo.find(' ')
primeiro_nome=nome_completo[0:primeiro_espaco]
quantidade_letras_primeiro_nome_v1=len(primeiro_nome)
print(quantidade_letras_primeiro_nome_v1)

quantidade_letras_primeiro_nome_v2=nome_completo.find(' ')
print(quantidade_letras_primeiro_nome_v2)





