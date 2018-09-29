#-*- coding:utf-8 -*-

import numpy as np 										#importamos librerias
import matplotlib.pyplot as plt
from scipy.stats import  norm 

with plt.xkcd():
	ran = np.random.normal(size=10000)					#valor aleatorio
	x   = np.linspace(-4,4,100000)
	plt.hist(ran,bins = 50,density = 1)					
	plt.plot(x,norm.pdf(x),'g',lw=3)
plt.savefig('1_2.pdf')
plt.show() 


