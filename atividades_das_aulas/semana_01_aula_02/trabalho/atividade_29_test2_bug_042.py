V=float(input('Digite o valor aqui: \n'))
R=V%1
print(f'{V} resulta em:')
if V >= 1:
    print(f'{(int(V))} moedas de 1 real')
if R>=0.50:
    M50centavos=R/50*100
    R=R-(int(M50centavos)*50/100)
    if M50centavos >= 1:
        print(f'{int(M50centavos)} moedas de 50 centavos')
if R>=0.25:
    M25centavos=R/25*100
    R=R-(int(M25centavos)*25/100)
    if M25centavos >= 1:
        print(f'{int(M25centavos)} moedas de 25 centavos')
if R>=0.10:
    M10centavos=R/10*100
    R=R-(int(M10centavos)*10/100)
    if M10centavos >= 1:
        print(f'{int(M10centavos)} moedas de 10 centavos')   
if R>=0.5:
    M5centavos=R/5*100
    R=R-(int(M5centavos)*5/100)
    if M5centavos >= 1:
        print(f'{int(M5centavos)} moedas de 5 centavos')
if R>=0.01:
    M1centavo=R/1*100
    R=R-(int(M1centavo)*1/100)
    if M1centavo >= 1:
        print(f'{round(M1centavo)} moedas de 1 centavo')