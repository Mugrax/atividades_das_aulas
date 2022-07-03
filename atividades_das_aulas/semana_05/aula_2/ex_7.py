class Carro:
    
    def __init__(self,consumo,combustivel=0):
        self.consumo = consumo 
        self.combustivel = combustivel

    def andar(self,distancia):
        self.combustivel-=distancia / self.consumo

    def obter_gasolina(self):
        print(f'{round(self.combustivel,2)} litros')

    def adicionar_gasolina(self,gasolina):
        self.combustivel+=gasolina

meu_fusca = Carro(15)
meu_fusca.adicionar_gasolina(20)
meu_fusca.andar(100)
meu_fusca.obter_gasolina()