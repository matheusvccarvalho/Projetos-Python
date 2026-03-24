#Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.

#Leitura de dados
raio=float(input('Digite o raio da esfera: '))

Volume= (4/3) * 3.14 * raio ** 3
Area= 4 * 3.14 * raio ** 2

#Retorno das informações
print(f'Volume da esfera {Volume:.2f}\nA area é {Area:.2f}')
