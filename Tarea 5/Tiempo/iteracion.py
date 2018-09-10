#-*-coding:utf-8-*-
def factorial_iterativo(n):
    '''Función que recibe un número n y retorna n!
    '''
    mul = 1 #primera multiplicación de la iteración
    for i in range(1,n+1): #itera hasta n
        mul = mul * i #1*2*3*4*..*n
    return mul
