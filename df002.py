'''
 Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''
num = int(input('Digite um número '))
print('''Esconha uma base para conversão :
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal ''')          
opçao = int(input('Sua opção: ')) 
if opçao == 1: 
   print('{} convertido para Binário é igual a {} '.format(num, bin(num)[2:]))
elif opçao == 2:
   print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif opçao == 3:
   print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
   print('Opção invalida')
print('==*=='*10)