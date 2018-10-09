#-*-coding: utf-8 

import numpy as np 
import matplotlib.pyplot as plt 

#Configuración de ejes 

plt.axis([-10,10,-10,10])
#Se añadirá "punto con gravedad"
plt.plot(0,0, marker ='*',c='r')
#Para mayor elegancia (no caos), elegimos 1 bolita
n = 1
pos = (20*np.random.sample(n*2) - 10).reshape(n,2)
vel = (0.1*np.random.normal(size=n*2)).reshape(n,2)
sizes = 100*np.random.sample(n)+100
circles = plt.scatter(pos[:,0],pos[:,1],marker = 'o', s=sizes, c='g')
for i in range(1000):
	#distancia al centro
	dis = np.sqrt(pos[:,0]**2 + pos[:,1]**2) #Distancia al centro
	#aceleracion
	a_x = ((-1/(15. + dis**2))/dis) * pos[:,0]
	a_y = ((-1/(15. + dis**2))/dis) * pos[:,1]
	#velocidades
	vel[:,0] +=  a_x
	vel[:,1] +=  a_y
	pos = pos + vel
	bounce = abs(pos)>10
	circles.set_offsets(pos)
	plt.pause(0.05)