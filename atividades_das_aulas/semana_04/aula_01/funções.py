def imposto(salario):
    if salario<3000:
        imp=0.1
    elif salario>=3000 and salario<5500:
        imp=0.13
    elif salario>=5500 and salario<8000:
        imp=0.16
    elif salario>=8000:
        imp=0.2
    return imp

    