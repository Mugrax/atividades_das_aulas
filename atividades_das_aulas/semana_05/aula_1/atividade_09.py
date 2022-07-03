from funçoes_dados import classificador, conversor_discionario 

arquivo='compras.csv'
lista=conversor_discionario('compras.csv',',')

#qual sobrenome aparece mais na base de dados?

quantidade_lista=len(lista)

sobrenomes=classificador(lista,quantidade_lista,'sobrenome')

quantidade_sobrenomes=len(sobrenomes)
quantidade_maior=0
for i in range(quantidade_sobrenomes):
    
    classificado_sobrenome=sobrenomes[i]
    contador_temporario=0
    
    for j in range(quantidade_lista):
        sobrenome_lista=lista[j]['sobrenome']

        if classificado_sobrenome==sobrenome_lista:
            contador_temporario+=1
        
        if contador_temporario>quantidade_maior:
            quantidade_maior=contador_temporario
            indice=i
            

sobrenome_com_maior_quantidade=sobrenomes[indice]

print(f'\nO sobrenome com maior repetição é: {sobrenome_com_maior_quantidade} e repetiu {quantidade_maior} vezes\n')
    