def fat(n,res):
    if n==0:
        return res 
    res=res*n
    return fat(n-1,res)
x=fat(5,1)
print(x)
#duvidas para aula N se torando dois depois de virar 0 e passar pelo if...