from random import randint


l = [[0 for i in range(20)] for i in range(20)]
i=randint(1,19)
l[i][5]=1
print(l)