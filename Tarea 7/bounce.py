#-*-coding:utf-8 

import numpy as np 
import matplotlib.pyplot as plt 

plt.figure(1)			
plt.clf()
#Creacion de ejes
plt.axis([-10,10,-10,10,])	

#Define properties of the 'bouncing balls'
#n bolas (10 bolas en este caso)
n     = 10
#crear arreglo con n*2 datos entre 0 y 1 aleatorio y 
#reordenar en una matriz de n filas y 2 columnas 
#pos = posicion, varía entre -10 y 10 
pos   = (20 * np.random.sample(n*2)-10).reshape(n,2)
#crear arreglo con n*2 datos aleatorios distribución gaussiana
#y reordenar en matriz de n filas y 2 columnas
#además vel = velocidad varía entre -1 y 1
vel   = (0.3 * np.random.normal(size=n*2)).reshape(n,2)
#arreglo de n datos 
#varia entre 100 y 200 
#tamaño del radio de las bolas 
sizes = 100 * np.random.sample(n)+100

#Colors where each row is (Red,Green,Blue,Alpha), Each can go
#from 0 to 1. Alpha is transparency,
#crea 10 bloques de datos de 1 fila y 4 columnas cada uno
colors = np.random.sample([n,3])

#Draw all the circles and return an object 'circles' that allows 
#manipulation of the plotted circles. 

circles = plt.scatter(pos[:,0],pos[:,1],marker = 'o',s = sizes,c=colors)

#se realizarán 100 iteraciones
for i in range(1000):
	pos = pos + vel  
	bounce = abs(pos) > 10   #Find balls that are outside walls
	vel[bounce] = -vel[bounce] #Bounce if outside the walls
	circles.set_offsets(pos)    #Change the positions
	#plt.draw()
	#plt.show()
#tiempo de duración
	plt.pause(0.05)

