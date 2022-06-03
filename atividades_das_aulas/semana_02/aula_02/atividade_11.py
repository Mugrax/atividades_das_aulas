from math import radians
from random import randint
a=int(input('digite um número:\n'))
b=int(input('digite um número:\n'))
variavel=randint(a,b)
P=int(input('digite seu palpite:\n'))
print(f'O número é:{variavel}')
if P==variavel:
    print('Você Acertou!')
elif P>variavel:
    print('Muito Alto...')
elif P<variavel:
    print('Muito Baixo...')