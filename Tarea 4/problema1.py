#-*- coding: utf-8 -*-

def des_encriptacion(cadena,desp):
	abc = 'abcdefghijklmnopqrstuvwxyz'
	#respuesta final 
	res = ""
	for letra in cadena:
	#encontrar la posicion de cada letra 
		pos = abc.find(letra)
	#el método .find retorna -1 si no encuentra el caracter en el abc
	#ejemplo, el espacio(" ").
		if pos == -1:
	#si no encuentra caracter en el abc se debe añadir este caracter a res. (Idea de Diego Salvador)
			res = res + letra
			continue
	#posicion de la letra desplazada desp letras
		des = pos + desp

	#al hacer len(abc) retorna 26, si la variable desplazamiento es mayor a 26
	#no tiene sentido buscar el elemento, por ejemplo 27 en el abc, ya que retornará un "fuera de rango"
	#para solucionarlo: 
		if des >=26:
			des = des - 26
	#ejemplo, si desp = 3, al llegar a una "z" debiera retornar "c", si no estuviera el if, en la linea
	#de abajo saldrá un error ya que abc [25+3] no existe. Sin embargo 28-26 = 2 y abc[2] = 'c'. 
	#Esto sirve para cualquier desplazamiento.
		res = res + abc[des]
	return res

#########################################################################

print('--------- METODO DE CESAR ---------\n')

ask = raw_input('Quieres encriptar o descrifar un mensaje? (ingresa 1 para encriptar, 2 para descrifrar) = ')

#while con múltiples condiciones
#https://stackoverflow.com/questions/2146419/how-to-do-while-loops-with-multiple-conditions
while not ask == "1" and not ask == "2":
	ask = None
	ask = raw_input('Ingresa 1 [encriptar] o 2 [descifrar] (CTRL + C para cerrar) = ')

if ask == '1':
	print '******* ENCRIPTACION *******'
	enp = raw_input('Ingresa un mensaje para ser encriptado \n')
	dsp = int(raw_input('Ingresa el desplazamiento de cifrado (debe ser negativo)\n'))
	while dsp > 0: 
		dsp = None
		dsp = int(raw_input('Debe ser un valor negativo!\n'))
	print "*******************"
	print "El siguiente mensaje está encriptado con un desplazamiento de",abs(dsp),"letras\n"
	print des_encriptacion(cadena=enp,desp=dsp)

elif ask == '2':
	print '******* DESENCRIPTACION *******'
	enp = raw_input('Ingresa un mensaje para ser descifrado \n')
	dsp = int(raw_input('Ingresa el desplazamiento con el cual fue encriptado (debe ser positivo)\n'))
	while dsp < 0: 
		dsp = None
		dsp = int(raw_input('Debe ser un valor positivo!\n'))
	print "*******************"
	print " Mensaje revelado = "
	print des_encriptacion(cadena=enp,desp=dsp)
