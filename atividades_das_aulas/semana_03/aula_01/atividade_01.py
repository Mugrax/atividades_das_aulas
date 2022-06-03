negativos=0
for var in range(5):
    a=int(input('informe o valor:'))
    if a<0:
        negativos+=1
print(f'negativos:{negativos} ')