contador_repeticao=0
media_de_idade=0
contador_jovens=0
#<18
media_salario_jovens=0
contador_adultos=0
#18>= a <60
media_salario_adultos=0
contador_idosos=0
#>=60
media_salario_idosos=0
while contador_repeticao<10:
    idade=int(input('idade: '))
    salario=float(input('salário: '))
    contador_repeticao+=1
    media_de_idade+=idade
    if idade<18:
        contador_jovens+=1
        media_salario_jovens+=salario
    elif idade>=18 and idade<60:
        contador_adultos+=1
        media_salario_adultos+=salario
    elif idade>=60:
        contador_idosos+=1
        media_salario_idosos+=salario
media_de_idade/=contador_repeticao+1
media_salario_jovens/=contador_jovens    
media_salario_adultos/=contador_adultos
media_salario_idosos/=contador_idosos
print(f'Media de idade:{round(media_de_idade,2)}')
print(f'jovens:{contador_jovens}\nadultos:{contador_adultos}\nidosos:{contador_idosos}')
if media_salario_jovens>media_salario_adultos and media_salario_jovens>media_salario_idosos:
    print('os jovens acumulam maior salário.')
elif media_salario_adultos>media_salario_jovens and media_salario_adultos>media_salario_idosos:
    print('os adultos acumulam maior salário.')
elif media_salario_idosos>media_salario_jovens and media_salario_idosos>media_salario_adultos:
    print('os idosos acumulam o maior salário.')
elif media_salario_jovens==media_salario_adultos:
    print('jovens e adultos partilham de maior salário.')
elif media_salario_jovens==media_salario_idosos:
    print('jovens e idosos partilham de maior salário.')
elif media_salario_adultos==media_salario_idosos:
    print('adultos e idosos partilham de maior salário.')
elif media_salario_jovens==media_salario_adultos and media_salario_jovens==media_salario_idosos:
    print('as três faixas etárias acumulam o maior salário.')
else:
    print('erro')