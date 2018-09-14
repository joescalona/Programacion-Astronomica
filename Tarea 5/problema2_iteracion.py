#-*-coding:utf-8-*-

#Factorial Iterativo
def factorial_iterativo(n):
    '''Función que recibe un número n y retorna n!
    '''
    mul = 1 #primera multiplicación de la iteración
    for i in range(1,n+1): #itera hasta n
        mul = mul * i #1*2*3*4*..*n
    return mul

print '****** FACTORIAL DE UN NUMERO ******'

num = abs(int(input('Número (se considerará parte entera y el valor absoluto) = ')))

print 'El factorial de',num,'es',factorial_iterativo(num)
