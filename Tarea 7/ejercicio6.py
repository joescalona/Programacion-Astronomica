#-*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#leer datos iniciales y asignarlos a las variables
pos_x, vel_x, pos_y, vel_y = np.loadtxt('datos_0.csv',delimiter='\t',unpack=True)

#Distancia relativa al (0.0)
dist0=np.sqrt(pos_x**2 + pos_y**2)
#subplot para tener 4 graficos en uno 
#idea de Franco Sepulveda
with plt.xkcd():
	plt.subplot(2,2,1)
	plt.title('Histograma en 0')
	plt.xlabel('Distribucion relativa')
	plt.ylabel('Numero de bolas')
	plt.hist(dist0)

#Energía cinética
Ek_0 = 0.5*(vel_x**2 + vel_y**2)
with plt.xkcd():
	plt.subplot(2,2,2)
	plt.title('Energia cinetica en 0')
	plt.xlabel('Energia cinetica')
	plt.ylabel('Numero de bolas')
	plt.hist(Ek_0)

#Leer datos en N-20
pos_x1, vel_x1, pos_y1, vel_y1 = np.loadtxt('datos.csv',delimiter='\t',unpack=True)
#Distancia relativa al (0.0) en N-20 iteraciones
dist1=np.sqrt(pos_x1**2 + pos_y1**2)
with plt.xkcd():
	plt.subplot(2,2,3)
	plt.xlabel('Distribucion relativa en N-20')
	plt.ylabel('Numero de bolas')
	plt.hist(dist1)

#Energía cinética
Ek_1 = 0.5*(vel_x1**2 + vel_y1**2)
with plt.xkcd():
	plt.subplot(2,2,4)
	plt.xlabel('Energia cinetica en N-20')
	plt.ylabel('Numero de bolas')
	plt.hist(Ek_1)
	#tight_layout para mejor estética
	plt.tight_layout()
plt.savefig('hist.pdf')