# PARA PARAR EL PROGRAMA AL CABO DE X SEGUNDOS IMPORTAMOS CLOCK
# IDEA SACADA DE: # https://recursospython.com/guias-y-manuales/scheduler/
from time import clock
#TIEMPO INICIAL
inicial=0
i=0
while True:
#TIEMPO ACTUAL
    actual=clock()
    i = i+1
    print i
#SI EL TIEMPO ES MAYOR A 2 SEGUNDOS, PARAR
    if (actual - inicial) > 2:
        break 
