from funçoes_dados import conversor_discionario

arquivo='compras.csv'
lista=conversor_discionario(arquivo,',')

#qual sao os anos da base de dados?

indice=len(lista)
anos=[]

for i in range(indice):
    ano=lista[i]['ano']
    indice_anos=len(anos)
    S_N=False
    for i in range(indice_anos):
        ano_2=anos[i]
        if ano==ano_2:
            S_N=True
    if S_N==False:
        anos.append(ano)

anos.sort()
        
print(f'do ano {anos[0]} ao ano {anos[indice_anos-1]}\n')        
print (f'esses foram os anos \n{anos}')