#NUMEROS DE MENOR A MAYOR

print('------ NUMEROS DE MENOR A MAYOR (DISTINTOS)------')
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

b=input('Ingresa otro numero = ')
		#SI EL VALOR DE b YA FUE INGRESADO
if b==a:
		#INSISTIR PARA QUE SEA DISTINTO
	while b==a:
		b=None
		b=input('Ya ingresaste ese valor anteriormente, prueba otro = ') 
if type(b)!=int:
	print('El numero debe ser entero!')
	b=None
	while type(b)!=int:
		b=input('Intentalo nuevamente :) , ingresa el numero = ')

c=input('Ingresa el ultimo numero = ')
if c==a or c==b:
	while c==a or c==b:
		c=None
		c=input('Ya ingresaste ese valor anteriormente, prueba otro = ')
if type(c)!=int:
	print('El numero debe ser entero!')
	c=None
	while type(c)!=int:
		c=input('Intentalo nuevamente :) , ingresa el numero = ')
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
	if b==c or c==b:
		print(x + str(a) +','+str(b)+','+str(c))
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
