#-*- coding:utf-8 -*- 

import numpy as np
import matplotlib.pyplot as plt

#Se configuran los ejes
plt.axis([-10,10,-10,10])
#Se añade el punto con 'gravedad'
plt.plot(0,0,marker='*',c='r')
n=10
pos=(20*np.random.sample(n*2)-10).reshape(n,2) 
vel=(0.1*np.random.normal(size=n*2)).reshape(n,2)    
sizes=100*np.random.sample(n)+100
#propiedades de bolas                       
colors=np.random.sample([n,4])                    
circles=plt.scatter(pos[:,0], pos[:,1], marker="o", s=sizes, c=colors)


def P(x):
	'''
	Entrega aceleración cuya X esté con distribución normal. 
	Las variables son
	mu,sigma
	'''
	mu=(sum(x)/n)   		  #Promedio de las posiciones
	sig=10	        		  #sigma.
	ra=sig*np.sqrt(2*np.pi)   #raiz de la función 
	num=x-mu               	  #numerador de la función
	S=10				      #desface
	pot=-0.5*(num/sig)**2     #exponente
	X=(1/ra)*np.exp(pot)      #distribución gausseana a x
	dist=np.sqrt(X**2+pos[:,1]**2) #Se crea una variable de distancia.
	a=(-1/(S+dist**2))      #Nuevo factor de aceleracion.
	ax=(a/2)*pos[:,0]       #Nueva aceleracion en X.
	return ax

for i in range(1000):
	x=pos[:,0]               #Se crea una variable con las posiciones originales de x.
	vel[:,0]=vel[:,0]+P(x)   #Se añade la aceleracion a la velocidad de x.
	pos=pos+vel              
	bounce=abs(pos) > 10
	vel[bounce]=-vel[bounce]
	circles.set_offsets(pos)
	plt.pause(0.05)