# -*-coding:utf-8-*-

#Fibonacci for loops
def Fib_for(n):
	# a y b son los 2 primeros numeros de la serie
	a = 1
	b = 1
	r = [] #de aqui se extraerá siempre el último elemento
	if n <= 1:
		#r.append(a)
		#r.append(b)
		return 1 #para los 2 primeros terminos 
	else:
		for i in range(1,n):
			c = a + b # nuevo elemento
			r.append(c) 
			a = b #se desplazan los numeros
			b = c #se desplazan los numeros
	return r[-1] 

print '****** FIBONACCI (COMIENZA CON EL 1) ******'
N = abs(int(raw_input('Ingresa la posición N que quieres saber: ')))
N2 = N-1
print 'La posición',N,'de Fibonacci es',Fib_for(N2)


