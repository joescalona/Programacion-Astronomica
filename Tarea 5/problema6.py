#-*-coding: utf-8-*-
from math import factorial

print "******** TRIANGULO DE PASCAL ********"
#se pide el número de filas
f = abs(int(input('Ingresa el número de filas = ')))

n = 0
k = 0

#comienza un ciclo dentro del otro
while (n<=f):
    print ''
    while (k<=n):
        #numerador = n!
        num = factorial(n)
        # denominador = k! * (n-k)!
        den = (factorial(k)) * (factorial(n-k))
        #respuesta
        res = (num)/(den)
        #k aumentará para continuar con el ciclo
        #k aumentará hasta que se iguale con n 
        k = k+1
        #imprimir respuesta
        print res,#
    #variar n para continuar hasta la cantidad de filas  
    n=n+1
    #reiniciar k 
    k=0

