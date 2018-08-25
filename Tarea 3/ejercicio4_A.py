#EXHAUSTIVE ENUMERATION
#SE DEFINE FUNCION RAIZ CUBICA
#DESCARADAMENTE COPIADO DEL MATERIAL ENVIADO POR PROFESORA
#PUEDES ENCONTRAR EL ORIGINAL EN LECTURE3-4, PAG 68
#LOS PASOS MATEMATICOS LOS EXPLICA LA PROFESORA MUCHO MEJOR QUE YO
#SIN EMBARGO TRATARE DE DEJAR MIS COMENTARIOS CON LO QUE EL PROGRAMA HACE
def raiz_cubica(x):
#PRECISION
    epsilon = 0.01 
    step = epsilon**3
    ans = 0.0
#CONTADORA DE ITERACIONES
    count=0

    while abs(ans**3 - x) >= epsilon and ans <=x:
#AGREGAR ITERACION HASTA QUE SE ROMPA EL CICLO
        count+=1
        ans += step
    if abs(ans**3 - x) >= epsilon:
        print 'No hemos encontrado la raiz de ',x
        
    print '* La raiz de', x, 'es aproximadamente', ans
    print '* Ocurrieron',count,'iteraciones \n'
raiz_cubica(25)
raiz_cubica(500)
raiz_cubica(10000)
