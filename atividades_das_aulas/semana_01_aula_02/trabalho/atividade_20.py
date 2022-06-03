QAC=float(input('Quantidade de ações compradas: \n'))
VAAC=float(input('Valor atual da ação: \n'))
TPPAC=float(input('Taxa paga pela ação: \n'))
QAV=float(input('Quantidade de ações vendidas: \n'))
VAAV=float(input('Valor atual da ação: \n'))
TPPAV=float(input('Taxa paga pela ação: \n'))
VTGCA=QAC*VAAC+QAC*TPPAC
VPTDC=QAC*TPPAC
VTGVA=QAV*VAAV
VPV=QAC*VAAV+QAC*TPPAV
VDTECV=VPV-VTGCA
print(f'Valor total gasto em compras de ações:{VTGCA}')
print(f'Valor pago em taxa durante a compra:{VPTDC}')
print(f'Valor total ganho na venda das ações:{VTGVA}')
print(f'Valor pago na venda:{VPV}')
print(f'Valor da diferença total entre compra e venda:{VDTECV}')
