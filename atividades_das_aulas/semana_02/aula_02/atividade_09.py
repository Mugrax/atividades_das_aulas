D=int(input('digite os dias:\n'))
M=int(input('digite os meses:\n'))
A=int(input('digite os anos:\n'))
A=A/4%1
V=1
if A==0:
    if M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12:
        if D in range(1,31):
            V=2
    elif M==2:
        if D in range(1,29):
            V=2
    elif M==4 or M==6 or M==9 or M==11:
        if D in range (1,30):
            V=2  
elif A!=0:
    if M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12:
        if D in range(1,31):
            V=2
    elif M==2:
        if D in range(1,28):
            V=2
    elif M==4 or M==6 or M==9 or M==11:
        if D in range (1,30):
            V=2
if V==1:
    print('data inválida')
elif V==2:
    print('data válida')