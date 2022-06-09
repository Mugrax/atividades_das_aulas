nomes=[]
medias=[]
for i in range(3):
    nome=input('digite seu nome:')
    nota1=float(input('digite a nota 1:'))
    nota2=float(input('digite a nota 2:'))
    media=(nota1+nota2)/2
    nomes.append(nome)
    medias.append(media)
for i in range(3):
    if medias[i]>=7:
        print(f'\nnome:{nomes[i]}\n media: {medias[i]}')
