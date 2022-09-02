import numpy as np

m = 3 #numero de linhas de A
n = 3 #numero de colunas de A
A = [[1, 1/2, 1/3],[1/2, 1/3, 1/4],[1/3, 1/4, 1/5]]

def norma(x): #Função calcula a norma de um vetor
    return np.sqrt(sum([x_i**2 for x_i in x]))


def GramSchmidt(A, m, n): #realiza a fatoração QR pelo processo de Gram-Schmidt
    Q = A 
    R = np.zeros((n,n))
    w = np.zeros(m)
    flag = 0
    #Gram-Schmidt
    for i in range(1,n):
        w = A[:][i]
        if i != 0:
            for j in range(1,i-1):
                print("kek")
                R[j][i] = np.dot((np.transpose(Q[:][j])),A[:][i])
                w = w - np.dot(R[j][i], Q[:][j])
                R[i,i] = norma(w)
                if R[i][i] == 0:
                    flag = 1
                    break
                else:
                    Q[:][i] = w/R[i][i]

    return Q, R, flag

Q, R, flag = GramSchmidt(A, m, n)

print(Q)
print(R)