
import random 
with open("discionario.txt", "r") as arquivo: 
    todotexto = arquivo.read() 
    palavras = list(map(str, todotexto.split())) 
  
    
    print(random.choice(palavras))
