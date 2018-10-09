#-*-coding: utf-8 

import numpy as np 
import matplotlib.pyplot as plt 

#Configuración de ejes 
with plt.xkcd():
	plt.axis([-10,10,-10,10])
#Se añadirá "punto con gravedad"
	plt.plot(0,0, marker ='*',c='r')
xx  = np.linspace(-10,10,100)
yy  = np.linspace(-10,10,100)
X,Y = np.meshgrid(xx,yy)
D = np.sqrt(X**2 + Y**2)
Z = -1./(15 + D**2)
cont = plt.contour(X,Y,Z,10)
#Para mayor elegancia (no caos), elegimos 1 bolita
n = 1
pos = (20*np.random.sample(n*2) - 10).reshape(n,2)
vel = (0.1*np.random.normal(size=n*2)).reshape(n,2)
sizes = 100*np.random.sample(n)+100
circles = plt.scatter(pos[:,0],pos[:,1],marker = 'o', s=sizes, c='g')

for i in range(100):
	#distancia al centro
	dis = np.sqrt(pos[:,0]**2 + pos[:,1]**2)
	#aceleracion (reducido en su decima parte)
	ace = (-1/(15 + dis**2))/0.1
	a_x = (ace)*pos[:,0]
	a_y = (ace)*pos[:,1]
	#velocidades
	vel[:,0] = vel[:,0] + a_x
	vel[:,1] = vel[:,1] + a_y
	pos = pos + vel
	bounce = abs(pos)>10
	circles.set_offsets(pos)
	with plt.xkcd():
		plt.pause(0.05)