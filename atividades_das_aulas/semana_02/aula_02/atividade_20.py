N1=float(input('digite a primeira nota:\n'))
N2=float(input('digite a segunda nota:\n'))
M=(N1+N2)/2
if M>=0 and M<4:
    conceito='E'
elif M>=4 and M<6:
    conceito='D'
elif M>=6 and M<7.5:
    conceito='C'
elif M>=7.5 and M<9:
    conceito='B'
elif M>=9 and M<=10:
    conceito='A'
else:
    conceito='conceito invalida'
    print('nota invalida')
print(f'notas parcias:{round(N1,1)}/{round(N2,1)}')
print(f'média: {round(M,1)}')
print(f'conceito: {conceito}')
if conceito=='A' or conceito=='B'or conceito=='C':
    print('APROVADO')
elif conceito=='D' or conceito=='E':
    print('REPROVADO')