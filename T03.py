import numpy as np

print("==========Give a matrix system:")
A = np.array([[1,1,1,11],[0,1,-2,0],[-3,1,0,0]])

print(A)


def VsV(a,b,n):
    return(b - a*(b[n]/a[n]))



print("======= L from Gausss elimnation")
for i in range(2):
    for j in range(i+1,3):
        A[j,:] = VsV(A[i,:],A[j,:],i)
print("L =")
print(A)

x = np.array([0,0,0])




#x[2]=(A[2,3])/A[2,2]
#x[1]=(A[1,3]-A[1,2]*x[2])/A[1,1]
#x[0]=(A[0,3]-A[0,1]*x[1]-A[0,2]*x[2])/A[0,0]

print("====== back substitution")
for i in range(3):
    j = 2 - i
    x[j]=A[j,3]
    for k in range(j+1,3):
        x[j] -=A[j,k]*x[k]
    x[j] = x[j]/A[j,j]
  
print(" x =",x)

print("=========Jacobi iteration")

A = np.array([[-3,1,0,0],[1,1,1,11],[0,1,-2,0]])
#A = np.array([[1,1,1,11],[0,1,-2,0],[-3,1,0,0]])

x = np.array([0.,0.,0.])
y = np.array([0.,0.,0.])
e = 1.
N = 0
while e > 0.001 and N<200:
    e = 0.
    for i in range(3):
        y[i] = x[i]+A[i,3]/A[i,i]
        for j in range(3):
            y[i]-=A[i,j]*x[j]/A[i,i]
        e += (x[i]-y[i])**2
    for i in range(3): #Gauss Siedel
        x[i] = y[i]
#    print(N,e)
    N +=1

print(A)
print(x,'number of iterations: ',N)

print("=========Gausss Seidel iteration")

A = np.array([[-3,1,0,0],[1,1,1,11],[0,1,-2,0]])
#A = np.array([[1,1,1,11],[0,1,-2,0],[-3,1,0,0]])

x = np.array([0.,0.,0.])
y = np.array([0.,0.,0.])
e =1.
N = 0
while e > 0.001 and N<200:
    e = 0.
    for i in range(3):
        y[i] = x[i]+A[i,3]/A[i,i]
        for j in range(3):
            y[i]-=A[i,j]*x[j]/A[i,i]
        e += (x[i]-y[i])**2
    #for i in range(3): #Gauss Siedel
        x[i] = y[i]
#    print(N,e)
    N +=1

print(A)
print(x,'number of iterations: ',N)

print("========== sparse matrix assembly")
A = np.array([[-3,1,0,0],[1,1,1,11],[0,1,-2,0]])
m = 0
p = []
for i in range(3):
    for j in range(3):
        if abs(A[i,j])>1e-6:
            p.append([i,j])
            m+=1
print(p,m)

print("=========sparse matrix multiplication test")

b = np.array([7,2,6])
c = np.array([0,0,0])
for i in range(3):
    for j in range(3):
        c[i] += A[i,j]*b[j]
print(c)

c = np.array([0,0,0])
for k in range(m):
    i,j = p[k]
    c[i] += A[i,j]*b[j]
print(c)



print("==========sparse matrix Jacobi")
x = np.array([0.,0.,0.])
y = np.array([0.,0.,0.])
e =1.
N = 0
while e > 0.001 and N<200:
    e = 0.
    for i in range(3):
        y[i] = x[i]+A[i,3]/A[i,i]
 #   for i in range(3):
 #       for j in range(3):
 #           y[i]-=A[i,j]*x[j]/A[i,i]


    for k in range(m):
        i,j = p[k]
        y[i]-=A[i,j]*x[j]/A[i,i]
    e = 0.
    for i in range(3):
        e += (x[i]-y[i])**2
    for i in range(3): #Gauss Siedel
        x[i] = y[i]
        # print(N,e)
    N +=1


print(x,N)





