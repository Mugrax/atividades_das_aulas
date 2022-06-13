def conversor_horas(segundos):
    minutos=round(segundos/60)
    horas=round(minutos/60)
    minutos=minutos-horas*60
    segundos=segundos-(horas*3600+minutos*60)
    return horas,minutos,segundos
segundos=int(input('digite os segundos'))
h,m,s=conversor_horas(segundos)
print(h,m,s)