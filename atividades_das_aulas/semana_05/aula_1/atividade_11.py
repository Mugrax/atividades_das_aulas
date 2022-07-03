from funçoes_dados import conversor_discionario 

arquivo='compras.csv'
lista=conversor_discionario('compras.csv',',')

#Qual opção de pagamento é mais utilizada em cada faixa etária?

#indice : 0 = idade / 1 = dinheiro / 2 = debito / 3 = credito

idades = []
lista_idades=[]

for i in lista:
    idade = i['idade']
    pagamento = i['pagamento']
    revisor = idade in lista_idades
    if revisor == False:
        lista_idades.append(idade)
        if pagamento == 'dinheiro':
            idades.append([idade,1,0,0])  
        elif pagamento == 'debito':
            idades.append([idade,0,1,0])
        elif pagamento == 'credito':
            idades.append([idade,0,0,1])         
    else:
        for j in idades:
            if idade == j[0]:
                if pagamento == 'dinheiro':
                    j[1]+=1   
                elif pagamento == 'debito':
                    j[2]+=1  
                elif pagamento == 'credito':
                    j[3]+=1                 

jovens=[]
adultos=[]
idosos=[]

# Jovens, 18 a 25 anos
# Adultos, 26 a 59 anos
# Idosos, igual ou maior que 60 anos

for i in idades:
    if i[0]>= 18 and i[0]<=25:
        jovens.append(i[1:4])
    elif i[0]>= 26 and i[0]<=59:
        adultos.append(i[1:4])
    elif i[0]>= 60:
        idosos.append(i[1:4])

for i in jovens:
    x=max(i)
    if x == i[0]:
        maior_pagamento_jovens='dinheiro'
    elif x == i[1]:
        maior_pagamento_jovens='debito'
    if x == i[2]:
        maior_pagamento_jovens='credito'

print(f'\nA opção de pagamento mais usada pelos jovens é {maior_pagamento_jovens}\n')

for i in adultos:
    x=max(i)
    if x == i[0]:
        maior_pagamento_adultos='dinheiro'
    elif x == i[1]:
        maior_pagamento_adultos='debito'
    elif x == i[2]:
        maior_pagamento_adultos='credito'

print(f'A opção de pagamento mais usada pelos adultos é {maior_pagamento_adultos}\n')

for i in idosos:
    x=max(i)
    if x == i[0]:
        maior_pagamento_idosos='dinheiro'
    elif x == i[1]:
        maior_pagamento_idosos='debito'
    elif x == i[2]:
        maior_pagamento_idosos='credito'

print(f'A opção de pagamento mais usada pelos idosos é {maior_pagamento_idosos}\n')
        