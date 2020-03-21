#X = (a+ 2) / 3 + b
#x = 3 +b / (a +2)
#caso 3 que puede ser caso 3 y 4


def caso3(valor):
	pila      = []
	resultado = []
	contador  = -1
	if valor != " ":
		for i in valor:
			if i != " ":
				pila.append(i)

	for i in pila: 
		contador +=1
		
		if i == "(":
		
			resultado.append([pila[contador+1],pila[contador+2],pila[contador+3]])
			pila.pop(contador)
			pila.remove(pila[contador])
			pila.remove(pila[contador+1])
			pila.remove(pila[contador+1])
			pila.pop(contador)

	contador = -1
	for i in pila:
		contador+=1
		if i == "*" or i == "/":
			#si antes hay =
			#ejemplo x =  * o / 2 + 4
			if pila[contador-1] == "=":
				resultado.append([i,pila[contador+1]])
				pila.pop(contador)
				pila.pop(contador)
			else:
				#ejemplo x = 2 + 4 * 
				resultado.append([i,pila[contador-1]])
				pila.pop(contador)
				pila.pop(contador-1)
	contador = -1
	for i in pila:
		contador+=1
		if  i == "+" or i == "-":
			if pila[contador-1] == "=":
				resultado.append([pila[contador], pila[contador+1]])
				pila.remove(pila[contador])
				pila.remove(pila[contador])
			else:
				resultado.append([pila[contador], pila[contador-1]])
				pila.remove(pila[contador])
				pila.remove(pila[contador-1])
	print valor
	
	

	var_t0 = "T0 = "+" " .join(resultado[0])
	var_t1="T1 = T0 " +" " .join(resultado[1])
	var_2="T2 =  T1 " + " " .join(resultado[2])

	print(var_t0)
	print(var_t1)
	print(var_2)
	



#Dos casos de prueba
caso3("X = (a + 5) / 3 + b")

print("--------------------------")
caso3("x = 3 + b / (a + 2 )")