lista1 = [1,2,'perro','gato']
print (lista1)
print (lista1[3])

print(lista1[2:])

lista1.append('nuevo')

print(lista1[2:])

lista1.insert(1,1.5)
print (lista1)

lista1.extend(['pajaro','conejo'])

print(lista1)

print(lista1.index('pajaro'))

print('perro' in lista1)
lista1.remove(1)
print(lista1)

lista1.pop()
print(lista1)

lista2 = ['holis','hoooolis']

lista3 = lista1 + lista2
print(lista3)