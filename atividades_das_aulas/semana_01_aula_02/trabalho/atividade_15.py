A=float(input('digite o preço do produto \n'))
B=float(input('Próximo Preço... \n'))
C=float(input('Próximo Preço... \n'))
D=float(input('Próximo Preço... \n'))
E=float(input('Próximo Preço... \n'))
Sub=A+B+C+D+E
Imp=Sub/100*6
VT=Imp-(-Sub)
print(f'Subtotal:{Sub}')
print(f'Imposto:{Imp}')
print(f'Valor Total:{VT}')
