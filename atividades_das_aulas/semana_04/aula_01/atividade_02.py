alunos=[]
for i in range(3):
    nome=input('digite seu nome:')
    nota1=float(input('digite a nota 1:'))
    nota2=float(input('digite a nota 2:'))
    media=(nota1+nota2)/2
    aluno={'nome':nome,'media':media}
    alunos.append(aluno)
for i in range(3):
    aluno=alunos[i]
    if aluno["media"]>=7:
        print(f'\nnome:{aluno["nome"]}\n media: {aluno["media"]}')
