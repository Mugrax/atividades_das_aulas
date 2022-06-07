S=1
n=int(input('digite um numero inteiro:\n'))
for i in range(2,n):
    variavel_N=i-1
    m=i+variavel_N
    S+=i/m
    print(f'S={round(S,2)}')