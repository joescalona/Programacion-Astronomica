import time 

i=1
while True:
    print "Welcome", i, "times. To stop press [CTRL + C]"
    i+=1
        #Delay for 2 seconds
    time.sleep(2)
        #SI I ES IGUAL A 7, BREAK. (EL PROGRAMA SALUDARA 6 VECES )
    if i == 7:
        break 