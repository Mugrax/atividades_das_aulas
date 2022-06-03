from distutils import core


nome_do_cliente=input('digite o nome do cliente:\n')
Quantidade_de_placas=int(input('digite a quantidade de placas:\n'))
Tipo_da_Placa=input('digite o tipo de madeira:\n')
caracteres=int(input('digite quantos caracteres:\n'))
cores=input('digite qual cor deseja:\n')
valor_minimo_por_placa=300
if Tipo_da_Placa=='angelim':
    valor_minimo_por_placa+=150
if caracteres>12:
    valor_minimo_por_placa+=((caracteres-12)*15)
if cores=='dourado' or cores=='dourada':
    valor_minimo_por_placa+=60
valor_total=valor_minimo_por_placa*Quantidade_de_placas
print(f'cliente:{nome_do_cliente}')
print(f'quantidade de placas:{Quantidade_de_placas}')
print(f'tipo de madeira:{Tipo_da_Placa}')
print(f'quantidade de caracteres{caracteres}')
print(f'cor {cores}')
print(f'valor por placa:R${(valor_minimo_por_placa)}')
print(F'valor total:R${(valor_total)}')