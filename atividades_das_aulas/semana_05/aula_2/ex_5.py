from classes import Ponto
from classes import Ret

retangulo = Ret()

retangulo.ponto_1 = Ponto(4,3) 
retangulo.ponto_2 = Ponto(10,6)

ponto_central = retangulo.ponto_centro()

ponto_central.pontos()