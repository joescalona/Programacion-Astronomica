#-*-coding:utf-8 

import numpy as np 
import matplotlib.pyplot as plt 

plt.figure(1)			
plt.clf()
plt.axis([-10,10,-10,10,])	


n     = 1000
pos   = (20 * np.random.sample(n*2)-10).reshape(n,2)
vel   = (0.3 * np.random.normal(size=n*2)).reshape(n,2)
sizes = 100 * np.random.sample(n)+100


colors = np.random.sample([n,4])

circles = plt.scatter(pos[:,0],pos[:,1],marker = 'o',s = sizes,c=colors)



#N iteraciones (100)
for i in range(100):
	pos = pos + vel  
	bounce = abs(pos) > 10
	vel[bounce] = -vel[bounce]
	#datos inicial 
	if (i == 0):
		np.savetxt('datos_0.csv',np.column_stack((pos[:,0],vel[:,0],pos[:,1],vel[:,1])),delimiter="\t",header='pos_x \t Vel X \t pos y\t Vel Y')
	#datos con N-20 
	elif (i == (100-20)):
		np.savetxt('datos.csv',np.column_stack((pos[:,0],vel[:,0],pos[:,1],vel[:,1])),delimiter="\t",header='pos_x \t Vel X \t pos y\t Vel Y')
	circles.set_offsets(pos)    
	plt.pause(0.05)

