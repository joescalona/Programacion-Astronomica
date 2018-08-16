#PROGRAMA RAIZ

	#COMENZAR CON g = 1 

g = 1

x = float(input('Ingresa un valor = '))

# IDEA DE FRANCO SEPULVEDA (PARA X<0 y X=0)
# EL SE DIO CUENTA QUE EL PROGRAMA NO ES FUNCIONAL PARA X=0
if x<0.0:
	print('El numero debe ser positivo')

elif x==0.0:
	print('La raiz de 0 es 0')

	#MIENTRAS LA EXPRESION SEA MAYOR A 0.01
	#(SI EL MIEMBRO DERECHO ES MAS PEQUENO, MAS PRECISO ES EL RESULTADO)
	#SIN EMBARGO NO SE LA EXPLICACION MATEMATICA DE ESTO
	
else:
	while abs((g*g)/x-1.)>0.01:
	#g IRA ADQUIRIENDO NUEVOS VALORES
		g=(g+x/g)/2

	#SI LA EXPRESION ANTERIOR ES MENOR AL VALOR ESTABLECIDO ANTES
	#IMPRIMIR g
	if abs((g*g)/x-1.)<0.01:
		print ('La raiz de '+str(x)+' es '+str(g))

	#PARA X=5489, el programa arroja 74.2356079049








