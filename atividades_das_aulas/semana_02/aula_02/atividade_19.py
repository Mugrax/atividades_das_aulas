N=int(input('digite um número até 1000:\n'))
C=N/100
Cc=C-C%1
D=(N-(100*Cc))/10
Dd=D-D%1
U=N-(10*Dd)-(100*Cc)
Uu=U-U%1
if Cc==0:
    if Cc==0 and Dd==0:
        print(f'{round(Uu)} unidades.')
    elif Cc==0 and Uu==0:
        print(f'{round(Dd)} dezenas.')
    else:
        print(f'{round(Dd)} dezenas e {round(Uu)} unidades.')
elif Dd==0:
    if Dd==0 and Uu==0:
        print(f'{round(Cc)} centenas.')
    else:    
        print(f'{round(Cc)} centenas e {round(Uu)} unidades.')
elif Uu==0:
    print(f'{round(Cc)} centenas e {round(Dd)} dezenas.')
else:
    print(f'{round(Cc)} centenas, {round(Dd)} dezenas e {round(Uu)} unidades.')