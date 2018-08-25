#IMPORTAR RANDOM PARA ELEGIR UN ELEMENTO AL AZAR
import random 

nombres = ['Amelia','Luis','Jaime','Neil','Constanza','Joaquin','Yuuki']
#IDEA SACADA DEL LINK EN EL ENUNCIADO
nom_elegido=random.choice(nombres)
#print nom_elegido
#IMPRIMIR CONDICIONES DEL JUEGO
print('------ ADIVINA EL NOMBRE ------')
print('\n Tendras solo 3 oportunidades')
print('Los nombres a elegir son = ')
for i in nombres:
    print '*',i

#PEDIR UN NOMBRE
n=raw_input('\n Comencemos, elige un nombre = ')
#CONTADOR (POSIBILIDADES) = 1
count = 1
#CICLO CON TOPE = 3
while True:
#SI EL USUARIO ADIVINA
    if n == nom_elegido:
        print ('Correcto! has adivinado :)')
        break
#SINO, SE DESCUENTA UNA POSIBILIDAD (AGREGANDOLE A COUNT)   
    else: 
        count+=1
#NONE NECESARIO PARA QUE EL USUARIO VUELVA A INTENTAR
        n=None
        n=raw_input('\n Nope, intentalo nuevamente,elige un nombre = ')
#SI LLEGA A 3 POSIBILIDADES
        if count == 3:
            print ('Has ocupado tus 3 opciones')
            print 'El nombre era = ',nom_elegido
            break 



