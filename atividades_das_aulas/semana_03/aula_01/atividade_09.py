minas_gerais=0
bahia=0
rio_de_janeiro=0
for i in range(1,10 +1):
    nome=input('nome:')
    r=int(input('você ja viajou para Rio de Janeiro?\nse sim digite 1\nse nâo digite 2\n'))
    if r==1:
        rio_de_janeiro+=1
    b=int(input('você ja viajou para Bahia?\nse sim digite 1\nse nâo digite 2\n'))
    if b==1:
        bahia+=1
    m=int(input('você ja viajou para Minas Gerais?\nse sim digite 1\nse nâo digite 2\n'))
    if m==1:
        minas_gerais+=1
if rio_de_janeiro>=bahia and rio_de_janeiro>=minas_gerais:
    if rio_de_janeiro==bahia:
        if rio_de_janeiro==minas_gerais:
            print('rio de janeiro, bahia e minas gerais sâo os destinos mais visitados')
        else:
            print('rio de janeiro e bahia sâo os destinos mais visitados')
    elif rio_de_janeiro==minas_gerais:
            print('rio de janeiro e minas gerais sâo os destinos mais visitados')                       
    else:
        print('rio de janeiro é o destino mais visitado')
elif bahia>=rio_de_janeiro and bahia>=minas_gerais:
    if bahia==rio_de_janeiro:
        if bahia==minas_gerais:
            print('bahia, rio de janeiro e minas gerais sâo os destinos mais visitados')
        else:
            print('bahia e rio de janeiro sâo os destinos mais visitados')
    elif bahia==minas_gerais:
            print('bahia e minas gerais sâo os destinos mais visitados')                       
    else:
        print('bahia é o destino mais visitado')
elif minas_gerais>=rio_de_janeiro and minas_gerais>=bahia:
    if minas_gerais==rio_de_janeiro:
        if minas_gerais==bahia:
            print('minas gerais,rio de janeiro e bahia sâo os destinos mais visitados')
        else:
            print('minas gerais e rio de janeiro sâo os destinos mais visitados')
    elif minas_gerais==bahia:
            print('minas gerais e bahia sâo os destinos mais visitados')                       
    else:
        print('minas gerais é o destino mais visitado')
else:
    print('nenhum e visitado')
