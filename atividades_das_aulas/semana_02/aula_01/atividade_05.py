P=float(input('digite o primeiro número:'))
S=float(input('digite o segundo número:'))
T=float(input('digite o terceiro número:'))
if P+S==T:
    print('A soma do primeiro com o segundo resultam no terceiro')
elif S+T==P:
    print('A soma do segundo com o terceiro resultam no primeiro')
elif P+T==S:
    print('A soma do primeiro com o terceiro resultam no segundo')
else:
    print('nenhum resultado')    