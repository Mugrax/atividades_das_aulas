altura=0
lista_homen_acima=[]
lista_mulher_acima=[]
lista_homen_abaixo=[]
lista_mulher_abaixo=[]
DA={
    'mulher_acima_da_media':lista_mulher_acima,
    'mulher_abaixo_da_media':lista_mulher_abaixo,
    'homen_acima_da_media':lista_homen_acima,
    'homen_abaixo_da_media':lista_homen_abaixo}
while altura>=0:
    altura=float(input('digite a altura:\n'))
    sexo=input('digite homen ou mulher:\n')
    if sexo=='mulher':
        if altura>1.60:
            lista_mulher_acima.append(altura)
        elif altura<1.60:
            lista_mulher_abaixo.append(altura)
    elif sexo=='homen':
        if altura>1.73:
            lista_homen_acima.append(altura)
        elif altura<1.73:
            lista_homen_abaixo.append(altura)
          
print(DA)

