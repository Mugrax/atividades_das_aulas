from random import randint


def gerador_quadrado():
    quadrado=[[randint(1,9) for i in range(3)]for i in range(3)]
    return quadrado
    
def verificacao_soma(quadrado):
    
    linha_1=(quadrado[0][0]+quadrado[0][1]+quadrado[0][2])
    linha_2=(quadrado[1][0]+quadrado[1][1]+quadrado[1][2])
    linha_3=(quadrado[2][0]+quadrado[2][1]+quadrado[2][2])
    
    coluna_1=(quadrado[0][0]+quadrado[1][0]+quadrado[2][0])
    coluna_2=(quadrado[0][1]+quadrado[1][1]+quadrado[2][1])
    coluna_3=(quadrado[0][2]+quadrado[1][2]+quadrado[2][2])

    diagonal_1=(quadrado[0][0]+quadrado[1][1]+quadrado[2][2])
    diagonal_2=(quadrado[0][2]+quadrado[1][1]+quadrado[2][0])
    print(quadrado)
    if diagonal_1==diagonal_2:
        if linha_1==linha_2 and linha_1==linha_3:
            if coluna_1==coluna_2 and coluna_1==coluna_3:
                print(quadrado)
                return 'vc obteve um quadrado magico'
            else:
                print(quadrado)
                return verificacao_soma(gerador_quadrado())
        else:
            print(quadrado)
            return verificacao_soma(gerador_quadrado())
    else:
        print(quadrado)
        return verificacao_soma(gerador_quadrado())

y=verificacao_soma(gerador_quadrado())
print(y)