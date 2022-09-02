import math
import copy
def norma(X):
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
def Cholesky_Decomposition(Ac, n):
    A = copy.deepcopy(Ac)
    inf = []
    #criar uma matriz de zeros:
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        inf.append(l)
    #colocar na primeira posição a raiz do primeiro elemento da matriz A
    inf[0][0] = int(math.sqrt(A[0][0]))
    for i in range(n):  # Decompondo A em uma matriz triangular Triangular inferior
        if (i != 0):
            for j in range(i):
                A[i][i] = A[i][i] - pow(inf[j][i], 2)
            if (A[i][i] <= 0):
                print("error")
                return
            else:
                inf[i][i] = int(math.sqrt(A[i][i]))
        k = i + 1
        while (k < n):
            if (i != 0):
                for l in range(i):
                    A[i][k] = A[i][k] - (inf[l][i] * inf[l][k])
            inf[i][k] = int(A[i][k] / inf[i][i])
            k = k + 1
    return inf

n = int(input("Tamanho da matriz:"))
A = []
print("insira a matriz A:")
for i in range(n):
    a = []
    for j in range(n):
        x = int(input())
        a.append(x)
    A.append(a)
r = Cholesky_Decomposition(A, n)
print("R:")
for i in range(n):
    for j in range(n):
        print(r[i][j], end = " ")
    print()
rt = []
for i in range(n):
    t = []
    for j in range(n):
        t.append(r[j][i])
    rt.append(t)
print("R Transposta:")
for i in range(n):
    for j in range(n):
        print(r[j][i], end = " ")
    print()
#---------------------------------------- Ax=b------------------------------------------------
b = []
print("insira o vetor b:")
for i in range(n):
    bvalor = int(input())
    b.append(bvalor)
for i in range(n):
    if i != 0:
        for j in range(i):
            b[i] = b[i] - rt[i][j] * b[j]
    if rt[i][i] == 0:
        print("error")
        break
    else:
        b[i] = b[i]/rt[i][i]
for i in reversed(range(n)):
    n1 = n-1
    if i != n1:
        j=n1
        while(j>i):
            b[i] = b[i] - r[i][j] * b[j]
            j=j-1
    if r[i][i] == 0:
        print("error")
        break
    else:
        b[i] = b[i] / r[i][i]
print("Solução do sistema x = ",b)
#-------------------------------------------- Matriz  inversa ----------------------------------------------------
B = [[float(i == j) for i in range(n)] for j in range(n)]
Y=sistema_triang_inf(rt, B)
A_inv=sistema_triang_sup(r,Y)
print("Inversa de A:")
print(A_inv)
#----------------------------------número de condicionamento------------------------------------
K1=norma(A_inv)*norma(A)
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

Y=sistema_triang_inf(rt, B)
X=sistema_triang_sup(r,Y)
print("Solução do sistema (AX=B) X : ")
print(X)
