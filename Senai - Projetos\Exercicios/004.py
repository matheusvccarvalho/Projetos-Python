#Escreva um programa que converta real para o Franco Congolês

#Leitura de dados
real= float(input("Digite qual valor em reis você deseja converter: "))
conversao = real * 499.826


#Retorno das informações
print(f'{real} reias , equivalem a {conversao:.2f} Francos Congolenses')
