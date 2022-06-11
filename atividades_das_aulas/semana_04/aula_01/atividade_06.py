altura=0
lista_homen_acima=[]
lista_mulher_acima=[]
lista_homen_abaixo=[]
lista_mulher_abaixo=[]
lista_nomes=[]
while altura>=0:
    altura=float(input('digite a altura:\n'))
    sexo=input('digite homen ou mulher:\n')
    if altura>=0:
        lista_nomes.append(sexo)
    if sexo=='mulher':
        if altura>=1.60:
            lista_mulher_acima.append(altura)
        elif altura<1.60:
            lista_mulher_abaixo.append(altura)
    elif sexo=='homen':
        if altura>=1.73:
            lista_homen_acima.append(altura)
        elif altura<1.73:
            lista_homen_abaixo.append(altura)
quantidade_h_ac=lista_homen_acima.count()
quantidade_h_ab=lista_homen_abaixo.count()
quantidade_m_ac=lista_mulher_acima.count()
quantidade_m_ab= lista_mulher_abaixo.count()
print(f'A {quantidade_m_ac} de mulheres acima da média de altura e {quantidade_m_ab} abaixo dessa média.')
print(f'A {quantidade_h_ac} de homens acima da média de altura e {quantidade_h_ab} abaixo dessa média.')