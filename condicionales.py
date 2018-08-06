print("Programa de becas")
distancia = int(input("introduce distancia en km: "))
print(distancia)

hermanos = int(input("introduce numero de hermanos: "))
print(hermanos)

salario = int(input("introduce salario anual bruto: "))
print(salario)

if distancia > 40 and hermanos > 2 and salario <= 20000:
	print("tiene derecho a becas")
else:
	print("no tiene derecho a beca")