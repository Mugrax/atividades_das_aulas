Custo_de_fabrica=float(input('digite o valor do custo de fábrica:'))
Percentual_do_distribuidor=Custo_de_fabrica*0.28
inpostos=Custo_de_fabrica*0.45
custo_final=Custo_de_fabrica+Percentual_do_distribuidor+inpostos
print(f'R${round(custo_final,2)}')