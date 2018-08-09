print("Asignaturas optativas 2018")
print("Asignaturas optativas: Informatica - Mercadeo - UI/UX")
opcion = input("escribe la asignatura escogida: ")
asignatura = opcion.lower()
if asignatura in ("informatica","mercadeo","ui/ux"):
	print("asignatura elegida es: " + asignatura)
else:
	print("no existe la asignatura: " + asignatura)