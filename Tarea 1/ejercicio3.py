																		#NUMEROS DE MENOR A MAYOR
print('------ NUMEROS DE MENOR A MAYOR ------')
																		#SOLICITAR NUMERO Y VERIFICAR QUE SEA ENTERO, SI NO ES ASI, IMPRIMIR MENSAJE
a=input('Ingresa un numero = ')
if type(a)!=int:
	print('El numero debe ser entero!')
																		#COMO a YA TIENE UN TIPO, QUE ES DISTINTO AL ENTERO, SE LE ASIGNA EL VALOR NULO A a
																		#VER https://stackoverflow.com/questions/19473185/what-is-a-none-value
	a=None
																		#INSISTIR HASTA QUE SEA ENTERO
	while type(a)!=int:
		a=input('Intentalo nuevamente :) , ingresa el numero = ')
else:																	#SI a ES ENTERO, NO HACER LO ANTERIOR
	a=int(a)
b=input('Ingresa otro numero = ')
if type(b)!=int:
	print('El numero debe ser entero!')
	b=None
	while type(b)!=int:
		b=input('Intentalo nuevamente :) , ingresa el numero = ')
c=input('Ingresa el ultimo numero = ')
if type(c)!=int:
	print('El numero debe ser entero!')
	c=None
	while type(c)!=int:
		c=input('Intentalo nuevamente :) , ingresa el numero = ')
else:
	c=int(c)

																		#POSIBLES COMBINACIONES DE LOS NUMEROS INGRESADOS (DISTINTOS) (3!)
x='Los numeros en orden ascendiente son = '
if a<b<c:
	print(x + str(a) +','+str(b)+','+str(c))
if a<c<b:
	print(x + str(a) +','+str(c)+','+str(b))
if b<a<c:
	print(x + str(b) +','+str(a)+','+str(c))
if b<c<a:
	print(x + str(b) +','+str(c)+','+str(a))
if c<a<b:
	print(x + str(c) +','+str(a)+','+str(b))
if c<b<a:
	print(x + str(c) +','+str(b)+','+str(a))
																		




























																		
											
