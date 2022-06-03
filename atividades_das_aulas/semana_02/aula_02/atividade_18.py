S=float(input('digite o salário:\n'))
if S<=280:
    percentual=20
    aumento_salario=S*0.20
    Salario_total=aumento_salario+S
elif S>280 and S<=700:
    percentual=15
    aumento_salario=S*0.15
    Salario_total=aumento_salario+S
elif S>700 and S<=1500:
    percentual=10
    aumento_salario=S*0.10
    Salario_total=aumento_salario+S
elif S>1500:
    percentual=5
    aumento_salario=S*0.05
    Salario_total=aumento_salario+S
print(f'O salario antes do reajuste:R${S}')
print(f'O percentual do aumento:{percentual}%')
print(f'O valor do aumento:R${round(aumento_salario,2)}')
print(F'O salario após aumento:R${round(Salario_total,2)}')