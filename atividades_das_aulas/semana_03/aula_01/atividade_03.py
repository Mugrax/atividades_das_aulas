n=int(input('digite um número inteiro e positivo:'))
somatorio=1
for i in range(1,n + 1):
    fatorial=1
    for valor in range(i, 1,-1):
        fatorial=fatorial*valor
    somatorio=somatorio+1/fatorial
print(somatorio)