#Crie um programa que leia um nome, e mostre o primeiro e o último nome

nome_completo=input("Digite seu nome..:")

primeiro_espaco=nome_completo.find(" ")
primeiro_nome=nome_completo[0:primeiro_espaco]


ultimo_espaco =nome_completo.rfind(' ')
ultimo_nome = nome_completo[ultimo_espaco +1:]

print(f'O primeiro nome é:{primeiro_nome}'
      f'\nO segudo nome é: {ultimo_nome}')