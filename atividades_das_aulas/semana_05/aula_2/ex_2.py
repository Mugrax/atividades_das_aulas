from classes import Retangulo as rt

base = int(input('Informe o valor da base: '))
altura = int(input('Informe o valor da altura: '))

ret = rt(base, altura)

pisos = ret.area()

rodapes = ret.perimetro()

print(f'\nPisos (1 x 1 m²): {pisos}\nRodapes (1 m): {rodapes}\n')
