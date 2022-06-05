D=int(input('digite os dias:\n'))
M=int(input('digite os meses:\n'))
A=int(input('digite os anos:\n'))
AR=A/4%1
if AR==0:
    if A>2022:
        print('data inválida')
    elif M==1 or M==3 or M==5 or M==7 or M==8 or M==10:
        if D in range(1,30):
            D+=1
            print(f'{D}/{M}/{A}') 
        elif D==31:
            M+=1
            D=1
            print(f'{D}/{M}/{A}') 
    elif M==2:
        if D in range(1,28):
            D+=1
            print(f'{D}/{M}/{A}') 
        elif D==29:
            M+=1
            D=1
            print(f'{D}/{M}/{A}') 
        elif D==30 or D==31:
            print('data invalida')
    elif M==4 or M==6 or M==9 or M==11:
        if D in range (1,29):
            D+=1
            print(f'{D}/{M}/{A}') 
        elif D==30:
             M+=1
             D=1
             print(f'{D}/{M}/{A}') 
        elif D==31:
            print('data invalida')
    elif M==12:      
        if D==31:
            A+=1
            M=1
            D=1
            print(f'{D}/{M}/{A}') 
        elif D in range(1,30):
            D+=1
            print(f'{D}/{M}/{A}') 
    elif M>13:
        print('data inválida')     
elif AR!=0:
    if M==1 or M==3 or M==5 or M==7 or M==8 or M==10:
        if D in range(1,30):
            D+=1
            print(f'{D}/{M}/{A}') 
        elif D==31:
            M+=1
            D=1
            print(f'{D}/{M}/{A}') 
    elif M==2:
        if D in range(1,27):
            D+=1
            print(f'{D}/{M}/{A}') 
        elif D==28:
            M+=1
            D=1
            print(f'{D}/{M}/{A}') 
        elif D==29 or D==30 or D==31:
            print('data invalida')
    elif M==4 or M==6 or M==9 or M==11:
        if D in range (1,29):
            D+=1
            print(f'{D}/{M}/{A}') 
        elif D==30:
             M+=1
             D=1
             print(f'{D}/{M}/{A}') 
        elif D==31:
            print('data invalida')
    elif M==12:      
        if D==31:
            A+=1
            M=1
            D=1
            print(f'{D}/{M}/{A}') 
        elif D in range(1,30):
            D+=1
            print(f'{D}/{M}/{A}') 
    elif M>13:
        print('data inválida')