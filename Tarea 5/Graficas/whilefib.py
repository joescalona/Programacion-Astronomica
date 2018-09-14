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

datos1 = Fib_while(90000)#almacenar datos de los 100 primeros números de fibonacci
#que es equivalente en este caso a 100 iteraciones
D1 = np.matrix(datos1) #transformar estos datos en una matriz

with plt.xkcd():
	fig = plt.figure(figsize=(8,5),dpi=100)
	plt.plot(datos1[0],datos1[1],color='hotpink')
	plt.xlabel('tiempo')
	plt.ylabel('Posicion')
	plt.title('Fibonacci mediante ciclo While')
plt.savefig('while.png')