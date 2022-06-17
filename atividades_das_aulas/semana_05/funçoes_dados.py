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
