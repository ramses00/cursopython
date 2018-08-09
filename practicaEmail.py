email = input("Introduce tu email: ")

puntos = 0

for i in email:
	if i == '.':
		puntos+=1
	elif i == '@':
		puntos = 0

print(puntos)
if puntos == 1:
	print("email valido: " + email)
else:
	print("email no valido: " + email)
