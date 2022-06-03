N=int(input('digitar um número até 3 digitos:'))
NC=N/100
NU=N%10
ND=(N%100-NU)/10
print(f'{N} tem {int(NC)} centenas, {int(ND)} dezenas e {NU} unidades.')