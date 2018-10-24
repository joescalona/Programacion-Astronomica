#-*- coding:utf-8 

import numpy as np 

f = open('data1.txt','r') #abrimos el archivo 

#Leemos e ignoramos las lineas de encabezado 
header1 = f.readline()
header2 = f.readline()
header3 = f.readline()

name1 = [] #lista vacia con los futuros datos de name
jmag1 = [] #lista vacia con los futuros datos de jmag

#Hacemos un loop y sobre cada línea y extraimos los datos que queremos
for line in f:
	line = line.strip()
	columns = line.split()
	name = name1.append(columns[2]) #agregar a name1
	jmag = jmag1.append(float(columns[3])) #agregar a jmag1

np.savetxt('datos.txt',np.column_stack((name1,jmag1)),fmt='%5s',delimiter='\t')


	