#PARA CALCULAR EL TIEMPO DE DEMORA
from time import time
# UN NUMERO MUY GRANDE ES, POR EJEMPLO, 2 MILLONES
max=int(raw_input('Inserta un numero entero positivo: '))
#ACA VA EL INICIAL TIME YA QUE EL USUARIO SE PUEDE DEMORAR EN INGRESAR EL NUMERO
inicial=time()
i=0
#CICLO QUE FINALIZA CUANDO I > MAX 
while i < max:
    i = i+1
    print i 
final = time()
#TIEMPO TOTAL 
print(final-inicial)
#SI EL USUARIO INGRESA 2 MILLONES, EL PROGRAMA TARDA 9.48944306374(s) 
#ESTE TIEMPO CAMBIA EN CADA INTENTO, PERO APROXIMADAMENTE SON 9(s)
