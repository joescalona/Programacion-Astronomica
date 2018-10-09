#-*-coding:utf-8 

import numpy as np 
import matplotlib.pyplot as plt 

#Creacion de ejes
plt.axis([-10,10,-10,10,])	


#n bolas (10 bolas en este caso)
n     = 10
pos   = (20 * np.random.sample(n*2)-10).reshape(n,2)
#La velocidad cambiará cada vez que se ejecuta el programa
vel   = ((np.random.sample())* np.random.normal(size=n*2)).reshape(n,2)
#tamaño del radio de las bolas 
sizes = 100 * np.random.sample(n)+100


#crea 10 bloques de datos de 1 fila y 4 columnas cada uno
colors = np.random.sample([n,3])
circles = plt.scatter(pos[:,0],pos[:,1],marker = 'o',s = sizes,c=colors)

#se realizarán 100 iteraciones
for i in range(100):
	pos = pos + vel  
	bounce = abs(pos) > 10   
	vel[bounce] = -vel[bounce] 
	circles.set_offsets(pos)    
	plt.pause(0.05)

