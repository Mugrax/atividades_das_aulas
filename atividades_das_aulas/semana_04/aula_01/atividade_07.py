from funções import imposto
dados=0
funcionarios=[]
total_horas=0
total_pagamento_bruto=0
total_imposto=0
total_pagamento_liquido=0
while dados==0:
    nome=input('digite o nome do funcionario:\n')
    valor_hora=float(input('digite o salário por hora:\n'))
    horas_trabalhadas=float(input('digite a quantidade de horas trabalhadas:\n'))
    salario_bruto=valor_hora*horas_trabalhadas
    imp=imposto(salario_bruto)
    valor_imp=salario_bruto*imp
    salario_liquido=salario_bruto+valor_imp
    percentual_de_imposto=imp*100
    funcionario=[]
    funcionario.append(nome)
    funcionario.append(horas_trabalhadas)
    funcionario.append(salario_bruto)
    funcionario.append(salario_liquido)
    funcionario.append(percentual_de_imposto)
    funcionario.append(valor_imp)
    funcionarios.append(funcionario)
    dados=int(input('Se deseja continuar tecle 0\nSe pretende finalizar tecle 1\n'))
volume=len(funcionarios)
for i in range(volume):
    total_horas+=funcionarios[i][1]
    total_pagamento_bruto+=funcionarios[i][2]
    total_imposto+=funcionarios[i][5]
    total_pagamento_liquido+=funcionarios[i][3]
for i in range(volume):
    print(f'Funcionario: {funcionarios[i][0]}\nSalário Bruto: R${round(funcionarios[i][2],2)}\nSalário liquido: R${round(funcionarios[i][3],2)}\nImposto: {funcionarios[i][4]}%\nValor do imposto: R${round(funcionarios[i][5],2)}\n')
print(f'Total de horas trabalhadas: {total_horas} horas\nTotal da folha de pagamento bruto: R${round(total_pagamento_bruto,2)}\nTotal de imposto: R${round(total_imposto,2)}\nFolha de pagamento liquida total: R${round(total_pagamento_liquido,2)}')