
# coding: utf-8

# In[6]:




def encrip(string,desplazamiento):
    #crear abecedario para ver si el caracter pertenece al abc o no
    abc ='abcdefghijklmnopqrstuvwxyz'
    cod = ''
    for car in string:
    #si el caracter pertenece a los caracteres del diccionario, hacer el código que ya tenás
        if car in abc:
            if car == '':
                cod = cod + car
            else:
                 cod = cod + chr((ord(car) + desplazamiento-97)%26+97)
    #sino está el caracter, significa que es un espacio o algún otro caracter rarito. Y si es así, entonces que sume la letra nomás.
        else:
            cod = cod + car 
    return cod

texto = raw_input('Ingresar texto= ')
s = int(input('Ingresar valor de desplazamiento= '))
print ('Texto encriptado = ',encrip(texto,s))

