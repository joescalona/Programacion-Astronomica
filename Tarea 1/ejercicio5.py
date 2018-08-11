	#PROGRAMA INTERES COMPUESTO

	#ASIGNACION DE VARIABLES

P = 10000 
n = 12
r = 0.08 

	#INGRESAR UN TIEMPO Y REGRESAR EL MONTO ACUMULADO

t=int(input('Ingresa el numero de ano para el cual sera calculada la cantidad de dinero = '))

	#CALCULAR EL VALOR ACUMULADO (A)
A= P * (1 + (r/n))**(n * t)
	
	#IMRPIMIR A 
print('El valor acumulado en '+str(t)+' anos es = '+str(A))
