contador=0
media_salario=0
media_filhos=0
percentual=0
maior_salario=0
while contador<5:
    salario=float(input('digite o sálario:\n'))
    num_filhos=int(input('digite o número de filhos:\n'))
    media_filhos+=num_filhos
    media_salario+=salario
    contador+=1
    if salario<=2000:
        percentual+=1
    if maior_salario<salario:
        maior_salario=salario 
media_salario/=5
media_filhos/=5
percentual*=20
print(f'média de salário:R${round(media_salario,2)}')
print(f'média de filhos:{media_filhos}')
print(f'maior salário:R${maior_salario}')
print(f'percentual de pessoas com salário até que R$2000:{percentual}%')