tupla1 = ('juan',12,5,1988)
print(tupla1)

lista1=list(tupla1)
print(lista1)

tupla2 = tuple(lista1)
print(tupla2)

print(tupla2.index(12))

print(tupla2.count('pedro'))

print(len(tupla2))

#tupla unitaria
tupla3 = ("carlos",)
print(len(tupla3))

nombre, mes, dia, year = tupla1

print(nombre,mes,dia,year)
