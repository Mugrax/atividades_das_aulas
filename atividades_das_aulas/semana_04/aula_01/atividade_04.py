#exemplos usados no input
#lista1=[1,2,3,4,5,6,7,8,9,10]
#lista2=[11,12,13,14,15,16,17,18,19,20]
indice_1=0
lista1=[]
lista2=[]
print('lista 1:')
for i in range(10):
    lista1+=[int(input())]
print('lista 2')
for i in range(10):
    lista2+=[int(input())]
for i in range(0,10):
    indice_lista_2=lista2[i]
    print(indice_lista_2)
    indice_1+=1
    if indice_1>1:
        indice_1+=1
    lista1.insert(indice_1,indice_lista_2)
print(lista1)