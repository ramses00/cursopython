for i in["pildoras","informaticas",2]:
	print("hola", end="    ")

for i in "juan@lalalalala.com":
	print("letras", end=" ")
print("")

email = False
miEmail = input("Introduce tu email: ")

for i in miEmail:
	if i == '@':
		email = True
if email: #(esto es una forma simplificada de decir si la variable es 
#verdadera, o se  si email == True)
	print("email correcto")
else:
	print("email incorrecto")