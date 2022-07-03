
from funçoes_dados import conversor_discionario

arquivo='compras.csv'
lista=conversor_discionario(arquivo,',')

#qual foi o gasto por ano?

# quantidade_da_lista=len(lista)

# lista_ano_2005=[]
# lista_ano_2006=[]
# lista_ano_2007=[]
# lista_ano_2008=[]
# lista_ano_2009=[]
# lista_ano_2010=[]
# lista_ano_2011=[]
# lista_ano_2012=[]
# lista_ano_2013=[]
# lista_ano_2014=[]
# lista_ano_2015=[]
# lista_ano_2016=[]
# lista_ano_2017=[]
# lista_ano_2018=[]
# lista_ano_2019=[]
# lista_ano_2020=[]

# lista_gasto_ano={2005:lista_ano_2005,2006:lista_ano_2006,2007:lista_ano_2007,
# 2008:lista_ano_2008,2009:lista_ano_2009,2010:lista_ano_2010,2011:lista_ano_2011,
# 2012:lista_ano_2012,2013:lista_ano_2013,2014:lista_ano_2014,2015:lista_ano_2015,
# 2016:lista_ano_2016,2017:lista_ano_2017,2018:lista_ano_2018,2019:lista_ano_2019,
# 2020:lista_ano_2020}

# for i in range(quantidade_da_lista):
#     ano=lista[i]['ano']
#     valor_gasto=lista[i]['compra']
#     if ano==2005:
#         lista_ano_2005.append(valor_gasto)
#     elif ano==2006:
#         lista_ano_2006.append(valor_gasto)
#     elif ano==2007:
#         lista_ano_2007.append(valor_gasto)
#     elif ano==2008:
#         lista_ano_2008.append(valor_gasto)
#     elif ano==2009:
#         lista_ano_2009.append(valor_gasto)
#     elif ano==2010:
#         lista_ano_2010.append(valor_gasto)
#     elif ano==2011:
#         lista_ano_2011.append(valor_gasto)
#     elif ano==2012:
#         lista_ano_2012.append(valor_gasto)
#     elif ano==2013:
#         lista_ano_2013.append(valor_gasto)
#     elif ano==2014:
#         lista_ano_2014.append(valor_gasto)
#     elif ano==2015:
#         lista_ano_2015.append(valor_gasto)
#     elif ano==2016:
#         lista_ano_2016.append(valor_gasto)
#     elif ano==2017:
#         lista_ano_2017.append(valor_gasto)
#     elif ano==2018:
#         lista_ano_2018.append(valor_gasto)
#     elif ano==2019:
#         lista_ano_2019.append(valor_gasto)
#     elif ano==2020:
#         lista_ano_2020.append(valor_gasto)

# quantidade_de_anos=len(lista_gasto_ano)
# quantidade_05=len(lista_ano_2005)
# quantidade_06=len(lista_ano_2006)
# quantidade_07=len(lista_ano_2007)
# quantidade_08=len(lista_ano_2008)
# quantidade_09=len(lista_ano_2009)
# quantidade_10=len(lista_ano_2010)
# quantidade_11=len(lista_ano_2011)
# quantidade_12=len(lista_ano_2012)
# quantidade_13=len(lista_ano_2013)
# quantidade_14=len(lista_ano_2014)
# quantidade_15=len(lista_ano_2015)
# quantidade_16=len(lista_ano_2016)
# quantidade_17=len(lista_ano_2017)
# quantidade_18=len(lista_ano_2018)
# quantidade_19=len(lista_ano_2019)
# quantidade_20=len(lista_ano_2020)

# gasto_anual_05=0
# gasto_anual_06=0
# gasto_anual_07=0
# gasto_anual_08=0
# gasto_anual_09=0
# gasto_anual_10=0
# gasto_anual_11=0
# gasto_anual_12=0
# gasto_anual_13=0
# gasto_anual_14=0
# gasto_anual_15=0
# gasto_anual_16=0
# gasto_anual_17=0
# gasto_anual_18=0
# gasto_anual_19=0
# gasto_anual_20=0

