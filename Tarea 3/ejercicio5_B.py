#para la funcion exponencial
from math import exp
# definimos funciones
# f2(x) ---> e^x - 4x 
# df2(x) ---> e^x - 4
def f2(x):
    return exp(x) - 4*x
def df2(x):
    return exp(x) - 4 

#supuesto inicial
xnew = [3.0]
#error tolerado al aproximar 
erro = 0.001 
#raiz de la funcion
resp = xnew[-1]
print '-------- Metodo de Newton --------'
print 'Funcion = e^x - 4x'
#try/except por si ocurre division por 0
try:
    while True:
        print 'Mejor aproximacion = ',resp
#metodo de newton-raphson
        resp = resp - (f2(resp)/df2(resp))
#agregar esta resp a xnew
        xnew.append(resp)
#alvanzar el error exigido
        if abs(xnew[-2]-xnew[-1]) <= erro:
            break
except (ZeroDivisionError):
    print 'Ha ocurrido una division por 0. No se puede continuar'
print '***La aproximacion final es',resp 