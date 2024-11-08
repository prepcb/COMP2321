import numpy as np

A = np.array([[1,1,1,1],[-3,1,0,0],[0,1,-2,0]])

print(A)


def VsV(a,b,n):
    return(b - a*(b[n]/a[n]))




for i in range(2):
     for j in range(i+1,3):
        print(i,j)
        A[j,:] = VsV(A[i,:],A[j,:],i)
print(A)


