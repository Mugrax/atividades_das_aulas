from funçoes_dados import conversor_discionario

arquivo='compras.csv'
lista=conversor_discionario('compras.csv',',')

#quantas pessoas a em cada faixa etaria?
# Jovens, 18 a 25 anos
# Adultos, 26 a 59 anos
# Idosos, igual ou maior que 60 anos

contador_jovens=0
contador_adultos=0
contador_idosos=0

quantidade_lista=len(lista)
for i in range(quantidade_lista):
    idade=lista[i]['idade']
    if idade>=18 and idade<=25:
        contador_jovens+=1
    elif idade>=26 and idade<=59:
        contador_adultos+=1
    elif idade>=60:
        contador_idosos+=1

print(f'Quantia de pessoas por faixa etária:\nJovens:{contador_jovens}\nAdultos:{contador_adultos}\nIdosos:{contador_idosos}')

