# Operações Matemáicas
'''
print(1+1)
print(54654-9)
print(454*8)
print(857/7)
print(3**3)

#print simples
print("Hello World")

#Variáveis e print formatado

nome = 'Matheus Carvalho'
idade = 19
print(f'Seu nome é {nome} e você tem {idade} anos')   #O "f" garante que o que está entre as chaves sejam as variaveis


#Leitura de dados

nome = input("Digite seu nome: ")
idade = input("Digite a sua idade: ")
cidade =input("Digite onde voce mora: ")

print(f'Seu nome é {nome} e você tem {idade} anos, e mora na cidade de {cidade}')


idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))

soma = idade1 + idade2

print(f'A soma de idades é {soma}')


#Strings

nome = 'Luis Eulálio'

#Fatiamento

print(nome[0])
print(nome[2:9])
print(nome[3:])


#Ánalise

print(len(nome))
print(nome.count('l'))
print(nome.find('l'))
print(nome.rfind('l'))

#Tranformação

nome = 'Luis Eulálio'
print(nome.upper())       # todas as letras serão maísculas
print(nome.lower())         # todas as letras serão minúsculas
print(nome.replace('L', 'l')) # substitui L por l

nome=input("Nome: ").strip()
print(nome)


Senai = 'LuisEulalio'

Senai.replace('L', 'P')  # substitui L por P
Senai.upper()  # todas as letras serão maíscula
Senai.lower()  # todas as letras serão minúsculas
Senai.capitalize()  # apenas a primeira letra da

Senai.title()  # todas as primeiras letras das
Senai.rstrip()  # remove espaços á direita
Senai.lstrip()  # remove espaços á esquerda


nome = 'Luis Eulálio'

print(len(nome))
print(nome.count('l'))
print(nome.find('l'))
print(nome.rfind('l'))


#Condicionais

numero=float(input("Digite um numero: "))

if numero >0:
    print("Positivo")
elif numero ==0:
    print("Nulo")
else:
    print("Negativo")

#For

for i in range(0,100):
    print('Bem vindo')

for i in range (0,10)
    print(i)

 for i in range(10,1,-1)
    print(i)

#soma

soma = 0
for i in range (0,5):

    n=int(input('Digite um número: '))
    soma= soma + n
    print(f'Soma : {soma}')

#while true
'''
while True:
    menu = int(input('1.OI'
                     '\n2.Olá'
                     '\n3. Sair ---->'))
    if menu ==1:
        print('OI')

    elif menu ==2:
        print('Olá')

    elif menu ==3:
        break

    else:
        print('Informação incorreta')








