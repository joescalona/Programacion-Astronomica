#-*-coding:utf-8-*-
from time import time

from iteracion import factorial_iterativo
from recursion import factorial_recursivo

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

n = abs(int(input('Número (se considerará parte entera y el valor absoluto) = ')))

print('***Para factorial iterativo') 
print 'Se demoró',tiempo(factorial_iterativo,n),'segundos'

print('***Para factorial recursivo')
print 'Se demoró',tiempo(factorial_recursivo,n),'segundos'

