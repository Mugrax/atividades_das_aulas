from random import randint

tabuleiro = [[0 for i in range(20)] for i in range(20)]

for i in range(0,19):
    coluna=randint(0,19)
    tabuleiro[i][coluna]=1
tentativas=0
acertos=0
acertos_agua=0
acertos_navios=0
contador=0
acertos_initerruptos=0
print(tabuleiro)
print('Respeitando a ideia de que seguimos as regras de tabuleiro para posições sendo de 1 a 20 verticalmente e horizontalmente.')
while tentativas<=34 and acertos<=19:
    posiçao_vertical=int(input('digite a posição vertical: '))
    posiçao_horizontal=int(input('digite a posição horizontal: '))
    posiçao_vertical-=1
    posiçao_horizontal-=1
    tentativas+=1
    if tabuleiro[posiçao_vertical][posiçao_horizontal]==1:
        acertos+=1
        contador+=1
        acertos_navios+=1
        if acertos_initerruptos<contador:
            acertos_initerruptos=contador
        tabuleiro[posiçao_vertical][posiçao_horizontal]=2
        print('Você acertou!!')
    elif tabuleiro[posiçao_vertical][posiçao_horizontal]==0:
        print('Você errou...')
        contador=0
        acertos_agua+=1
    elif tabuleiro[posiçao_vertical][posiçao_horizontal]==2:
        print('Aqui jas um navio')
        contador=0
if acertos==20:
    print('Você ganhou!!')
elif tentativas==35:
    print('Você perdeu...')
porcentagem_agua=(acertos_agua*100)/tentativas
porcentagem_navio=(acertos_navios*100)/tentativas
print('Estatísticas\n')
print(f'Acertos em águas:{acertos_agua}')
print(f'porcentagem de acertos em águas:{round(porcentagem_agua,2)}%')
print(f'Acertos em navios:{acertos_navios}')
print(f'porcentagem de acertos em navios:{round(porcentagem_navio,2)}%')
print(f'Acertos initerruptos: {acertos_initerruptos}')