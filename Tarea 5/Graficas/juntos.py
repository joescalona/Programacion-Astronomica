# -*-coding:utf-8-*-
import time 
import matplotlib.pyplot as plt 
import numpy as np
#Fibonacci while loops 
def Fib_while(n):
	time.clock() #comienza el tiempo a correr
	cont = 0 #se inicializa el contador
	x1 = [] ##se inicializa eje x
	y1 = [] #eje y
	r = [1,1]
	while len(r) <= n: #la cantidad de elementos en la lista debe ser <= n 
		t=time.clock() #marcar el tiempo * cada iteración
		cont += 1 #contabilizar 
		#cabe notar que la cantidad de iteraciones en este método
		#es la misma que la posición deseada de fibonacci
		y1.append(cont) #agregamos "valor" al eje y
		x1.append(t) #y su correspondiente tiempo 
		r.append(r[-1]+r[-2]) #agregar la suma del ultimo elemento con el penultimo
	ejex1 = np.array(x1) #matriz con datos de eje x
	ejey1 = np.array(y1) #matriz con datos de eje y
	return (ejex1,ejey1)

datos1 = Fib_while(34)#almacenar datos de los 100 primeros números de fibonacci
#que es equivalente en este caso a 100 iteraciones
D1 = np.matrix(datos1) #transformar estos datos en una matriz


###################################################################
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

datos = Fib_for(34) #almacenar datos de los 100 primeros números de fibonacci
#que es equivalente en este caso a 100 iteraciones
D = np.matrix(datos) #transformar estos datos en una matriz

###################################################################
#Fibonacci Recursivo 
#Esta serie comienza con el numero 1.
def Fib_Recursivo(n):
	if n < 2:
		return 1
	else: 
		return (Fib_Recursivo(n-1) + Fib_Recursivo(n-2))

def tiempo_fib(n):
	ini = time.clock()
	Fib_Recursivo(n)
	fin = time.clock()
	tot = fin - ini 
	return tot   	

x = np.arange(0,34)

###################################################################

with plt.xkcd():
	fig = plt.figure(figsize=(8,5),dpi=100)
	plt.plot (datos[0],datos[1],color='olive')
	plt.plot(datos1[0],datos1[1],color='hotpink')
	plt.plot([tiempo_fib(i) for i in x],x,'b.-')
	plt.title('Graficas juntas')
	plt.xlabel('Tiempo')
	plt.ylabel('Posicion')
plt.savefig('todos.png')