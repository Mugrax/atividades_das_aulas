QP=int(input('digite a quantidade comprada:'))
P=5.40
quantidade_de_desconto=int(QP/100)
VTC=QP*P
D=quantidade_de_desconto*5/10
DER=D*(VTC/100)
VTCCD=VTC-DER
print(f'Valor total da compra sem desconto: {VTC}')
print(f'A quantidade de centenas compradas desse produto é: {quantidade_de_desconto}')
print(f'O Desconto:R${round(DER,2)}')
print(f'O valor total da compra com desconto: {VTCCD}')