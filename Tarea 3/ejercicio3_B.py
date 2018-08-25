from math import sqrt 
#APARTADO A)
#-------------------------
#DEFINIMOS FUNCION QUE ARROJA SI UN VALOR ES PRIMO O NO 
#INPUT = X
#SI X ES PRIMO, RETORNA 1
#SI NO, RETORNA 0

def es_primo(x):
#INICIO LOOP DESDE 2 HASTA X-1 
    for i in range(2,x):

#LA FUNCION -IF ANY(LISTA)- LA APRENDI EN SOLOLEARN (SECCION "MAS TIPOS >> FUNCIONES 
#UTILES")
#PARA QUE UN NUMERO SEA PRIMO, ESTE DEBE SER DIVISIBLE SOLO POR 1 Y EL MISMO
#POR LO TANTO SI EXISTIERA ALGUN i (IF ANY) QUE EL CUOCIENTE ENTRE EL NUMERO E i 
#SEA IGUAL A 0
#EL NUMERO NO ES PRIMO (Y LA FUNCION RETORNARA 0)
        if any([x%i==0]):
            return 0 
    return 1
#-------------------------
#APARTADO B)
x = int(input('Ingresa un numero y dire si es primo o no = '))
if x==1:
	print('No es primo :( ')

elif x>0:
	if es_primo(x) == 1:
		print('Es primo!')
	else:
		print('No es primo :( ')
else: 
	print('Debe ser un numero entero y positivo!')


