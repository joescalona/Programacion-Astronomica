#CALCULAR FACTORIAL

		#IMPRIMIR EN PANTALLA LO QUE HACE EL PROGRAMA
print('------ FACTORIAL DE UN NUMERO ------')
		#MULT ES 1, PARA QUE COMIENCE EL CICLO 
mult=1
		#SOLICITAR UN NUMERO (ENTERO)
n=input('Ingresa un numero = ')
		#MIENTRAS QUE EL NUMERO INGRESADO NO SEA ENTERO, IMPRIMIR EN PANTALLA UN MENSAJE
while type(n)!= int:
	print('La funcion factorial solo admite numeros enteros')
	n=input('Ingresa un numero :) = ')
		#PERO SI EL NUMERO ES ENTERO
if type(n)==int:
		#HACER UN CICLO DONDE SE MULTIPLICAN TODOS LOS NUMEROS ENTEROS ANTERIORES A EL (CONTANDOLO)
	for i in range(1,n+1):
		mult=mult*i
print ('El factorial de '+str(n)+' es '+str(mult))
