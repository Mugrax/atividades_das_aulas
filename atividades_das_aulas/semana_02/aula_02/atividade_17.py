from distutils.log import error
from urllib import response


temperatura=float(input('digite a temperatura:\n'))
escolha=int(input('digite 1 ou 2 para:\n1-Converter celsius em Fahrenheit\n2-Converter Fahrenheit em Celsius\n'))
if escolha==1:
    resposta=(temperatura*9/5)+32
    print(f'{round(resposta,1)} graus Fahrenheit')
elif escolha==2:
    resposta=(temperatura-32)*5/9
    print(f'{round(resposta,1)} graus Celsius')
else:
    print('digite uma opçâo valida')
