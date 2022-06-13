from math import pi

def raio_esfera_volume(r):
    v=(4/3)*pi*r**3
    return round(v,2)
r=float(input())
v=raio_esfera_volume(r)
print(v)