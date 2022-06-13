from posixpath import split
from funções import validação_data
data=input('digite a data como o exemplo: 01/janeiro/2001\n')
D,M,A=data.split('/')
D=int(D)
A=int(A)
lista_mes=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
x=1+(lista_mes.index(M))
validacao=validação_data(D,x,A)
print(f'dia {D} do mês {M} do ano {A}')
print(validacao)