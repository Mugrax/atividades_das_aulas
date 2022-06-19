from funçoes_dados import conversor_discionario

arquivo='compras.csv'
lista=conversor_discionario('compras.csv',',')

#A opção de debito e mais usada entre homens ou mulheres?

contador_homen=0
contador_mulher=0

quantidade_lista=len(lista)

for i in range(quantidade_lista):
    sexo=lista[i]['sexo']
    pagamento=lista[i]['pagamento']
    if sexo=='M':
        if pagamento=='debito':
            contador_homen+=1
    elif sexo=='F':
        if pagamento=='debito':
            contador_mulher+=1

if contador_homen>contador_mulher:
    print('Homens')
elif contador_mulher>contador_homen:
    print('mulher')
else:
    print('empate')