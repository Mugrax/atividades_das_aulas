num=int(input('informe um valor:\n'))
fatorial=1
for n in range(num, 1,-1):
    fatorial=fatorial*n
print(f'{num}!={fatorial}')