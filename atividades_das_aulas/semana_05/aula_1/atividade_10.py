from funçoes_dados import conversor_discionario 

arquivo='compras.csv'
lista=conversor_discionario('compras.csv',',')

#Qual foi o ano em que os homens mais usaram o crédito?

contador=0
lista_anos=[]
anos=[]
for i in lista:
    sexo=i['sexo']
    ano=i['ano']
    pagamento=i['pagamento']
    if sexo=='M' and pagamento=='credito':
        variavel = ano in anos
        if variavel==True:
            for i in lista_anos:
                if i[1]==ano:
                    i[0]+=1
        else:
            anos.append(ano)
            lista_anos.append([1,ano]) 
print(max(lista_anos))       
        





