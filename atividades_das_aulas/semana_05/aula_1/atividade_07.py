from funçoes_dados import conversor_discionario

arquivo='compras.csv'
lista=conversor_discionario('compras.csv',',')

#qual faixa etaria q mais gasta?

contador_jovens=0
contador_adultos=0
contador_idosos=0

indice_jovens=[]
indice_adultos=[]
indice_idosos=[]

quantidade_lista=len(lista)
for i in range(quantidade_lista):
    idade=lista[i]['idade']
    if idade>=18 and idade<=25:
        contador_jovens+=1
        indice_jovens.append(i)
    elif idade>=26 and idade<=59:
        contador_adultos+=1
        indice_adultos.append(i)
    elif idade>=60:
        contador_idosos+=1
        indice_idosos.append(i)

quantidade_jovens=len(indice_jovens)
quantidade_adultos=len(indice_adultos)
quantidade_idosos=len(indice_idosos)

valor_compra_jovens=0
valor_compra_adultos=0
valor_compra_idosos=0

for i in range(quantidade_jovens):
    indice_compra_jovens=indice_jovens[i]
    valor=lista[indice_compra_jovens]['compra']
    valor_compra_jovens+=valor

for i in range(quantidade_adultos):
    indice_compra_adultos=indice_adultos[i]
    valor=lista[indice_compra_adultos]['compra']
    valor_compra_adultos+=valor
    
for i in range(quantidade_idosos):
    indice_compra_idosos=indice_idosos[i]
    valor=lista[indice_compra_idosos]['compra']
    valor_compra_idosos+=valor

print('A faixa etária que mais gasta é:')

if valor_compra_jovens>valor_compra_adultos and valor_compra_jovens>valor_compra_idosos:
    print('Jovens')
elif valor_compra_adultos>valor_compra_jovens and valor_compra_adultos>valor_compra_idosos:
    print('Adultos')
elif valor_compra_idosos>valor_compra_jovens and valor_compra_idosos>valor_compra_adultos:
    print('Idosos')