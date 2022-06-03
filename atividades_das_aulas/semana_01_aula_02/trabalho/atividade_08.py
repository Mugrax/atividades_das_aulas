VPF=float(input('Valor do pão francês \n'))
VPD=float(input('Valor do pão doce \n'))
VQ=float(input('Valor do Quindin \n'))
PF=float(input('Quantos Pães Francêses foram vendidos hoje? \n'))
PD=float(input('Quantos Pães Doces foram vendidos hoje? \n'))
Q=float(input('Quantos Quindins foram vendidos hoje? \n'))
TF=PF*VPF+PD*VPD+Q*VQ
TFI=TF/100*95
Tpoupanca=TFI/100*10
I=TF/100*5
print(f'faturamento R${TF}')
print(f'total a ser guardado R${Tpoupanca}')
print(f'imposto descontado R${I}')