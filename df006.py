'''
 A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
'''
from datetime import date
print('Bem vindo A Confederação Nacional de Natação ')
ano = int(input('Em que ano nasceu ? '))
atual = date.today().year
idade = atual - ano

if idade <= 9 and idade >= 0:
    print('Sua idade é de {} então sua categoria é a Mirim'.format(idade))
elif idade <= 14 and idade >= 10 :
    print('Sua idade é de {} então sua categoria é a INFANTIL'.format(idade))
elif idade <= 19 and idade >= 15:
    print('Sua idade é de {} então sua categoria é a JÚNIOR'.format(idade))
elif idade <= 25 and idade >= 16:
    print('Sua idade é de {} então sua categoria é a SÊNIOR'.format(idade))
else:
    idade <= 26
    print('Sua idade é de {} então sua categoria é a MASTER'.format(idade))
print('===*BOA PROVA*===')
