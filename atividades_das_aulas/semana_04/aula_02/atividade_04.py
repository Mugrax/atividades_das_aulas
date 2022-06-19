def quadro(linhas,colunas):
    if linhas<=1:
        linhas=1
    elif linhas>=20:
        linhas=20
    if colunas<=1:
        colunas=1
    elif colunas>=20:
        colunas=20
    coluna='+'
    linha='|'
    for i in range(colunas):
        coluna+='-'
        linha+=' '
    coluna+='+\n'
    linha+='|\n'
    linha*=linhas
    quadro=coluna+linha+coluna
    return quadro
x=quadro(5,20)
print(x)
print('+--------------------+')