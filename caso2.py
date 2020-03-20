#X = a / a + b * b
# 0 1 2 3 4 5 6 7 8
#caso 2


def caso2(valor):
	pila  = []
	resultados = []
	contador = -1


	for i in valor:
		if i != " ":
			pila.append(i)

	for i in pila:
		contador+=1
		if i == "*" or i == "/":
			resultados.append([pila[contador-1], pila[contador], pila[contador+1]])
			pila.remove(pila[contador])
			pila.remove(pila[contador])
			pila.remove(pila[contador-1])

	contador=-1
	for i in pila:
		if pila != "":
			if i == "+" or i == "-":
				resultados.append([i])
				pila.remove(i)
	print(valor)
	print("t0 = " + str(resultados[0]))
	print("t1 = " + str(resultados[1]))
	print("t2 = t0 "+ str(resultados[2]) + " t1")




	


caso2("x = a / a + b / b")