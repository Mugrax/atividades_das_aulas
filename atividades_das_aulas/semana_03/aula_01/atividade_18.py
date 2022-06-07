soma=0
lista=[]
freio=0
contador_valor_positivo=0
contador_valor_negativo=0
while freio==0:
    pedido=input('digite o numero ou digite stop quando desejar parar:\n')
    if pedido=='stop':
        freio+=1
    else:
        pedido=int(pedido)
        if pedido<0:
            contador_valor_negativo+=1
            lista+=[pedido]
        elif pedido>0:
            contador_valor_positivo+=1
            lista+=[pedido]
tamanho_da_lista=len(lista)
for i in (lista):
    soma+=i
media_dos_valores=soma/tamanho_da_lista
porcentagem_de_valor_negativo=(contador_valor_negativo*100)/tamanho_da_lista
porcentagem_de_valor_positivo=(contador_valor_positivo*100)/tamanho_da_lista
print(soma)
print( f'média dos valores:{round(media_dos_valores,2)}')
print( f'quantidade de valores positivos:{contador_valor_positivo}')
print( f'quantidade de valores negativos:{contador_valor_negativo}')
print( f'percentual de valores positivos:{porcentagem_de_valor_positivo}%')
print( f'percentual de valores negativos:{porcentagem_de_valor_negativo}%')