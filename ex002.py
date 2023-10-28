'''
Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, que é uma estrutura versátil e simples de entender. Por exemplo:

for c in range(0, 4):

print(c)

print(‘Acabou’)


'''
'''
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
'''
'''
for c in range (0, 7, 2):
    print(c)
print('===*FIM*===')
'''
'''
n = int(input('Digite um numero '))
for c in range(0, n+1):
    print(c)
print('Fim')
'''
'''
i = int(input('Inicio '))
f = int(input('Fim '))
p = int(input('Passo '))
for c in range(i, f+1 , p):
    print(c)
print('==*FIM*==')
'''
s = 0
for c in range(0, 4):
    n = int(input('Digite um numero '))
    s += n
print('A soma de todos foi {}'.format(s))
