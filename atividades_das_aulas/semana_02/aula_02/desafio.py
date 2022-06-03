from random import randint
x=randint(0,9)
y=randint(0,9)
z=randint(0,9)
print(x,y,z)
conversor=x*100+y*10+z
palpite=int(input('digite seu palpite:\n'))
px=int(palpite/100)
py=int(palpite/10-px*10)
pz=int(palpite-px*100-py*10)
print(conversor)
print(palpite)
print(px,py,pz)
if palpite==(conversor):
    print('Você ganhou 1.000.000 de reaaais!!')
elif x==px or x==py or x==pz:
    if y==px or y==py or y==pz:
        if z==px or z==py or z==pz:
            print('você ganhou 1000 reais!')
        else:
            print('você ganhou 100 reais!')
    else:
        print('você ganhou 10 reais')
elif y==px or y==py or y==pz:
    if x==px or x==py or x==pz:
        if z==px or z==py or z==pz:
            print('você ganhou 1000 reais!')
        else:
            print('você ganhou 100 reais!')
    else:
        print('você ganhou 10 reais')
elif z==px or z==py or z==pz:
    if y==px or y==py or y==pz:
        if x==px or x==py or x==pz:
            print('você ganhou 1000 reais!')
        else:
            print('você ganhou 100 reais!')
    else:
        print('você ganhou 10 reais')
else:
    print('você não ganhou...')