from funçoes_dados import  conversor_discionario 

arquivo='compras.csv'
lista=conversor_discionario('compras.csv',',')

#Qual o valor gasto em compras por jovens do ano de 2010 até 2015?

idades = []
lista_anos=[]
pagamento_jovens_ano=0
for i in range(6):
    x=2010+i
    lista_anos.append(x)

for i in lista:
    ano=i['ano']
    idade = i['idade']
    compras = i['compra']
    revisor = ano in lista_anos
    if revisor == True:
        if idade >= 18 and idade <=25:
            pagamento_jovens_ano+=compras

print(f'foi gasto: R${round(pagamento_jovens_ano,2)}')