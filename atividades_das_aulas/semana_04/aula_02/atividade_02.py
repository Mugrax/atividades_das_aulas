def julgamento(x):
    if x>0:
        R='P'
    else:
        R='N'
    return R
x=float(input('digite um número: '))
R=julgamento(x)
print(R)