from random import randint

tabuleiro = [[0 for i in range(20)] for i in range(20)]

for i in range(0,19):
    coluna=randint(0,19)
    tabuleiro[i][coluna]=1
tentativas=0
acertos=0
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
        tabuleiro[posiçao_vertical][posiçao_horizontal]=2
        print('Você acertou!!')
    elif tabuleiro[posiçao_vertical][posiçao_horizontal]==0:
        print('Você errou...')
    elif tabuleiro[posiçao_vertical][posiçao_horizontal]==2:
        tentativas-=1
        print('Aqui jas um navio(nenhum ponto de tentativa foi gasto)')
if acertos==20:
    print('Você ganhou!!')
elif tentativas==35:
    print('Você perdeu...')
