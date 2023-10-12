'''
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
'''

numero_1 = int(input('Digite o 1° número '))
numero_2 = int(input('Digite o 2° número '))
if numero_1 > numero_2:
    print('O 1° número é maior ')
elif numero_2 > numero_1:
    print('O 2° número é maior  ')
else:
    print('O 1° número e o 2° número são iguais ')
print('===FIM===')
