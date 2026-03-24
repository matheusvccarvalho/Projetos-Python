'''

#Crie um programa que leia uma frase e mostre:
1.Quantas vezes aparece a letra “a”
2.Em que posição ela aparece a primeira vez
3.Em que posição ela aparece na última vez
'''

frase=input("Digite uma frase: ").strip().lower()

frase=frase.replace('á','a')    # O lower transforma as lestras em minusculas
frase=frase.replace('à','a')    # O replace transforma os 'As' com acento em 'As' sem acento
frase=frase.replace('â','a')
frase=frase.replace('ã','a')

print(f'Quantidade de As:{frase.count('a')}'
      f'\nPrimeiro A:{frase.find('a')+1}'   
      f'\nUltimo  A;{frase.rfind('a')+1}')