import csv
import numpy as np

def readm(fname='A.csv'):
    f= open(fname,'r')
    A=[]
    for line in f.readlines():
        A.append([float(x) for x in line.strip().split(',')])
    f.close()
    return A


#def mutmul(A,b):
    #m,n = len(A), len(b[0])
    #J = len(A[0])
    #if len(A[0]) == len(b):
        #C = [ [0]*n for i in range(m) ]
        #for r in range(m):
            #for c in range(n):
                #C[r][c] = sum([ A[r][j]*b[j][c] for j in range(J)])
        #return C
    #return[]
def guass(a,b):
    a = np.array(a)
    b=np.array(b)
    n=len(a)
    for k in range(0, n-1):
      for i in range(k+1, n):
        if a[i,k] != 0.0:
            lam = a[i,k]/a[k,k]
            a[i,k+1:n] = a[i, k+1:n] - lam*a[k,k+1:n]
            b[i] = b[i] - lam*b[k]
    x=[0]*n
    for k in range(n-1, -1, -1):
      x[k] = (b[k] - np.dot(a[k,k+1:n], x[k+1:n]))/a[k,k]
    return x

a=readm('A.csv')
b=readm('b.csv')
print(guass(a,b))