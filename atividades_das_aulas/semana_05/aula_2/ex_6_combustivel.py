class Bomba_Combustivel:

    def __init__(self,tipo_combustivel,valor_litro=0,quantidade_combustivel=0):
        self.comb = tipo_combustivel
        self.vl = valor_litro
        self.q_comb = quantidade_combustivel

    def abastece_por_valor(self,valor):

        quantidade = valor / self.vl
        
        if quantidade > self.q_comb:
            print('quantidade de combustivel insuficiente')
        else:
            self.q_comb-=quantidade
            print(f'Foi colocado: {round(quantidade,2)} Litros')

    def abastecer_por_litro(self,quantidade_litros):

        valor_pagar = quantidade_litros * self.vl

        if quantidade_litros > self.q_comb:
            print('quantidade de combustivel insuficiente')
        else:
            self.q_comb-=quantidade_litros
            print(f'Valor a ser pago: R${round(valor_pagar,2)}')
    
    def alterar_valor(self,valor):
        self.vl = valor

    def alterar_combustivel(self,combustivel):
        self.comb = combustivel

    def alterar_quantidade_combustivel(self,quantidade_colocada):
        self.q_comb+=quantidade_colocada

