import numpy as np

A = np.array([[1,1,1,11],[0,1,-2,0],[-3,1,0,0]])

print(A)


def VsV(a,b,n):
    return(b - a*(b[n]/a[n]))




for i in range(2):
     for j in range(i+1,3):
        print(i,j)
        A[j,:] = VsV(A[i,:],A[j,:],i)
print(A)

x = np.array([0,0,0])




#x[2]=(A[2,3])/A[2,2]
#x[1]=(A[1,3]-A[1,2]*x[2])/A[1,1]
#x[0]=(A[0,3]-A[0,1]*x[1]-A[0,2]*x[2])/A[0,0]

for i in range(3):
    j = 2 - i
    x[j]=A[j,3]
    for k in range(j+1,3):
        x[j] -=A[j,k]*x[k]
    x[j] = x[j]/A[j,j]
  
print(x)