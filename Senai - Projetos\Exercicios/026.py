'''
Faça um programa que leia um número e retorne o fatorial !

4! = 4 x 3 x 2 x 1

'''

numero=int(input('Digite m numero e descubra o seu fatorial:'))

i=1
fat=1

while i<=numero:
    fat=fat*i
    i +=1

print(f'O fatorial de {numero} é {fat}')