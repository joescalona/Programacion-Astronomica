from math import sqrt 
#APARTADO A)
#-------------------------
#DEFINIMOS FUNCION QUE ARROJA SI UN VALOR ES PRIMO O NO 
#INPUT = X
#SI X ES PRIMO, RETORNA 1
#SI NO, RETORNA 0

def es_primo(x):
#INICIO LOOP DESDE 2 HASTA X-1 
    for i in range(2,x):

#LA FUNCION -IF ANY(LISTA)- LA APRENDI EN SOLOLEARN (SECCION "MAS TIPOS >> FUNCIONES 
#UTILES")
#PARA QUE UN NUMERO SEA PRIMO, ESTE DEBE SER DIVISIBLE SOLO POR 1 Y EL MISMO
#POR LO TANTO SI EXISTIERA ALGUN i (IF ANY) QUE EL CUOCIENTE ENTRE EL NUMERO E i 
#SEA IGUAL A 0
#EL NUMERO NO ES PRIMO (Y LA FUNCION RETORNARA 0)
        if any([x%i==0]):
            return 0 
    return 1
#-------------------------
#APARTADO B)
y = int(input('Ingresa un numero y dire si es el cuadrado de un primo = '))

#SI NUMERO INGRESADO ES MAYOR A 0, SE SACA LA RAIZ DEL NUMERO
if y>0:
    raiz=int(sqrt(y))
#SINO, PEDIR QUE SEA POSITIVO
else: 
    print('Debe ser positivo')
#1 POR CONVENIO, NO ES CONSIDERADO PRIMO 
#LO LEI AQUI: https://es.wikipedia.org/wiki/N%C3%BAmero_primo
if raiz==1:
    print('No lo es :( ')
#SI LA RAIZ ES DISTINTO DE 1
else:
#SI LA RAIZ ES PRIMO (VER APARTADO A)
    if es_primo(raiz) == 1:
        print 'Lo es! del primo ',raiz
    else:
        print('No lo es :( ')

