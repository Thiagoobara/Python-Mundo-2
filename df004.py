'''
 Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
atual = date.today().year
nascimento = int(input('Em que ano nasceu ? '))
idade = atual - nascimento
falta = 18 - idade
passou = idade - 18
if idade == 18:
    print('Esta com {} anos, você esta na idade de se alistar '.format(idade))
elif idade < 19:
    print('Esta com {} anos falta {} anos  para se alistar '.format(idade, falta))
else:
    print('Esta com {} anos, passou {} anos do seu alistamento '.format(idade, passou))
print('*===FIM===*')

