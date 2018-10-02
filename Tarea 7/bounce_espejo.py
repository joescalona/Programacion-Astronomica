#-*-coding:utf-8 

import numpy as np 
import matplotlib.pyplot as plt 

plt.figure(1)			
plt.clf()
plt.axis([-10,10,-10,10,])	


n     = 10
pos   = (20 * np.random.sample(n*2)-10).reshape(n,2)
vel   = (0.3 * np.random.normal(size=n*2)).reshape(n,2)
sizes = 100 * np.random.sample(n)+100


colors = np.random.sample([n,4])

circles = plt.scatter(pos[:,0],pos[:,1],marker = 'o',s = sizes,c=colors)


for i in range(1000):
	pos = pos + vel  
	bounce = abs(pos) > 10  
	pos[bounce] = -pos[bounce]
	circles.set_offsets(pos)    
	plt.pause(0.05)

