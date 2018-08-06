
dicc1 = {"venezuela":"caracas", "alemania":"berlin", "españa":"madrid"}

dicc1["italia"]="lisboa"
print(dicc1)

dicc1["italia"]="roma"
print(dicc1)

del dicc1["españa"]
print(dicc1)

lista1 = ["juan","pedro","mario"]
dicc2 = {lista1[0]:23,lista1[1]:22,lista1[2]:18}
print(dicc2)

dicc3 = {"nombre":"michael","edad":24,"anillos":{"temporadas":[1991,1992,1993]}}
print(dicc3)
print(dicc3["anillos"])

print(dicc3.keys())
print(dicc3.values())
