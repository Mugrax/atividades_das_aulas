class Conta_Corrente:
    
    def __init__(self,num_conta,nome,saldo=0):
        self.num_conta = num_conta
        self.nome = nome 
        self.saldo = saldo

    def alterar_nome(self,nome):
        self.nome = nome
    
    def deposito(self,valor):
        if valor < 0:
            print('valor incorreto')
        else:
            self.saldo+=valor
    
    def saque(self,valor):
        if valor < 0:
            print('valor incorreto')
        elif valor > self.saldo:
            print(f'saldo insuficiente\n\nseu saldo é de {self.saldo}')
        else:
            self.saldo-=valor 
       
        
