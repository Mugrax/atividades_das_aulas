from re import T


temperatura=float(input('digite a temperatura:\n'))
if temperatura<=15:
    print('muito frio')
elif temperatura>15 and temperatura<=22:
    print('frio')
elif temperatura>22 and temperatura<=26:
    print('agradável')
elif temperatura>26 and temperatura<=30:
    print('quente')
else:
    print('muito quente')
