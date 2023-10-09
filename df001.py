'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
print('Realizando o sonho da casa própria que bom vamos analisar ')
print('==*=='*10)
valor_casa = float(input('Digite o valor da casa dos sonhos R$ '))
valor_salario = float(input('Digite seu salario R$ '))
anos = float(input('Em quantos anos pretende pagar? '))
soma = (valor_salario*30) / 100
pagamento_mes = valor_casa / (12 * anos)
print('==*=='*10)
if pagamento_mes <= valor_salario :
    print('Parabéns seu financiamento foi aprovado ')
    print('Ficou R${:.2f} por mês '.format(pagamento_mes))

else:
    print('Desculpa não se enquadra ')
    print('Ficou R${:.2f} por mês '.format(pagamento_mes))
    