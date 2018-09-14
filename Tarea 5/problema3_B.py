# -*-coding:utf-8-*-

#Fibonacci while loops 
def Fib_while(n):
	r = [1,1] #lista con 2 primeros terminos, aunque se pedirá el último. 
	while len(r) <= n: #la cantidad de elementos en la lista debe ser <= n 
		r.append(r[-1]+r[-2]) #agregar la suma del ultimo elemento con el penultimo
	return r[-1] #retornar el último

print '****** FIBONACCI (COMIENZA CON EL 1) ******'
N  = abs(int(raw_input('Ingresa la posición N que quieres saber: ')))
N2 = N - 1
print 'La posición',N,'de Fibonacci es',Fib_while(N2)



