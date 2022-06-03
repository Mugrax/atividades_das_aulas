contador_repeticao=0
menor_valor=0
maior_valor=0
while contador_repeticao<10:
    valor=float(input())
    contador_repeticao+=1
    if valor>maior_valor:
        maior_valor=valor
    if valor<menor_valor:
        menor_valor=valor
print(f'Maior valor:{maior_valor}\n Menor valor:{menor_valor}')