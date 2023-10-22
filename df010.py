'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
jogadapc = randint (0, 2)
print('-='*11)
print('''Suas opções:
    [0] Pedra
    [1] Papel
    [2] Tesoura
    ''')
print('-='*11)
jogador = int(input('Qual sua escolha? '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POW')
print('Computador jogou {}'.format(itens[jogadapc]))
print('Jogador jogou {}' .format(itens[jogador]))
if jogadapc == 0:            #pc jogou pedra
    if jogador == 0:
        print('EMPATE (-_-)')
    elif jogador == 1:
        print('JOGADOR GANHA (*_-)')
    elif jogador == 2:
        print('COMPUTADOR VENCE (;_;)')
    else:
        print('Jogada ivalida')    
if jogadapc == 1: #pc jogou papel
    if jogador == 0:
        print('COMPUTADOR GANHA (;_;)')
    elif jogador == 1:
        print('EMPATE (-_-)')
    elif jogador == 2:
        print('Jogador vence (*_-)')
    else:
        print('Jogada ivalida')
          
if jogadapc == 2:            #pc jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE (*_-)')
    elif jogador == 1:
        print('COMPUTADOR VENCE (;_;)')
    elif jogador == 2:
        print('EMPATE (-_-)')
    else:
        print('Jogada ivalida')