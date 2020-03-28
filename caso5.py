#caso #5

#X = 2*y - ((4*y) + z)
def caso5(valor):
	pila         = []
	resultado    = []
	resultado_f  = []
	resultado_ff =[]
	contador  = -1
	if valor != " ":
		for i in valor:
			if i != " ":
				pila.append(i)


	for i in pila: 
		contador +=1
		
		if i == "(":	
			resultado.append(pila[contador])
			resultado.append(pila[contador+1])
			resultado.append(pila[contador+2]) 
			resultado.append(pila[contador+3]) 
			resultado.append(pila[contador+4]) 
			resultado.append(pila[contador+5])
			resultado.append(pila[contador+6])
			resultado.append(pila[contador+7])
			resultado.append(pila[contador+8])
			pila.pop(contador)
			pila.pop(contador)
			pila.pop(contador)
			pila.pop(contador)
			pila.pop(contador)
			pila.pop(contador)
			pila.pop(contador)
			pila.pop(contador)
			pila.pop(contador)
		
	if pila[-1] == "*" or pila[-1] == "/":
		resultado_f.append([pila[-1],pila[-2]])
		pila.pop()
		pila.pop()
	else:
		resultado_f.append([pila[-2],pila[-3],pila[-4]])
		pila.remove(pila[-2])
		pila.remove(pila[-2])
		pila.remove(pila[-2])
	

	resultado.remove(resultado[0])
	resultado.pop()
	
	contador=-1
	for i in resultado:
		contador+=1
		if i == "(":
			resultado_ff.append([resultado[contador+1],resultado[contador+2],resultado[contador+3]])
			resultado.remove(resultado[contador])
			resultado.remove(resultado[contador])
			resultado.remove(resultado[contador])
			resultado.remove(resultado[contador])
			resultado.remove(resultado[contador])



	valor_t0 = "t0 = " + " " .join(resultado_ff[0])
	valor_t1 = "t1 = t0 "+ " " .join(resultado) 
	valor_t2 = "t2 = "+ " ".join(resultado_f[0])
	valor_t3 = "t3 = t2 "+pila[-1]+ " t1" 
	
	

	print valor_t0
	print valor_t1
	print valor_t2
	print valor_t3
	print valor




