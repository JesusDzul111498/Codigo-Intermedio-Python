#Menu de casos a esperar
import caso1
import caso2
import caso3
import caso4
import caso5


print ("\t\tGeneracion de codigo intermedio")
print("*--Caso 1 : Simbolos aritmeticos con diferente prioridad")
print("*--Caso 2 : Simbolos aritmeticos con diferente prioridad")
print("*--Caso 3 : Simbolos aritmeticos con parentesis ")
print("*--Caso 4 : Simbolos aritmeticos con parentesis ")
print("*--Caso 5 : Almenos dos simbolos aritmeticos con  anidamiento de parentesis ")
int_n = input("Ingrese el numero de caso: ")

while int_n != 0:
	if int_n == 1:
		print("\n#__Caso 1 : Simbolos aritmeticos con diferente prioridad\n")
		print("Usted puede ver un ejemplo del caso o ingresar un caso")
		print("1 == ver caso de ejemplo")
		print("2 == ingresar ejemplo")
		ingresar = input()
		while ingresar != 0:
			if ingresar == 1:
				print("Ejemplo :")
				caso1.caso1("X = 2 + 5 * Y")
			if ingresar == 2:
				print("Ejemplo X = 2 + 5 * Y sintaxis")
				ejemplo = raw_input("Ingresa la expresion :\n")
				str(ejemplo)
				caso1.caso1(ejemplo)
			print("\n1 == ver caso de ejemplo")
			print("2 == ingresar ejemplo")
			print("0 == salir")
			ingresar = input()
	if int_n == 2:
		print("#__Caso 2 : Simbolos aritmeticos con diferente prioridad")
		print("Usted puede ver un ejemplo del caso o ingresar un caso")
		print("1 == ver caso de ejemplo")
		print("2 == ingresar ejemplo")
		ingresar = input()
		while ingresar != 0:
			if ingresar == 1:
				print("Ejemplo :")
				caso2.caso2("X = a / a + b * b")
			if ingresar == 2:
				print("Ejemplo X = a / a + b * b sintaxis")
				ejemplo = raw_input("Ingresa la expresion :\n")
				str(ejemplo)
				caso2.caso2(ejemplo)
			print("\n1 == ver caso de ejemplo")
			print("2 == ingresar ejemplo")
			print("0 == salir")
			ingresar = input()
	if int_n == 3:
		print("#__Caso 3 : Simbolos aritmeticos con parentesis ")
		print("Usted puede ver un ejemplo del caso o ingresar un caso")
		print("1 == ver caso de ejemplo")
		print("2 == ingresar ejemplo")
		ingresar = input()
		while ingresar != 0:
			if ingresar == 1:
				print("Ejemplo :")
				caso3.caso3("X = (a+ 2) / 3 + b")
			if ingresar == 2:
				print("Ejemplo X = (a+ 2) / 3 + b sintaxis")
				ejemplo = raw_input("Ingresa la expresion :\n")
				str(ejemplo)
				caso3.caso3(ejemplo)
			print("\n1 == ver caso de ejemplo")
			print("2 == ingresar ejemplo")
			print("0 == salir")
			ingresar = input()

	if int_n == 4:
		print("#__Caso 4 : Simbolos aritmeticos con parentesis ")
		print("Usted puede ver un ejemplo del caso o ingresar un caso")
		print("1 == ver caso de ejemplo")
		print("2 == ingresar ejemplo")
		ingresar = input()
		while ingresar != 0:
			if ingresar == 1:
				print("Ejemplo :")
				caso4.caso4("X = (a+ 2) / (3 - b)")
			if ingresar == 2:
				print("Ejemplo X = (a+ 2) / (3 - b) sintaxis")
				
				ejemplo= raw_input("Ingresa la expresion :\n")
				str(ejemplo)
				caso3.caso3(ejemplo)
			print("\n1 == ver caso de ejemplo")
			print("2 == ingresar ejemplo")
			print("0 == salir")
			ingresar = input()
	if int_n == 5:
		print("#__Caso 5 : Almenos dos simbolos aritmeticos con  anidamiento de parentesis ")
		print("Usted puede ver un ejemplo del caso o ingresar un caso")
		print("1 == ver caso de ejemplo")
		print("2 == ingresar ejemplo")
		ingresar = input()
		while ingresar != 0:
			if ingresar == 1:
				print("Ejemplo :")
				caso5.caso5("X = 2*y - ((4*y) + z)")
			if ingresar == 2:
				print("Ejemplo X = 2*y - ((4*y) + z) sintaxis")
				
				ejemplo= raw_input("Ingresa la expresion :\n")
				str(ejemplo)
				caso3.caso3(ejemplo)

			print("\n1 == ver caso de ejemplo")
			print("2 == ingresar ejemplo")
			print("0 == salir")
			ingresar = input()
	else:
		print "\n***Ingresa un numero valido***\n"


	print("*--Caso 1 : Simbolos aritmeticos con diferente prioridad")
	print("*--Caso 2 : Simbolos aritmeticos con diferente prioridad")
	print("*--Caso 3 : Simbolos aritmeticos con parentesis ")
	print("*--Caso 4 : Simbolos aritmeticos con parentesis ")
	print("*--Caso 5 : Almenos dos simbolos aritmeticos con  anidamiento de parentesis ")
	int_n = input("\nIngrese el numero de caso o 0 para salir: ")
	if int_n == 0:
		print "Adios++"


