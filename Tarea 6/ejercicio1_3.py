#-*- coding:utf-8 -*-

import numpy as np 										#importamos librerias
import matplotlib.pyplot as plt


T = np.zeros(10000)
for x in range(10):
	v = np.random.random(10000)
	T += v

with plt.xkcd():
	plt.hist(T/10,bins=30)
plt.savefig('1_3.pdf')
plt.show()