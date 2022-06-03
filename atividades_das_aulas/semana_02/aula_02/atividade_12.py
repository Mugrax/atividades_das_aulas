quantidade_de_mensagens=int(input())
Plano_Básico=5
if quantidade_de_mensagens>60 and quantidade_de_mensagens<=180:
    quantidade_taxada=quantidade_de_mensagens-60
    Plano_Básico=quantidade_taxada*0.05+5
elif quantidade_de_mensagens>180:
    taxa_fixa=120*0.05
    quantidade_taxada=quantidade_de_mensagens-180
    Plano_Básico=quantidade_taxada*0.10+5+taxa_fixa
inposto=Plano_Básico*0.12
valor_total=Plano_Básico+inposto
print(f'Valor a se pagar:R${valor_total}')
print(f'Valor sem inposto:R${Plano_Básico}')
print(f'Valor do inposto:R${inposto}')
print(f'Quantidade de mensagens:{quantidade_de_mensagens}')