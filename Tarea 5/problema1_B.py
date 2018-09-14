#-*- coding:utf-8 -*-

#importamos math para el coseno y el seno
from math import cos,sin 
#definimos funciones

# f1(x)---> x^3 - 5
# f1'(x)---> 3x^2 
def f1(x):
    return x**3 - 5

def df1(x):
    return 3*x**2

# f2(x) --->  x^(3/5) - 16
# f2'(x) ---> 3 / (5x^(2/5))
def f2(x):
	return x**(3./5.) - 16
def df2(x):
	return 3/(5*x**(2./5.))

#f3(x) ---> cos(x) - 6x
#f3'(x) ---> -sin(x) - 6
def f3(x):
	return cos(x) - 6*x

def df3(x):
	return -sin(x) - 6

#definimos una funcion que tenga el m‚todo de newton
def newton(f,df,xi):
	"""Funcion que aproxima una ra¡z mediante el m‚todo de Newton-Raphson
	Argumentos:
	f  = funcion a calcular su raiz
	df = derivada de f
	xi = supuesto inicial
	"""
	xnew = [xi,]
	erro = 0.001
	resp = xnew[-1]
	coun = 0

	while True:
		resp = resp - (f(resp)/df(resp))
		xnew.append(resp)
		coun += 1 
		if abs(xnew[-2]-xnew[-1]) <= erro:
			break
	print '***Han ocurrido',coun,'iteraciones'
	print '***La aproximacion final es',resp

print '-------- Metodo de Newton --------'
#funcion f1(x)
print 'Función => f1(x) = x^3 - 5'
newton(f1,df1,-10.0)

#funcion f2(x)
print '\nFunción => f2(x) = x^(3/5) - 16'
newton(f2,df2,50.0)

#funcion f3(x)
print '\nFunción => f3(x) = cos(x) - 6x'
newton(f3,df3,-10.0)



