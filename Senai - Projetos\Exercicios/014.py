'''
Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.
'''

letra=input("Por favor, digite um letra: ").strip().lower()[0]

letra=letra.replace('á','a')
letra=letra.replace('à','a')
letra=letra.replace('â','a')
letra=letra.replace('ã','a')

letra=letra.replace('é', 'e')
letra=letra.replace('è', 'e')
letra=letra.replace('ê', 'e')
letra=letra.replace('ẽ', 'e')

letra=letra.replace('í', 'i')
letra=letra.replace('ì', 'i')
letra=letra.replace('î', 'i')

letra=letra.replace('ó', 'o')
letra=letra.replace('ô', 'o')
letra=letra.replace('ò', 'o')

letra=letra.replace('ú', 'u')
letra=letra.replace('ù', 'u')
letra=letra.replace('û', 'u')

if letra == 'a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
    print("Vogal")
else:
    print('Consoante')