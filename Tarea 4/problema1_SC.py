#-*- coding: utf-8 -*-

def des_encriptacion(cadena,desp):
	abc = 'abcdefghijklmnopqrstuvwxyz'
	res = ""
	for letra in cadena:
		pos = abc.find(letra)
	#el método .find retorna -1 si no encuentra el caracter en el abc
		if pos == -1:
			res = res + letra
			continue
		des = pos + desp
		if des >=26:
			des = des - 26
		res = res + abc[des]
	return res

print('--------- METODO DE CESAR ---------\n')

ask = raw_input('Quieres encriptar o descrifar un mensaje? (ingresa 1 para encriptar, 2 para descrifrar) = ')

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
