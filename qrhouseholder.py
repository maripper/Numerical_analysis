import numpy as np

def norma(x):
    return np.sqrt(sum([x_i**2 for x_i in x]))
import math
import copy
def normaMatriz(X):
    valor = 0
    n=len(X)
    for i in range(n):
        v=0
        for j in range(n):
            v = v + abs(X[j][i])
        if(v > valor or i==0):
            valor = v
    return valor

def sistema_triang_inf(Rt, A):
    n=len(A)
    for i in range(n):
        if (i != 0):
            for j in range(n):
                valor=0
                for k in range(i):
                    valor = valor + (A[k][j] * Rt[i][k])
                A[i][j]=(A[i][j]-valor)/Rt[i][i]
        else:
            for j in range(n):
                A[i][j]=A[i][j]/Rt[i][i]
    return A
def sistema_triang_sup(R, A):
    n=len(A)
    for i in reversed(range(n)):
        if (i != (n-1)):
            for j in range(n):
                valor=0
                k=n-1
                while(k>i):
                    valor = valor + (A[k][j] * R[i][k])
                    k=k-1
                A[i][j]=(A[i][j]-valor)/R[i][i]
        else:
            for j in range(n):
                A[i][j]=A[i][j]/R[i][i]
    return A
def multiplica_matriz_vetor(A,b):
    y = []
    n=len(A)
    for i in range(n):
        v = 0
        for j in range(n):
            v = v + A[i][j] * b[j]
        y.append(v)
    return y
def multiplica_matriz(A,B):
    sizeL=len(A)
    sizeC=len(A[0])
    C=[]
    for i in range(sizeL):
        c = []
        for j in range(sizeC):
            c.append(0)
        C.append(c)
    for i in range(sizeL):
        for j in range(sizeC):
            val=0
            for k in range(len(B[0])):
                val = val + A[i][k]*B[k][j]
            C[i][j]=val
    return C
def transposta(M):
    n = len(M)
    return [[ M[i][j] for i in range(n)] for j in range(n)]
def Q_i(Q_min, i, j, k):
    if i < k or j < k:
        return float(i == j)
    else:
        return Q_min[i-k][j-k]
def householder(A):
    n = len(A)
    R = A
    Q = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        Q.append(l)
    # Householder
    for k in range(n-1):
        I = [[float(i == j) for i in range(n)] for j in range(n)]
        Rt= transposta(R)
        x=[]
        j=k
        while(j<n):
            x.append(Rt[k][j])
            j=j+1
        t=norma(x)
        nx=len(x)
        r = []
        r.append(t)
        j = 1
        while (j < nx):
            r.append(0)
            j = j + 1
        u=[]
        u=np.subtract(x,r)
        gama = 2/(pow(norma(u), 2))
        gama_u_ut = [[(float(i == j) - gama*u[i] * u[j]) for i in range(n - k)]for j in range(n - k)]
        Q_t = [[Q_i(gama_u_ut, i, j, k) for i in range(n)] for j in range(n)]
        if k == 0:
            Q = Q_t
            R = multiplica_matriz(Q_t, A)
        else:
            Q = multiplica_matriz(Q_t, Q)
            R = multiplica_matriz(Q_t, R)
    return transposta(Q), R


n = int(input("Tamanho da matriz:"))
A = []
print("insira a matriz A:")
for i in range(n):
    a = []
    for j in range(n):
        x = int(input())
        a.append(x)
    A.append(a)
Q, R = householder(A)
Qt = transposta(Q)
print ("A:",A)
print ("Q:",Q)
print ("R:",R)
#-------------------------------------------- Matriz  inversa ----------------------------------------------------
B = [[float(i == j) for i in range(n)] for j in range(n)]
Y=multiplica_matriz(Qt, B)
A_inv=sistema_triang_sup(R,Y)
print("Inversa de A:")
print(A_inv)
#----------------------------------número de condicionamento------------------------------------
K1=normaMatriz(A_inv)*normaMatriz(A)
print("número de condicionamento K1:",K1)
#--------------------------------------------AX=B-----------------------------------------------------------------
B = []
print("insira a matriz B:")
for i in range(n):
    b = []
    for j in range(n):
        x = int(input())
        b.append(x)
    B.append(b)

Y=multiplica_matriz(Qt, B)
X=sistema_triang_sup(R,Y)
print("Solução do sistema (AX=B) X : ")
print(X)
#---------------------------------------- Ax=b------------------------------------------------
print("insira o vetor b:")
b=[]
for i in range(n):
    bvalor = int(input())
    b.append(bvalor)
y=multiplica_matriz_vetor(Qt,b)
for i in range(n):
    for j in range(n):
        R[i][j]=round(R[i][j],10)
for i in reversed(range(n)):
    n1 = n-1
    if i != n1:
        j=n1
        while(j>i):
            y[i] = y[i] - R[i][j] * y[j]
            j=j-1
    if R[i][i] == 0:
        print("error")
        break
    else:
        y[i] = y[i] / R[i][i]
print("Solução do sistema (Ax=b)x = ",y)