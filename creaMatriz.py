import random
def creaMatriz(n):
    n=n+1
    matriz=[]
    minas=[]
    #print(n)
    for i in range(n):#este for nos permite crear un arreglo de listas de n*n
        a=[0]*n
        matriz.append(a)
    for i in range(n):
        matriz[i][0]=i#asignamos numero al eje y
        matriz[0][i]=i#asignamos letras al eje x
    if n==10:    
        for i in range (10):
            x=int(random.randint(1,n-1))
            y=int(random.randint(1,n-1))
            print("x=",x,"y=",y, "i=",i)
            matriz[x][y]=1#asignamos las minas a la matriz de manera aleatoria 
            minas.append([x,y])#guardamos la posicion de las minas 
    if n==17:
        for i in range (40):
            x=int(random.randint(1,n-1))
            y=int(random.randint(1,n-1))
            print("x=",x,"y=",y, "i=",i)
            matriz[x][y]=1#asignamos las minas a la matriz de manera aleatoria 
            minas.append([x,y])#guardamos la posicion de las minas 
    
    print(minas)
    return matriz, minas

matriz, minas=creaMatriz(16)
print(minas)
for i in range (10):
    print(matriz[i])
