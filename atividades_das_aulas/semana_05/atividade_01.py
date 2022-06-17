
from funçoes_dados import conversor_discionario

arquivo='compras.csv'
lista=conversor_discionario(arquivo,',')

maior_valor=0
indice=len(lista)

for i in range(indice):
    if maior_valor<lista[i]['compra']:
        maior_valor=lista[i]['compra']
        comprador=lista[i]['nome']

print(f'{comprador}:R${maior_valor}')
