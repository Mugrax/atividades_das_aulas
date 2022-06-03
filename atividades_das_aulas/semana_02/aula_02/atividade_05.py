Quantidade=int(input('digite quantidade adquirida:\n'))
preço_unitario=float(input('digite o preço unitário:\n'))
total=Quantidade*preço_unitario
if Quantidade<=5:
    desconto=0.02
elif Quantidade>5 and Quantidade<=10:
    desconto=0.03
else:
    desconto=0.05
total_a_pagar=total-(total*desconto)
print(f'total a pagar:R${round(total_a_pagar,2)}')