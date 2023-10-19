'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida

'''
import time
print('===*Bem vindo a balança virtual*=== ')
peso = float(input('Digite seu peso em kg '))
altura = float(input('Digite sua altura '))
imc = peso / (altura ** 2 )
print('Calculando ...')
time.sleep(2)
if imc <= 18.4:
    print('Seu peso é de {} e sua altura é {} portanto seu imc é {:.2f} está Abaixo do Peso'.format(peso,altura, imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu peso é de {} e sua altura é {} portanto seu imc é {:.2f} está no peso ideal '.format(peso, altura, imc))
elif imc >= 26 and imc <= 30:
    print('Seu peso é de {} e sua altura é {} portanto seu imc é {:.2f} está com Sobrepeso '.format(peso, altura, imc))
elif imc >= 31 and imc <= 40:
    print('Seu peso é de {} e sua altura é {} portanto seu imc é {:.2f} está Obesidade '.format(peso, altura, imc))
else:
    print('Seu peso é de {} e sua altura é {} portanto seu imc é {:.2f} está Obesidade Mórbida'.format(peso, altura, imc))
print('===*FIM*===')
