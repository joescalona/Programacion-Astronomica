# -*-coding:utf-8-*-

#Fibonacci Recursivo 

#Esta serie comienza con el numero 1.
def Fib_Recursivo(n):
	#para n = 0 y n = 1 (serie comienza con estos valores)
	if n < 2:
		return 1
	#recursividad de fibonacci (nuevo termino = suma de los dos anteriores)
	else: 
		return (Fib_Recursivo(n-1) + Fib_Recursivo(n-2))

print '****** FIBONACCI (COMIENZA CON EL 1) ******'
N  = abs(int(raw_input('Ingresa la posición N que quieres saber: ')))
N2 = N
print 'La posición',N,'de Fibonacci es',Fib_Recursivo(N2)	                                          