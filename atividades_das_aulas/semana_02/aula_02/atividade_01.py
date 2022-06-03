X=float(input('digite o primeiro número: \n'))
Y=float(input('digite o segundo número: \n'))
Z=int(input('digite uma das opções abaixo:\n1-adição \n2-subtração \n'))
if Z==1:
    Soma=X+Y
    print(f'a soma é {Soma}')
elif Z==2:
    sub=X-Y
    print(f'a subtração é {sub}')
else:
    Zz=int(input('digite uma opção valida...\n'))
    if Zz==1:
         Soma=X+Y
         print(f'a soma é {Soma}')
    elif Zz==2:
         sub=X-Y
         print(f'a subtração é {sub}')
