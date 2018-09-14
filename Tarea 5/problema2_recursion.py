# -*-coding:utf-8-*-

#Factorial Recursivo
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

print '****** FACTORIAL DE UN NUMERO ******'
num = abs(int(input('Número (se considerará parte entera y el valor absoluto) = ')))

print 'El factorial de',num,'es',factorial_recursivo(num)
