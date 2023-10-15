'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
'''
print('Vamos saber se passou de ano ...')
n1 = float(input('Digite a 1° nota '))
n2 = float(input('Digite a 2° nota '))
media = (n1 + n2) / 2
if media <= 4.9:
    print('Sua média foi de {} infelizmente foi REPROVADO '.format(media))
elif 5.0 <= media <= 6.9: 
    print('Sua média foi de {} ficou de RECUPERAÇÃO'.format(media))
else:
    print('Sua média foi de {} foi APROVADO'.format(media))
print('===*FIM*===')


