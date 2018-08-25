#definimos funciones

# f1(x)---> x^2 - 4x 
# f1'(x)---> 2x - 4
def f1(x):
    return x**2 - 4*x

def df1(x):
    return 2*x-4

#supuesto inicial (con 2.0 retorna ZeroDivisionError)
xnew = [3.0]
#error tolerado al aproximar 
erro = 0.001 
#raiz de la funcion
resp = xnew[-1]
print '-------- Metodo de Newton --------'
print 'Funcion = x^2 - 4x'
#try/except por si ocurre division por 0
try:
    while True:
        print 'Mejor aproximacion = ',resp
#metodo de newton-raphson
        resp = resp - (f1(resp)/df1(resp))
#agregar esta resp a xnew
        xnew.append(resp)
#alcanzar el error exigido
        if abs(xnew[-2]-xnew[-1]) <= erro:
            break
except (ZeroDivisionError):
    print 'Ha ocurrido una division por 0. No se puede continuar'
print '***La aproximacion final es',resp 