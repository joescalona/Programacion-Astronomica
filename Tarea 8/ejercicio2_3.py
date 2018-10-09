#-*-coding: utf-8 

import numpy as np 
import matplotlib.pyplot as plt 

#funcion para vel en eje x
def vel_x(x):
		return x + a_x 
#funcion para vel en eje y
def vel_y(y):
		return y + a_y

#Configuración de ejes 
with plt.xkcd():
	plt.axis([-10,10,-10,10])
#Se añadirá "punto con gravedad"
	plt.plot(0,0, marker ='*',c='r')
#Para mayor elegancia (no caos), elegimos 1 bolita
n = 1
pos = (20*np.random.sample(n*2) - 10).reshape(n,2)
vel = (0.1*np.random.normal(size=n*2)).reshape(n,2)
sizes = 100*np.random.sample(n)+100
circles = plt.scatter(pos[:,0],pos[:,1],marker = 'o', s=sizes, c='g')
for i in range(100):
	x = vel[:,0]
	y = vel[:,1]
	#distancia al centro
	dis = np.sqrt(pos[:,0]**2 + pos[:,1]**2)
	#aceleracion (reducido en su decima parte)
	ace = (-1/(15 + dis**2))/0.1
	a_x = (ace)*pos[:,0]
	a_y = (ace)*pos[:,1]
	#velocidades
	vel[:,0] = vel_x(x)
	vel[:,1] = vel_y(y)
	pos = pos + vel
	bounce = abs(pos)>10
	circles.set_offsets(pos)
	#imprime cada velocidad 
	print '{} , {}'.format(vel_x(x),vel_y(y))
	with plt.xkcd():
		plt.pause(0.05)
