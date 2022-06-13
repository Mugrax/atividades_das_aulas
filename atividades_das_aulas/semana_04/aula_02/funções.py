def validação_data(D,M,A):
    AR=A/4%1
    if AR==0:
        if A>2022:
            return 'data inválida'
        elif M==1 or M==3 or M==5 or M==7 or M==8 or M==10:
            if D in range(1,30):
                return 'Válido'
            elif D==31:
                return 'Válido' 
        elif M==2:
            if D in range(1,28):
                return 'Válido'
            elif D==29:
                return 'Válido' 
            elif D==30 or D==31:
                return 'data invalida'
        elif M==4 or M==6 or M==9 or M==11:
            if D in range (1,29):
                return 'Válido'
            elif D==30:
                return 'Válido'
            elif D==31:
                return 'data invalida'
        elif M==12:      
            if D==31:
                return 'Válido'
            elif D in range(1,30):
                return 'Válido'
        elif M>13:
            return 'data inválida'     
    elif AR!=0:
        if A>2022:
            return 'data inválida'
        elif M==1 or M==3 or M==5 or M==7 or M==8 or M==10:
            if D in range(1,30):
                return 'Válido'
            elif D==31:
                return 'Válido'
        elif M==2:
            if D in range(1,27):
                return 'Válido' 
            elif D==28:
                return 'Válido'
            elif D==29 or D==30 or D==31:
                return 'data inválida'
        elif M==4 or M==6 or M==9 or M==11:
            if D in range (1,29):
                return 'Válido'
            elif D==30:
                return 'Válido'
            elif D==31:
                return 'data invalida'
        elif M==12:      
            if D==31:
                return 'Válido'
            elif D in range(1,30):
                return 'Válido'
        elif M>13:
            return 'data inválida'