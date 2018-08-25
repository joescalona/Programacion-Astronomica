#BISECCION
#DESCARADAMENTE COPIADO DEL MATERIAL ENVIADO POR PROFESORA
#PUEDES ENCONTRAR EL ORIGINAL EN LECTURE3-4, PAG 81
#SE DEFINE FUNCION RAIZ CUBICA
def raiz_cubica(x):
#PRECISION
	epsilon = 0.01
#MINIMO Y MAXIMO DEL INTERVALO
	low,high = 0.0, max(1.0,x)
#RESPUESTA
	ans = (high + low)/2.0 
#CONTADORA DE ITERACIONES
	count = 0

	while abs(ans**3 - x) >= epsilon:
		#print 'low =',low, 'high =',high, 'ans = ',ans
		count +=1
#SI EL CUADRADO DE LA POSIBLE RESPUESTA ES MENOR QUE X 
#ENTONCES DEBE ESTAR A LA IZQUIERDA
		if ans**3 < x:
			low = ans
#SI ES MAYOR, DEBE ESTAR A LA DERECHA
		else:
			high = ans

		ans = (high + low)/2.0
		
	print '* La raiz de', x, 'es aproximadamente', ans
	print '* Ocurrieron',count,'iteraciones \n'
raiz_cubica(25)
raiz_cubica(500)
raiz_cubica(10000)
