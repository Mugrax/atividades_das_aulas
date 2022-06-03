N1B=float(input('digite a nota do primeiro bimestre:\n'))
N2B=float(input('digite a nota do segundo bimestre:\n'))
N3B=float(input('digite a nota do terceiro bimestre:\n'))
N4B=float(input('digite a nota do quarto bimestre:\n'))
NTA=int(input('digite o número total de aulas:\n'))
F=int(input('digite o número de faltas:\n'))
limite_de_faltas=NTA*0.25
if F>=limite_de_faltas:
    print('Reprovado por Faltas')
elif F<limite_de_faltas:
    Média_da_nota=(N1B+N2B+N3B+N4B)/4
    if Média_da_nota>=7.00:
        print('Aprovado')
    elif Média_da_nota<7.00:
        print('Reprovado por Média')