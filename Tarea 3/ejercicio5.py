from math import exp

#definimos funciones

# f1(x)---> x^2 - 4x 
# f1'(x)---> 2x - 4
def f1(x):
	return x**2 - 4*x

def df1(x):
	return 2*x-4

xnew = [3.0] #supuesto inicial
erro = 0.001 #error 
resp = xnew[-1] #raiz de la funcion

while True:
	print resp
	dres = -1 * f1(resp)/df1(resp)
	resp = resp + dres
	xnew.append(resp)
	if abs(xnew[-2]-xnew[-1] < erro):
		break



# f2(x) ---> e^x - 4x 
# df2(x) ---> e^x - 4
def f2(x):
	return exp(x) - 4*x
def df2(x):
	return exp(x) - 4 

xnew = [1.0] #supuesto inicial
erro = 0.001 #error 
resp = xnew[-1] #raiz de la funcion

while True:
	#rint resp
	resp = resp - (f2(resp)/df2(resp))
	xnew.append(resp)
	if abs(xnew[-2]-xnew[-1] < erro):
		break
print resp

#f3(x)--->10x - x^2
#df3(x)--->10 - 2x 
def f3(x):
	return 10*x - x**2 
def df3(x):
	return 10 - 2*x 

xnew = [1.0] #supuesto inicial
erro = 0.001 #error 
resp = xnew[-1] #raiz de la funcion

while True:
	#print resp
	resp = resp - (f3(resp)/df3(resp))
	xnew.append(resp)
	if abs(xnew[-2]-xnew[-1] < erro):
		break
print resp

