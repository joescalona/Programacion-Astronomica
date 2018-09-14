#-*-coding:utf-8 

from math import sqrt 

#funcion Fibonacci
def Fib(n):
	'''Función que entrega la posición enésima de la serie de fibonacci
	Argumentos: 
	n = posición deseada
	'''
	h = (((1+sqrt(5))/2.)**n-((1 - sqrt(5))/(2))**n)/sqrt(5)
	return int(h) 

print '********** Fibonacci (comienza con 1) **********'
num = (abs(int(input('Ingresa la posición que quieres saber = '))))

print Fib(num)