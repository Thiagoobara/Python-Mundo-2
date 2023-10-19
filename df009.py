'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros
'''
print('===*BEM VINDO*==')
preco = float(input('Digite o valor do produto R$'))
print('Escolha a forma de pagamento ')
print(('''
     [1] À vista no dinheiro|cheque
     [2] À vista no cartão
     [3] 2x no cartão 
     [4] 3x ou mais no cartão'''))
forma = int(input('Digite sua escolha: '))
if forma == 1:
    avista = (preco * 10) / 100
    pagar1 = preco - avista
    print('Valor a ser pago R${:.2f}'.format(pagar1))
elif forma == 2:
    avistac = (preco * 5) / 100
    pagar2 = preco - avistac
    print('Valor a ser pago R${:.2f}'.format(pagar2))
elif forma == 3:
    print('Valor a ser pago R${:.2f}'.format(preco))
else :
    tresx = (preco * 20) / 100
    pagar4 = preco + tresx
    print('Valor a ser pago R${:.2f}'.format(pagar4))
print('===*OBRIGADO volte sempre*===')





