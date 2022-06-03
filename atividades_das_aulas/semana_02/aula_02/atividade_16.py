l1=float(input('digite os 3 lados:\n'))
l2=float(input())
l3=float(input())
if l1==l2 and l1==l3:
    print('é um triângulo equilátero')
elif l1==l2 or l1==l3 or l2==l3:
    print('é um trângulo isóceles')
else:
    print('é um triângulo escaleno')