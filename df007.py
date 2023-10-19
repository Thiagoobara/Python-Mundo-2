'''
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes

Desenvolva um programa que leia o comprimento de 3 retas e diga se ela pode ou não formar um triangulo.
'''
r1 = float(input('Digite a 1° reta '))
r2 = float(input('Digite a 2° reta '))
r3 = float(input('Digite a 3° reta '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Sim, é possível formar o triangulo, ', end='' )
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')

else:
    print('Não é possível formar um triangulo ')
print('---Fim----')