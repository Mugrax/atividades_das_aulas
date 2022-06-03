I=float(input('taxa: \n'))
P=float(input('aplicação mensal: \n'))
n=float(input('número de meses: \n'))
R=(P*(1+I)**n-1)/I
print(f'resultado:{R}')