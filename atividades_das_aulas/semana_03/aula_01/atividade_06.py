print('1-candidato A\n2-candidato B\n3-voto nulo\n4-voto em branco')
contador_cA=0
contador_cB=0
contador_VN=0
contador_VB=0
for x in range(5):
    y=int(input('digite o número do 1 ao 4:'))
    while y<1 or y>4 or not(y>=0) or not(y<=0):
        y=int(input('digite um número válido: '))
        input
    if y==1:
        contador_cA+=1
    elif y==2:
        contador_cB+=1
    elif y==3:
        contador_VN+=1
    elif y==4:
        contador_VB+=1
print(f'total de votos candidato A:{contador_cA}')
print(f'total de votos candidato B:{contador_cB}')
print(f'total de votos nulos:{contador_VN}')
print(f'total de votos em branco:{contador_VB}')