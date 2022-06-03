cor_1=input('digite a primeira cor:\n')
cor_2=input('digite a segunda cor:\n')
if cor_1=='vermelho':
    if cor_2=='amarelo':
        print('laranja')
    elif cor_2=='azul':
        print('roxo')
    elif cor_2=='vermelhor':
        print('vermelho')
elif cor_1=='azul':
    if cor_2=='amarelo':
        print('verde')
    elif cor_2=='vermelho':
        print('roxo')
    elif cor_2=='azul':
        print('azul')
elif cor_1=='amarelo':
    if cor_2=='vermelho':
        print('laranja')
    elif cor_2=='azul':
        print('verde')
    elif cor_2=='amarelo':
        print('amarelo')
else:
    print('error')