import csv


def conversor_discionario(arquivos,delimitador):
    
    arquivo=open(arquivos,'r')
    tabela=csv.reader(arquivo, delimiter=delimitador)

    lista=[]
    lista+=tabela 
    discionario=[]
    indice=len(lista)

    for i in range(1,indice):
        discionario+=[{'nome':lista[i][0],'sobrenome':lista[i][1],'idade':int(lista[i][2]),
        'sexo':lista[i][3],'compra':float(lista[i][4]),'ano':int(lista[i][5]),'pagamento':lista[i][6]}]

    return discionario



def classificador(lista,indice,chave):

    classificados=[]

    for i in range(indice):

        variavel=lista[i][chave]
        indice_classificados=len(classificados)
        S_N=False
        
        for i in range(indice_classificados):
            variavel_2=classificados[i]
        
            if variavel_2==variavel:
                S_N=True

        if S_N==False:
            classificados.append(variavel)
        

    return classificados

def separador_faixa_etaria(lista):
    lista_idades=[]
    for i in lista:
        idade = i['idade']
        revisor = idade in lista_idades
        if revisor == False:
            lista_idades.append(idade)
        else:
            pass
        return lista_idades

# def separador_pagamento_idade(lista,):
#     for i in lista:
#         idade = i['idade']
#         pagamento=i['pagamento']
#         if idade>=18 and 
#         if pagamento == 'dinheiro':
#                 idades.append([1,0,0])  
#             elif pagamento == 'debito':
#                 idades.append([0,1,0])
#             elif pagamento == 'credito':
#                 idades.append([0,0,1])         
#         else:
#             for j in idades:
#                 if idade == j[0]:
#                     if pagamento == 'dinheiro':
#                         j[1]+=1   
#                     elif pagamento == 'debito':
#                         j[2]+=1  
#                     elif pagamento == 'credito':
#                         j[3]+=1                 