#Crie um programa para analisar o IMC de uma pessoa, e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.

peso=float(input("Digite seu peso: "))
altura=float(input("Digite a sua altura: "))

imc = peso / (altura*altura)
print(imc)

if imc >40:
    print("Obesidade grave")
elif imc>30:
    print("Obesidade")
elif imc > 27:
    print("Sobrepeso")
elif imc > 22:
    print("Normal")
else:
    print("magreza")

