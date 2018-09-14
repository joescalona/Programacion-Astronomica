#-*-coding:utf-8-*-
import time
import matplotlib.pyplot as plt 
import numpy as np 
def Fib_for(n):
	t = time.clock() #comienza el tiempo a correr
	a = 1
	b = 1
	r = []
	cont = 0 #se inicializa el contador
	y = [] #se inicializa eje y
	x = [] #eje x
	if n <= 1:
		t = time.clock() #marcar el tiempo * cada iteración
		cont = cont + 1 #contabilizar 
		#cabe notar que la cantidad de iteraciones en este método
		#es la misma que la posición deseada de fibonacci
		y.append(cont) #agregamos "valor" al eje y
		x.append(t) #y su correspondiente tiempo 
	else:
		for i in range(1,n):
			t = time.clock() 
			cont = cont + 1 
			y.append(cont) #agregamos "valor" al eje y
			x.append(t) #y su correspondiente tiempo 
			c = a + b
			r.append(c) 
			a = b 
			b = c 
	ejex = np.array(x) #crear matriz con datos de eje x
	ejey = np.array(y) #datos de eje y
	return (ejex,ejey) #devolver arreglo con datos almacenados

datos = Fib_for(90000) #almacenar datos de los 100 primeros números de fibonacci
#que es equivalente en este caso a 100 iteraciones
D = np.matrix(datos) #transformar estos datos en una matriz
with plt.xkcd():
	fig = plt.figure(figsize=(8,5),dpi=100)
	plt.plot (datos[0],datos[1],color='olive')
	plt.xlabel('tiempo')
	plt.ylabel('Posicion')
	plt.title('Fibonacci mediante ciclo For')
plt.savefig('for.png')