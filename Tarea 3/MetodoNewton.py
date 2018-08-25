import numpy as np 
import matplotlib.pyplot as plt 

def f(x):
    return x**2 - 2

def df(x):
    return 2*x 

#comienza en -2 y termina en 2, con 98 numeros entre medio
x = np.linspace(-2,2,100)
plt.figure(num='Newton')
plt.plot(x,f(x))
plt.grid('on')
plt.show()

xNew = [4.0] #valor inicial
erro = 0.001
resp = xNew[-1]

print '%11s %11s' % ('x','f(x)')
while True:
    print '%11.8f % 11.8f' % (resp, f(resp))
    dres = -1 * f(resp)/df(resp)
    resp = resp + dres
    xNew.append(resp)
    if abs(xNew[-2]-xNew[-1] < erro):
        break

xNew = np.array(xNew)
x = np.linspace(0,5,100)
plt.figure(num='Newton')
plt.clf()
plt.plot(x,f(x))
plt.plot(xNew, f(xNew),'ko',ms=6)
plt.grid('on')
plt.show()