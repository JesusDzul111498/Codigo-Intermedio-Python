#caso 4
#ejemplo
# X = (a+ 2) / (3 - b)

def caso4(valor):
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
	

		
	
	resultado.append([pila.pop()])

	var_t0 = "T0 = "+" " .join(resultado[0])
	var_t1="T1 =  " +" " .join(resultado[1])
	var_2="T2 =  T0 " + " " .join(resultado[2]) + " T1"
	print valor
	print(var_t0)
	print(var_t1)
	print(var_2)
