class Bola:

    def __init__(self,cor,circunferencia,material):
        self.x = cor
        self.y = circunferencia
        self.z = material

    def troca_cor(self,cor):
        self.x = cor

    def mostra_cor(self):
        print(self.x)

class Retangulo:

    def __init__(self,base,altura):
        self.x = base 
        self.y = altura
    
    def mudar_lados(self,base,altura):
        self.x = base
        self.y = altura
    
    def retornar_valor(self):
        return self.x,self.y

    def perimetro(self):
        perimetro = self.x * 2 + self.y * 2
        return perimetro

    def area(self):
        area = self.x * self.y
        return area

class Ponto:

    def __init__(self,ponto_x=0,ponto_y=0):
        self.x = ponto_x
        self.y = ponto_y
    def pontos(self):
        print(f'{self.x}\n{self.y}')
    

class Ret:

    def __init__(self):
        self.ponto_1 = None
        self.ponto_2 = None
    
    def ponto_centro(self):
        ponto_central = Ponto()
        ponto_central.x = (self.ponto_1.x + self.ponto_2.x) / 2
        ponto_central.y = (self.ponto_1.y + self.ponto_2.y) / 2
        return ponto_central    
        
    
