X=float(input())
if X>50:
    X=X+45*(X/100)
else:
    X=X+30*(X/100)
print(f'Valor: R${round(X,2)}')