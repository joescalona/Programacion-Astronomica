#definimos funciones

#f3(x)--->10x - x^2
#df3(x)--->10 - 2x 
def f3(x):
    return 10*x - x**2 
def df3(x):
    return 10 - 2*x 

#supuesto inicial
xnew = [7.0]
#error tolerado al aproximar 
erro = 0.001 
#raiz de la funcion
resp = xnew[-1]
print '-------- Metodo de Newton --------'
print 'Funcion = 10 - x^2'
#try/except por si ocurre division por 0
try:
    while True:
        print 'Mejor aproximacion = ',resp
#metodo de newton-raphson
        resp = resp - (f3(resp)/df3(resp))
#agregar esta resp a xnew
        xnew.append(resp)
#alcanzar el error exigido
        if abs(xnew[-2]-xnew[-1]) <= erro:
            break
except (ZeroDivisionError):
    print 'Ha ocurrido una division por 0. No se puede continuar'
print '***La aproximacion final es',resp 
