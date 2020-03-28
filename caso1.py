

#ejemplo =  "X = 3 + 5 * Y"
#           0 1 2 3 4 5 


def caso1(valor):
	pila = []
	variables = []
	contador = -1
	for i in valor:
		if i != " ":
			pila.append(i)
	var_t0 = ""
	for i in pila:

		contador +=1
		if i =="*" or i=="/":

			
			variables.append([pila[contador-1], pila[contador], pila[contador+1]])
			var_t0 = "t0 = " + pila[contador-1] +  pila[contador]+ pila[contador+1] + " "
			pila.remove(pila[contador])
			pila.remove(pila[contador])
			pila.remove(pila[contador-1])




			
	contador2 = -1
	
	var_t1 = ""
	for i in pila:
		# "X = + Y"
		   #0 1 2 3
		contador2 +=1
		if i == "+" or i == "-":
			
			

			if pila[contador2-1] == "=":
				#agregar numero o literal
				#valor t1 + contador + contador+1
				var_t1 = "t1 = t0" +pila[contador2]+pila[contador2+1]
				variables.append([pila[contador2], pila[contador2+1]])
				
				pila.remove(pila[contador2])
				pila.remove(pila[contador2-1])
			
			
				
				#x = y +
			else:
				#agregar numero o literal
				#contador-1 + contador + valort1
				var_t1 = "t1 ="+pila[contador2-1]+ pila[contador2] +" t0"

				variables.append([pila[contador2-1], pila[contador2]])
				
				pila.remove(pila[contador2])
				pila.remove(pila[contador2-1])
				
			
				
	print valor
	print(var_t0)
	print(var_t1)



