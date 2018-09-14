#-*- coding:utf-8 -*-

#https://www.uv.es/~diaz/mn/node21.html

#importamos math para el coseno
from math import cos

#definimos las funciones

#f1(x) ---> x^3 - 5
def f1(x):
	return x**3 - 5

#f2(x) --->  x^(3/5) - 16
def f2(x):
	return x**(3./5.) - 16

#f3(x) ---> cos(x) - 6x
def f3(x):
	return cos(x) - 6*x

#definimos la funcion "secante" para comprimir la cantidad de codigo.
def secante(f,xi,xf):
	"""Funcion que aproxima una raiz mediante el método de la secante. 
	Argumentos:
	f  = funcion a calcular su raiz
	xi = valor inicial del intervalo
	xf = valor final del intervalo
	"""
	#definimos el error tolerado
	error = 0.001
	#respuesta (respt) es el punto medio entre el valor inicial y el final
	respt = (xi + xf)/2. 
	#iteraciones-
	itera = 0
	#generar respuesta cada vez más precisa por el método de la secante
	while (abs(f(respt)))>0.001: 
		respt = xf - (f(xf)*(xf -xi))/(f(xf)-f(xi))
		itera += 1
	#se cambian los papeles para poder continuar con el método.
	#lo vi aquí: https://www.youtube.com/watch?v=YOHtIzPmfzE
		xi = xf
		xf = respt  
	print '*** Han ocurrido',itera,'iteraciones'
	print '*** La aproximacion final de la raiz es',respt


print '-------- Metodo de la secante --------\n'
#funcion f1(x)
print 'Función => f1(x) = x^3 - 5'
secante(f1,-10,10)

#funcion f2(x)
print '\nFunción => f2(x) = x^(3/5) - 16'
secante(f2,50.0,200.0)

#funcion f3(x)
print '\nFunción => f3(x) = cos(x) - 6x'
secante(f3,-10.0,10.0)




