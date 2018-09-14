#-*-coding:utf-8-*-
import matplotlib.pyplot as plt 
import numpy as np
import time
#Fibonacci Recursivo 
#Esta serie comienza con el numero 1.
def Fib_Recursivo(n):
	if n < 2:
		return 1
	else: 
		return (Fib_Recursivo(n-1) + Fib_Recursivo(n-2))

def tiempo_fib(n):
	ini = time.clock()
	Fib_Recursivo(n)
	fin = time.clock()
	tot = fin - ini 
	return tot   	

x = np.arange(0,34)


with plt.xkcd():
	fig = plt.figure(figsize=(8,5),dpi=100)
	plt.plot([tiempo_fib(i) for i in x],x,'b.-')
	plt.xlabel('tiempo')
	plt.ylabel('Posicion')
	plt.title('Fibonacci mediante recursion')
	plt.savefig('recursion.png')
#plt.show()