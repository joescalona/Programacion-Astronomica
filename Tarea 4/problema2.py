#-*- coding: utf-8 -*-

def des_encriptacion(desp):
	#imprime el valor de desp para saber cuanto es el desplazamiento
	print desp
	abc = 'abcdefghijklmnopqrstuvwxyz'
	#cadena a descifrar
	cad = "gwc uivioml bw nqvl bpm zqopb apqnb"
	res = ""
	for letra in cad:
		pos = abc.find(letra)
		if pos == -1:
			res = res + letra
			continue
		des = pos + desp
		if des >=26:
			des = des - 26
		res = res + abc[des]
	return res

#probar en un rango de 1 hasta 26, que es la cantidad de letras del alfabeto
#luego buscar hasta encontrar una frase con sentido (desp = 18)
for i in range(1,27):
	print des_encriptacion(i)