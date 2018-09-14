#-*-coding:utf-8-*-
from time import time

#se definen las funciones necesarias

def Fib_for(n):
	a = 1
	b = 1
	r = []
	if n <= 1:
		return 1 
	else:
		for i in range(1,n):
			c = a + b
			r.append(c) 
			a = b
			b = c
	return r[-1] 

def Fib_while(n):
	r = [1,1] 
	while len(r) <= n: 
		r.append(r[-1]+r[-2])
	return r[-1]

def Fib_Recursivo(n):
	if n < 2:
		return 1
	else: 
		return (Fib_Recursivo(n-1) + Fib_Recursivo(n-2))


def tiempo(f,num):
	''' Funcion que calcula el tiempo de ejecución de otra función
	Argumentos:
	f   = función
	num = argumento de f
	'''
	ini = time()#iniciar cronómetro
	f(num) #aquí la función ingresada tomará como argumento num
	fin = time() #fin cronómetro 
	return (fin - ini) 

print '--------- Calculador de tiempo ---------'

n = abs(int(input('Posición de fibonacci = ')))
print('***Para Fibonacci (FOR)') 
print 'Se demoró',tiempo(Fib_for,n),'segundos'

print('***Para Fibonacci (WHILE)') 
print 'Se demoró',tiempo(Fib_while,n),'segundos'

print('***Para Fibonacci (RECURSION)') 
print 'Se demoró',tiempo(Fib_Recursivo,n),'segundos'e