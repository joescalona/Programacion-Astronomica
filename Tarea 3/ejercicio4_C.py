#NEWTON
#DESCARADAMENTE COPIADO DEL MATERIAL ENVIADO POR PROFESORA
#PUEDES ENCONTRAR EL ORIGINAL EN LECTURE3-4, PAG 89
#SE DEFINE FUNCION RAIZ CUBICA
def raiz_cubica(x):
#PRECISION
	epsilon = 0.01
#RESPUEST
	guess = x/2.0
#CONTADORA DE ITERACIONES
	count=0
	while abs(guess**3 - x) >= epsilon:
		count+= 1
#METODO DE NEWTON 
		guess = guess - (((guess**3) - x) / (3*(guess**2)))
	#print('* Ocurrieron '+str(count)+ ' iteraciones \n')
	print '* La raiz de', x, 'es aproximadamente', guess
	print '* Ocurrieron',count,'iteraciones \n'
raiz_cubica(25)
raiz_cubica(500)
raiz_cubica(10000)