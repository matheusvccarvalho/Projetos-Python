'''
s0 + v0 * t + (1/2) * a * t**2


s0 =   # Posicao inicial (m)
v0 =   # Velocidade inicial (m/s)
a =   # Aceleracao (m/s^2)
t =   # Tempo (s)
'''


s0=float(input('Digite a Posição inicial:  '))
v0=float(input('Digite a Velocidade Inicial: '))
a=float(input('Digite a Acelereção: '))
t=float(input('Digite o Tempo: '))

tempo_final = s0 + v0 * t + (1/2) * a * t**2

print(f'A posição do objeto no tempo {t}  é de {tempo_final} (m)')