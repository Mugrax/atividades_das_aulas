import csv


# arquivo=open('discionario.csv','r') 
# print(arquivo)
# lines=arquivo.readlines()
# print(lines)
#------------------------------------
#atividade 10 funçao

nome_arquivo='discionario.csv'
f=open(nome_arquivo)#encoding='ufc-8')
tabela=csv.reader(f)#delimite=',')
print(list(tabela))


#------------------------------------
# lista=[]
# lista+=f
# print(lista)


