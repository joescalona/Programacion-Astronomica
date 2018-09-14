#-*-coding:utf-8-*-
from time import time

#Se definen las funciones necesarias para el ejercicio 
def factorial_iterativo(n):
    '''Función que recibe un número n y retorna n!
    '''
    mul = 1 #primera multiplicación de la iteración
    for i in range(1,n+1): #itera hasta n
        mul = mul * i #1*2*3*4*..*n
    return mul

def factorial_recursivo(n):
	'''Función que recibe un número n y retorna n!
	''' 
	# 0! = 1

	if n == 0:
		return 1
	
	elif n == 1: #caso base de función recursiva
		return n
	else:
		return n*factorial_recursivo(n-1)
	# si n != a 1, siempre multiplicará n * (n-1) hasta que n == 1. 


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

