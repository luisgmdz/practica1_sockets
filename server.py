#!/usr/bin/env python3

import random
import socket
import time
HOST = "10.100.67.169"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
buffer_size = 1024


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
            matriz[x][y]=1#asignamos las minas a la matriz de manera aleatoria 
            minas.append([x,y])#guardamos la posicion de las minas 
    if n==17:
        for i in range (40):
            x=int(random.randint(1,n-1))
            y=int(random.randint(1,n-1))
            matriz[x][y]=1#asignamos las minas a la matriz de manera aleatoria
            minas.append([x,y])#guardamos la posicion de las minas 
    return matriz, minas



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOST, PORT))
    TCPServerSocket.listen()
    print("El servidor TCP está disponible y en espera de solicitudes")

    Client_conn, Client_addr = TCPServerSocket.accept()
    with Client_conn:
        print("Conectado a", Client_addr)

        while True:
            print("Esperando a recibir datos... ")
            data = Client_conn.recv(buffer_size)
            print ("los datos recibidos son:",str(data))
            data=data.decode(encoding="utf-8")
            #print("Dificultad*= ",data)
            if data =='1':
                matriz, minas=creaMatriz(9)
                for i in range (10):
                    print(matriz[i])
            elif data == '2':
                matriz, minas=creaMatriz(16)
                for i in range (17): 
                    print(matriz[i])
            else:
                print("El valor ingresado es incorrecto")
            print(minas)
            while True:
                verificar=Client_conn.recv(buffer_size)
                verificar=verificar.decode('utf-8')
                verificar=verificar.split(",")
                print("verificar es:", verificar)
                aux=[]
                print(verificar[0],verificar[1])
                aux.append([int(verificar[0]),int(verificar[1])])
                print(aux[0])
                if aux[0] in minas:
                    flag='0'
                    flag=flag.encode('utf-8')
                    Client_conn.send(flag)
                    break
                else:
                    flag='1'
                    flag=flag.encode('utf-8')
                    Client_conn.send(flag)
        TCPServerSocket.close()