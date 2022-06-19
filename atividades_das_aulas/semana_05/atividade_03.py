
from funçoes_dados import conversor_discionario

arquivo='compras.csv'
lista=conversor_discionario(arquivo,',')

#percentual de homen e mulheres

quantidade_de_pessoas=len(lista)
contador_homen=0
contador_mulher=0

for i in range(quantidade_de_pessoas):
    sexo=lista[i]['sexo']
    if sexo=='M':
        contador_homen+=1
    else:
        contador_mulher+=1

porcentagem_homen=(contador_homen*100)/quantidade_de_pessoas
porcetagem_mulher=(contador_mulher*100)/quantidade_de_pessoas

print(f'Homen:{porcentagem_homen}%\nMulheres:{porcetagem_mulher}%')