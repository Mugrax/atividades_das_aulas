Segundos=int(input('digite os segundos:\n'))
if Segundos>=60 and Segundos<3600:
    minutos=Segundos/60
    print(f'{round(minutos,2)}minutos')
elif Segundos>=3600 and Segundos<86400:
    horas=Segundos/3600
    print(f'{round(horas,2)}horas')
elif Segundos>=86400:
    dias=Segundos/86400
    print(f'{round(dias,2)}dias')
else:
    print(f'{Segundos}segundos') 