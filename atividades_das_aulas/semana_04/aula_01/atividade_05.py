N=1
lista=[]
soma=0
maior=0
menor=99999999999999999999999999999999
while N>0:
    N=float(input())
    lista.append(N)
    if N>maior:
        maior=N
    if N<menor and N>=0:
        menor=N
lista.pop()
quantidade_da_lista=len(lista)
for i in range(quantidade_da_lista):
    soma+=lista[i]
media=soma/quantidade_da_lista
print(f'Soma:{round(soma,2)}')
print(f'Media:{round(media,2)}')
print(f'Maior número:{maior}\nMenor número:{menor}')

