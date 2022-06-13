def contador_de_espaços(x=''):
    x=list(x)
    contagem=x.count(' ')
    return contagem
x='pao de batata'
contagem=contador_de_espaços(x)
print(contagem)