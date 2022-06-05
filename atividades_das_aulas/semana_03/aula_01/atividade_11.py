populacao_pais_A=80000
populacao_pais_B=200000
taxa_de_crescimento_do_pais_A=0.03
taxa_de_crescimento_do_pais_B=0.0015
contador_anos=0
while populacao_pais_A<=populacao_pais_B:
    contador_anos+=1
    populacao_pais_A+=populacao_pais_A*taxa_de_crescimento_do_pais_A
    populacao_pais_B+=populacao_pais_B*taxa_de_crescimento_do_pais_B
print(f'{contador_anos} anos')
