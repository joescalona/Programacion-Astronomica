#-*-coding: utf-8

#se define raíz cubica
def raiz_cubica(x,e):
	"""Funcion que calcula la raíz cúbica de un numero float usando el método de Newton-Raphson.
	Argumentos:
	x = valor al cual se le aplicará la raiz cúbica
	e = error (epsilon)
	"""
#respuesta 
	respt = x/2.0
	while abs(respt**3 - x) >= e:
#metodo de newton
		respt = respt - (((respt**3) - x) / (3*(respt**2)))
	print '*** La raiz de', x, 'es aproximadamente', respt

print '-------- Raíz cúbica --------\n'
numero  = float(raw_input('Ingresa un número = '))
epsilon = float(raw_input('Ingresa el error tolerado (positivo) = '))
while not (epsilon)>=0:
	epsilon = float(raw_input('el error debe ser positivo! = '))

raiz_cubica(numero,epsilon) 
