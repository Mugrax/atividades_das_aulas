X=float(input('digite os 3 valores:\n'))
Y=float(input())
Z=float(input())
if X>Y and X>Z:
    print(X)
elif Y>X and Y>Z:
    print(Y)
elif Z>X and Z>Y:
    print(Z)
else:
    print('os três sao iguais')