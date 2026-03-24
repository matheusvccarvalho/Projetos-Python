import random
import time

pc = random.randint(1,3)
j = int(input('1 - Pedra \n2 - Papel \n3 - Tesoura \n ---->'))
if j>3:
    j=int(input('Digite outro numero:'))

time.sleep(1)
print('JO')
time.sleep(1)
print('KEM')
time.sleep(1)
print('PO')
time.sleep(1)
print('Ainda pensando')
time.sleep(1)

if pc ==j:
    print('Empate')
elif(j==1 and pc ==3) or (j ==2 and pc ==1) or (j == 3 and pc ==2):
    print(f'Jogador ganhou  J: {j} x {pc} :PC')
else:
    print(f'Perdeu! :)  J: {j} x {pc} :PC')

