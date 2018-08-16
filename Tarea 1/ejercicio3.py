#NUMEROS DE MENOR A MAYOR
#PROGRAMA MAS LARGO YA QUE CONSIDERE DIVERSAS OPCIONES INGRESADAS POR EL USUARIO
#DISCULPAR POR LA ABUNDANCIA DE CODIGO

print('------ NUMEROS DE MENOR A MAYOR (DISTINTOS) ------'+'\n')
		#SOLICITAR NUMERO Y VERIFICAR QUE SEA ENTERO
a=input('Ingresa un numero = ')

		#SI UN FLOTANTE, TAL COMO 2.0 ES INGRESADO, CONSIDERARLO COMO ENTERO
if float(a)==int(a):
	a=int(a) 

elif type(a)!=int:
	print('\n'+'El numero debe ser entero!')
		#COMO a YA TIENE UN TIPO, QUE ES DISTINTO AL ENTERO, SE LE ASIGNA EL VALOR NULO A a
		#LO APRENDI AQUI https://stackoverflow.com/questions/19473185/what-is-a-none-value
	a=None
		#INSISTIR HASTA QUE SEA ENTERO
	while type(a)!=int:
		a=input('Intentalo nuevamente :) , ingresa el numero = ')
		if float(a)==int(a):
			a=int(a) 

b=input('Ingresa otro numero = ')
		#SI EL VALOR DE b YA FUE INGRESADO
if b==a:
		#INSISTIR PARA QUE SEA DISTINTO
	while b==a:
		b=None
		b=input('Ya ingresaste ese valor anteriormente, prueba otro = ') 

if float(b)==int(b):
	b=int(b) 

elif type(b)!=int:
	print('El numero debe ser entero!')
	b=None
	while type(b)!=int:
		b=input('Intentalo nuevamente :) , ingresa el numero = ')
		if float(b)==int(b):
			b=int(b) 

c=input('Ingresa el ultimo numero = ')
if c==a or c==b:
	while c==a or c==b:
		c=None
		c=input('Ya ingresaste ese valor anteriormente, prueba otro = ')

if float(c)==int(c):
	c=int(c) 

elif type(c)!=int:
	print('El numero debe ser entero!')
	c=None
	while type(c)!=int:
		c=input('Intentalo nuevamente :) , ingresa el numero = ')
		if float(c)==int(c):
			c=int(c) 
else:
	c=int(c)

		#POSIBLES COMBINACIONES DE LOS NUMEROS INGRESADOS (DISTINTOS) (3!)
x='Los numeros en orden ascendiente son = '
while a<b and a<c:
	if b<c:
		print(x + str(a) +','+str(b)+','+str(c))
		break
	if c<b:
		print(x + str(a) +','+str(c)+','+str(b))
		break
		
while b<a and b<c:
	if a<c:
		print(x + str(b) +','+str(a)+','+str(c))
		break
	if c<a:
		print(x + str(b) +','+str(c)+','+str(a))
		break
while c<a and c<b:
	if a<b:
		print(x + str(c) +','+str(a)+','+str(b))
		break
	if b<a:
		print(x + str(c) +','+str(b)+','+str(a))
		break