# for i in range(quantidade_05):
#     gasto_anual_05+=lista_ano_2005[i]
# for i in range(quantidade_06):
#     gasto_anual_06+=lista_ano_2006[i]
# for i in range(quantidade_07):
#     gasto_anual_07+=lista_ano_2007[i]
# for i in range(quantidade_08):
#     gasto_anual_08+=lista_ano_2008[i]
# for i in range(quantidade_09):
#     gasto_anual_09+=lista_ano_2009[i]
# for i in range(quantidade_10):
#     gasto_anual_10+=lista_ano_2010[i]
# for i in range(quantidade_11):
#     gasto_anual_11+=lista_ano_2011[i]
# for i in range(quantidade_12):
#     gasto_anual_12+=lista_ano_2012[i]
# for i in range(quantidade_13):
#     gasto_anual_13+=lista_ano_2013[i]
# for i in range(quantidade_14):
#     gasto_anual_14+=lista_ano_2014[i]
# for i in range(quantidade_15):
#     gasto_anual_15+=lista_ano_2015[i]
# for i in range(quantidade_16):
#     gasto_anual_16+=lista_ano_2016[i]
# for i in range(quantidade_17):
#     gasto_anual_17+=lista_ano_2017[i]
# for i in range(quantidade_18):
#     gasto_anual_18+=lista_ano_2018[i]
# for i in range(quantidade_19):
#     gasto_anual_19+=lista_ano_2019[i]
# for i in range(quantidade_20):
#     gasto_anual_20+=lista_ano_2020[i]

# gasto_total_por_ano=gasto_anual_05+gasto_anual_06+gasto_anual_07+gasto_anual_08+gasto_anual_09+gasto_anual_10+gasto_anual_11+gasto_anual_12+gasto_anual_13
# +gasto_anual_14+gasto_anual_15+gasto_anual_16+gasto_anual_17+gasto_anual_18+gasto_anual_19+gasto_anual_20/quantidade_de_anos

# print(f'Gasto do ano de 2005:\nR${round(gasto_anual_05,2)}\n')
# print(f'Gasto do ano de 2006:\nR${round(gasto_anual_06,2)}\n')
# print(f'Gasto do ano de 2007:\nR${round(gasto_anual_07,2)}\n')
# print(f'Gasto do ano de 2008:\nR${round(gasto_anual_08,2)}\n')
# print(f'Gasto do ano de 2009:\nR${round(gasto_anual_09,2)}\n')
# print(f'Gasto do ano de 2010:\nR${round(gasto_anual_10,2)}\n')
# print(f'Gasto do ano de 2011:\nR${round(gasto_anual_11,2)}\n')
# print(f'Gasto do ano de 2012:\nR${round(gasto_anual_12,2)}\n')
# print(f'Gasto do ano de 2013:\nR${round(gasto_anual_13,2)}\n')
# print(f'Gasto do ano de 2014:\nR${round(gasto_anual_14,2)}\n')
# print(f'Gasto do ano de 2015:\nR${round(gasto_anual_15,2)}\n')
# print(f'Gasto do ano de 2016:\nR${round(gasto_anual_16,2)}\n')
# print(f'Gasto do ano de 2017:\nR${round(gasto_anual_17,2)}\n')
# print(f'Gasto do ano de 2018:\nR${round(gasto_anual_18,2)}\n')
# print(f'Gasto do ano de 2019:\nR${round(gasto_anual_19,2)}\n')
# print(f'Gasto do ano de 2020:\nR${round(gasto_anual_20,2)}\n')

# print(f'Gasto média total por ano:R${round(gasto_total_por_ano,2)}\n')

anos={}

for i in lista:
    chave=i['ano']
    if chave not in anos:
        anos[chave]=0
    anos[chave]+=i['compra']

sorted(anos.items())

print(sorted(anos.items()))