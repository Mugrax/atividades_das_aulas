
from funçoes_dados import conversor_discionario

arquivo='compras.csv'
lista=conversor_discionario(arquivo,',')

#qual foi o gasto por ano

quantidade_da_lista=len(lista)

lista_ano_2005=[]
lista_ano_2006=[]
lista_ano_2007=[]
lista_ano_2008=[]
lista_ano_2009=[]
lista_ano_2010=[]
lista_ano_2011=[]
lista_ano_2012=[]
lista_ano_2013=[]
lista_ano_2014=[]
lista_ano_2015=[]
lista_ano_2016=[]
lista_ano_2017=[]
lista_ano_2018=[]
lista_ano_2019=[]
lista_ano_2020=[]

lista_gasto_ano={2005:lista_ano_2005,2006:lista_ano_2006,2007:lista_ano_2007,
2008:lista_ano_2008,2009:lista_ano_2009,2010:lista_ano_2010,2011:lista_ano_2011,
2012:lista_ano_2012,2013:lista_ano_2013,2014:lista_ano_2014,2015:lista_ano_2015,
2016:lista_ano_2016,2017:lista_ano_2017,2018:lista_ano_2018,2019:lista_ano_2019,
2020:lista_ano_2020}

for i in range(quantidade_da_lista):
    ano=lista[i]['ano']
    valor_gasto=lista[i]['compra']
    if ano==2005:
        lista_ano_2005.append(valor_gasto)
    elif ano==2006:
        lista_ano_2006.append(valor_gasto)
    elif ano==2007:
        lista_ano_2007.append(valor_gasto)
    elif ano==2008:
        lista_ano_2008.append(valor_gasto)
    elif ano==2009:
        lista_ano_2009.append(valor_gasto)
    elif ano==2010:
        lista_ano_2010.append(valor_gasto)
    elif ano==2011:
        lista_ano_2011.append(valor_gasto)
    elif ano==2012:
        lista_ano_2012.append(valor_gasto)
    elif ano==2013:
        lista_ano_2013.append(valor_gasto)
    elif ano==2014:
        lista_ano_2014.append(valor_gasto)
    elif ano==2015:
        lista_ano_2015.append(valor_gasto)
    elif ano==2016:
        lista_ano_2016.append(valor_gasto)
    elif ano==2017:
        lista_ano_2017.append(valor_gasto)
    elif ano==2018:
        lista_ano_2018.append(valor_gasto)
    elif ano==2019:
        lista_ano_2019.append(valor_gasto)
    elif ano==2020:
        lista_ano_2020.append(valor_gasto)

quantidade_de_anos=len(lista_gasto_ano)
quantidade_05=len(lista_ano_2005)
quantidade_06=len(lista_ano_2006)
quantidade_07=len(lista_ano_2007)
quantidade_08=len(lista_ano_2008)
quantidade_09=len(lista_ano_2009)
quantidade_10=len(lista_ano_2010)
quantidade_11=len(lista_ano_2011)
quantidade_12=len(lista_ano_2012)
quantidade_13=len(lista_ano_2013)
quantidade_14=len(lista_ano_2014)
quantidade_15=len(lista_ano_2015)
quantidade_16=len(lista_ano_2016)
quantidade_17=len(lista_ano_2017)
quantidade_18=len(lista_ano_2018)
quantidade_19=len(lista_ano_2019)
quantidade_20=len(lista_ano_2020)

gasto_anual_05=0
gasto_anual_06=0
gasto_anual_07=0
gasto_anual_08=0
gasto_anual_09=0
gasto_anual_10=0
gasto_anual_11=0
gasto_anual_12=0
gasto_anual_13=0
gasto_anual_14=0
gasto_anual_15=0
gasto_anual_16=0
gasto_anual_17=0
gasto_anual_18=0
gasto_anual_19=0
gasto_anual_20=0

lista_de_gastos_por_ano=[]

for i in range(quantidade_05):
    gasto_anual_05+=lista_ano_2005[i]

lista_de_gastos_por_ano.append(gasto_anual_05)

for i in range(quantidade_06):
    gasto_anual_06+=lista_ano_2006[i]

lista_de_gastos_por_ano.append(gasto_anual_06)

for i in range(quantidade_07):
    gasto_anual_07+=lista_ano_2007[i]

lista_de_gastos_por_ano.append(gasto_anual_07)

for i in range(quantidade_08):
    gasto_anual_08+=lista_ano_2008[i]

lista_de_gastos_por_ano.append(gasto_anual_08)

for i in range(quantidade_09):
    gasto_anual_09+=lista_ano_2009[i]

lista_de_gastos_por_ano.append(gasto_anual_09)

for i in range(quantidade_10):
    gasto_anual_10+=lista_ano_2010[i]

lista_de_gastos_por_ano.append(gasto_anual_10)

for i in range(quantidade_11):
    gasto_anual_11+=lista_ano_2011[i]

lista_de_gastos_por_ano.append(gasto_anual_11)

for i in range(quantidade_12):
    gasto_anual_12+=lista_ano_2012[i]

lista_de_gastos_por_ano.append(gasto_anual_12)

for i in range(quantidade_13):
    gasto_anual_13+=lista_ano_2013[i]

lista_de_gastos_por_ano.append(gasto_anual_13)

for i in range(quantidade_14):
    gasto_anual_14+=lista_ano_2014[i]

lista_de_gastos_por_ano.append(gasto_anual_14)

for i in range(quantidade_15):
    gasto_anual_15+=lista_ano_2015[i]

lista_de_gastos_por_ano.append(gasto_anual_15)

for i in range(quantidade_16):
    gasto_anual_16+=lista_ano_2016[i]
    
lista_de_gastos_por_ano.append(gasto_anual_16)

for i in range(quantidade_17):
    gasto_anual_17+=lista_ano_2017[i]

lista_de_gastos_por_ano.append(gasto_anual_17)

for i in range(quantidade_18):
    gasto_anual_18+=lista_ano_2018[i]

lista_de_gastos_por_ano.append(gasto_anual_18)

for i in range(quantidade_19):
    gasto_anual_19+=lista_ano_2019[i]

lista_de_gastos_por_ano.append(gasto_anual_19)

for i in range(quantidade_20):
    gasto_anual_20+=lista_ano_2020[i]

lista_de_gastos_por_ano.append(gasto_anual_20)

maior_gasto_anual=0

for num,i in enumerate(range(quantidade_de_anos)):
    if maior_gasto_anual<lista_de_gastos_por_ano[i]:
        maior_gasto_anual=lista_de_gastos_por_ano[i]
        numero=num

if num==0:
    num_ano=2005
elif num==1:
    num_ano=2006
elif num==2:
    num_ano=2007
elif num==3:
    num_ano=2008
elif num==4:
    num_ano=2009
elif num==5:
    num_ano=2010
elif num==6:
    num_ano=2011
elif num==7:
    num_ano=2012
elif num==8:
    num_ano=2013
elif num==9:
    num_ano=2014
elif num==10:
    num_ano=2015
elif num==11:
    num_ano=2016
elif num==12:
    num_ano=2017
elif num==13:
    num_ano=2018
elif num==14:
    num_ano=2019
elif num==15:
    num_ano=2020

print(f'O ano com maior gasto foi {num_ano}\nCom o valor de:R${round(maior_gasto_anual,2)}')
