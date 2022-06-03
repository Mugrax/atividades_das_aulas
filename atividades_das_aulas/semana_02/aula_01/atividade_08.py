X=float(input('peso em gramas:'))
if X<=500:
    PR=1.10
elif X>500 and X<=2000:
    PR=2.20
elif X>2000 and X<=10000:
    PR=3.70
elif X>10000:
    X-=10000
    I=X/1000
    PR=5+(int(I))*3.80
print(f'o preço da remessa é: R${round(PR,2)}')